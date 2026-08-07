<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://pegasus.isi.edu/documentation/_static/pegasus_circular_white_logo.png" width="100"/>

# Execution Instances for the SRA Search Workflow

## Workflow Description

[SRA](https://www.ncbi.nlm.nih.gov/sra/) is a toolkit that provides a collection of
tools and libraries for using data in the INSDC Sequence Read Archives. Much of the
data submitted these days contains alignment information, for example in BAM,
Illumina export.txt, and Complete Genomics formats. The test case implemented as a
[Pegasus workflow](https://github.com/pegasus-isi/sra-search-pegasus-workflow) aims
to download and align SRA data, using SRA Toolkit, Samtools and Bowtie2. This test
case is composed of four different tasks:

  1. `fasterq-dump` – converts SRA data into FASTQ format.
  2. `bowtie2-build` – indexes the genome with an FM Index (based on the
     Burrows-Wheeler Transform or BWT) to keep its memory footprint small.
  3. `bowtie2` – aligns sequencing reads to long reference sequences.
  4. `merge` – merges a set of BAM files into a final tarball.

The figure below shows an overview of the SRA Search workflow structure:

<img src="docs/images/srasearch.png?raw=true" width="600">

## Execution Instances

Execution instances are formatted according to
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

Instance files are named using the following convention:
`srasearch-<COMPUTE_PLATFORM>-<ACCESSION_LIST_SIZE>a-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Pegasus workflow was
  executed (`chameleon`).
- `<ACCESSION_LIST_SIZE>`: The number of NCBI accession numbers processed by the
  workflow.
- `<RUN_ID>`: The workflow execution identification — each accession list size was
  executed several times.

These are the smallest production workflows in this repository, but with
comparatively long task runtimes (data download and alignment), which makes their
makespans vary noticeably across repeated runs:

| `<ACCESSION_LIST_SIZE>` | Tasks | Files | Makespan (observed range) |
| ---: | ---: | ---: | --- |
| 10 | 22 | 48 | 1,486 – 5,813 s |
| 20 | 42 | 88 | 7,576 – 7,878 s |
| 30 | 64 | 130 | 7,479 – 10,492 s |
| 40 | 84 | 170 | 5,465 – 11,419 s |
| 50 | 104 | 210 | 5,641 – 12,339 s |

### Workflow Structure

The SRA Search workflow structure depends exclusively on the number of NCBI
accession numbers (`<ACCESSION_LIST_SIZE>`): each accession number is processed by a
`fasterq-dump` task, which is followed by a `bowtie2` task. The workflow has a
single `bowtie2-build` task (regardless of the number of accessions). It also ends
with an upside-down triangle of `merge` tasks: one `merge` task is added for every
25 `bowtie2` tasks, and if more than a single `merge` task has been added, a final
`merge` task (to merge all data from the previous merge tasks) is appended.
