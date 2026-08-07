<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://pegasus.isi.edu/documentation/_static/pegasus_circular_white_logo.png" width="100"/>

# Execution Instances for the 1000Genome Workflow

## Workflow Description

The [1000 Genomes Project](https://www.internationalgenome.org) provides a reference
for human variation, having reconstructed the genomes of 2,504 individuals across 26
different populations. The test case implemented as a
[Pegasus workflow](https://github.com/pegasus-isi/1000genome-workflow) identifies
mutational overlaps using data from the 1000 Genomes Project in order to provide a
null distribution for rigorous statistical evaluation of potential disease-related
mutations. This test case is composed of five different tasks:

  1. `individuals` – fetches and parses the Phase 3 data from the 1000 Genomes
     Project per chromosome;
  2. `individuals_merge` – combines all outputs of the `individuals` tasks into a
     single file;
  3. `sifting` – computes the SIFT scores of all of the SNPs (single nucleotide
     polymorphisms) variants, as computed by the Variant Effect Predictor;
  4. `mutation_overlap` – measures the overlap in mutations (SNPs) among pairs of
     individuals; and
  5. `frequency` – calculates the frequency of overlapping mutations across
     subsamples of certain individuals.

The figure below shows **a branch** of the 1000Genome workflow for the analysis of a
**single chromosome**.

<img src="docs/images/1000genome.png?raw=true" width="450">

### Research Publication

Details of the 1000Genome workflow description, computational jobs, and performance
metrics can be found in the following research publication:

- Ferreira da Silva, R., Filgueira, R., Deelman, E., Pairo-Castineira, E.,
  Overton, I. M., & Atkinson, M. (2019). Using Simple PID-inspired Controllers
  for Online Resilient Resource Management of Distributed Scientific Workflows.
  Future Generation Computer Systems, 95, 615–628.
  https://doi.org/10.1016/j.future.2019.01.015

## Execution Instances

Execution instances are formatted according to
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

Instance files are named using the following convention:
`1000genome-<COMPUTE_PLATFORM>-<NUM_CH>ch-<NUM_SEQ>-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Pegasus workflow was
  executed (`chameleon`).
- `<NUM_CH>`: The number of chromosomes evaluated in the workflow execution
  (2 to 22, in steps of 2).
- `<NUM_SEQ>`: The number of sequences per chromosome file (`100k` or `250k`).
- `<RUN_ID>`: The workflow execution identification.

The number of chromosomes (`<NUM_CH>`) impacts the number of tasks in the workflow,
while the number of sequences per chromosome file (`<NUM_SEQ>`) impacts the workflow
data footprint (both input and output data), as well as task runtime — and, in these
executions, the number of `individuals` tasks.

The table below summarizes the parameter combinations available in this directory:

| `<NUM_CH>` | Tasks (`100k`) | Makespan (`100k`) | Tasks (`250k`) | Makespan (`250k`) |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 52 | 776 s | 82 | 2,391 s |
| 4 | 104 | 1,391 s | 164 | 2,924 s |
| 6 | 156 | 1,522 s | 246 | 3,348 s |
| 8 | 208 | 1,787 s | 328 | 5,138 s |
| 10 | 260 | 2,814 s | 410 | 5,053 s |
| 12 | 312 | 2,091 s | 492 | 6,433 s |
| 14 | 364 | 2,290 s | 574 | 7,401 s |
| 16 | 416 | 2,498 s | 656 | 7,879 s |
| 18 | 468 | 2,533 s | 738 | 10,038 s |
| 20 | 520 | 2,765 s | 820 | 9,460 s |
| 22 | 572 | 3,014 s | 902 | 10,417 s |

### Workflow Structure

The 1000Genome workflow structure depends on the _number of chromosomes_
(`<NUM_CH>`) evaluated and the _number of sequences per chromosome_ (`<NUM_SEQ>`).
The workflow consists of one independent **branch** per chromosome. For a *single
branch*:

- Each `individuals` task evaluates a fixed number of sequences, so the number of
  `individuals` tasks per branch grows with `<NUM_SEQ>`: 10 tasks for `100k` and 25
  tasks for `250k` in these executions;
- There is only _one_ `individuals_merge` task per branch;
- There is only _one_ `sifting` task per branch;
- The number of `mutation_overlap` and `frequency` tasks per branch is driven by the
  number of **populations** (e.g., African, Mixed American, East Asian, European,
  South Asian) being evaluated — 7 of each per branch in these executions.

A per-branch total is therefore 26 tasks for `100k` and 41 tasks for `250k`.

An equivalent [CWL implementation of this workflow](../../streamflow), executed with
StreamFlow, is also available in this repository.
