<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://raw.githubusercontent.com/cooperative-computing-lab/cctools/master/doc/manuals/logos/makeflow-logo.png" width="160" />

# Execution Instances for the BLAST Workflow

## Workflow Description

[BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) is a toolkit for finding regions
of similarity between biological sequences. The program compares nucleotide or
protein sequences to sequence databases and calculates the statistical significance.
The test case implemented as a
[Makeflow workflow](https://github.com/cooperative-computing-lab/makeflow-examples/tree/master/blast)
aims to run BLAST tasks against large reference databases in a reasonable amount of
time. This test case is composed of four different tasks:

  1. `split_fasta` – splits the reference file into pieces.
  2. `blastall` – runs the BLAST program.
  3. `cat_blast` – merges results from each BLAST execution.
  4. `cat` – merges error messages from each BLAST execution.

The figure below shows an overview of the BLAST workflow structure:

<img src="docs/images/blast.png?raw=true" width="500">

## Execution Instances

Execution instances are formatted according to
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

Instance files are named using the following convention:
`blast-<COMPUTE_PLATFORM>-<WF_SIZE>-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Makeflow workflow was
  executed (`chameleon`).
- `<WF_SIZE>`: The size of the workflow (`small`, `medium`, `large`), which depends
  on the query size and the number of sequences per split.
- `<RUN_ID>`: The workflow execution identification — each workflow size was
  executed several times.

| `<WF_SIZE>` | `blastall` tasks | Total tasks | Files | Makespan (observed range) |
| --- | ---: | ---: | ---: | --- |
| `small` | 40 | 43 | 127 | 903 – 1,987 s |
| `large` | 100 | 103 | 307 | 3,216 – 3,908 s |
| `medium` | 300 | 303 | 907 | 5,074 – 6,317 s |

Note that `<WF_SIZE>` characterizes the input configuration rather than the task
count: `medium` runs use a larger query split into more pieces than `large` runs,
and therefore yield more (but individually shorter) `blastall` tasks.

### Workflow Structure

The BLAST workflow structure is only dependent on the _workflow size_
(`<WF_SIZE>`), which defines the number of `blastall` tasks — it depends on the
query size and number of sequences per split (as defined in the
[workflow GitHub repository](https://github.com/cooperative-computing-lab/makeflow-examples/tree/master/blast)).
The workflow also has three additional tasks: a single `split_fasta` task that
precedes all `blastall` tasks, and single `cat_blast` and `cat` tasks that follow
them.
