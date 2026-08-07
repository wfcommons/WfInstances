<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://raw.githubusercontent.com/cooperative-computing-lab/cctools/master/doc/manuals/logos/makeflow-logo.png" width="160" />

# Execution Instances for the BWA Workflow

## Workflow Description

[BWA](http://bio-bwa.sourceforge.net) is a software package for mapping
low-divergent sequences against a large reference genome, such as the human genome.
The test case implemented as a
[Makeflow workflow](https://github.com/cooperative-computing-lab/makeflow-examples/tree/master/bwa)
aims to run BWA tasks against large reference databases in a reasonable amount of
time. This test case is composed of five different tasks:

  1. `fastq_reduce` – subsamples the reference file into parts.
  2. `bwa_index` – produces the index from the reference file.
  3. `bwa` – searches for the queries in a shared reference database.
  4. `cat_bwa` – merges results from each BWA execution.
  5. `cat` – merges error messages from each BWA execution.

The figure below shows an overview of the BWA workflow structure:

<img src="docs/images/bwa.png?raw=true" width="500">

## Execution Instances

Execution instances are formatted according to
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

Instance files are named using the following convention:
`bwa-<COMPUTE_PLATFORM>-<WF_SIZE>-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Makeflow workflow was
  executed (`chameleon`).
- `<WF_SIZE>`: The size of the workflow (`small`, `medium`, `large`), which depends
  on the query size and the number of sequences per split.
- `<RUN_ID>`: The workflow execution identification — each workflow size was
  executed several times.

| `<WF_SIZE>` | `bwa` tasks | Total tasks | Files | Makespan (observed range) |
| --- | ---: | ---: | ---: | --- |
| `small` | 100 | 104 | 312 | 690 – 847 s |
| `medium` | 1,000 | 1,004 | 3,012 | 4,608 – 5,482 s |
| `large` | 1,000 | 1,004 | 3,012 | 46,527 – 57,274 s |

`medium` and `large` runs share the same structure (the same number of `bwa`
tasks); they differ in the size of the query data processed by each task, which is
why the `large` makespans are an order of magnitude longer. This makes the pair
useful for studying task-runtime distributions at a fixed workflow shape.

### Workflow Structure

The BWA workflow structure is only dependent on the _workflow size_ (`<WF_SIZE>`),
which defines the number of `bwa` tasks — it depends on the query size and number of
sequences per split (as defined in the
[workflow GitHub repository](https://github.com/cooperative-computing-lab/makeflow-examples/tree/master/bwa)).
The workflow also has four additional tasks: single `fastq_reduce` and `bwa_index`
tasks that precede all `bwa` tasks, and single `cat_bwa` and `cat` tasks that follow
them.
