<img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" />
<img src="https://pegasus.isi.edu/documentation/_static/pegasus_circular_white_logo.png" width="100"/>

# Execution Instances for Epigenomics Workflow

## Workflow Description

The Epigenomics workflow is a data processing pipeline for executing various
genome sequencing operations. DNA sequence data generated by the Illumina-Solexa
Genetic Analyzer system is split into several chunks that can be operated on
in parallel. The data in each chunk is converted into a file format that can
be used by the Maq software that maps short DNA sequencing reads. From there,
the sequences are filtered to remove noisy and contaminating segments and
mapped into the correct location in a reference genome. Finally, a global map
of the aligned sequences is generated and the sequence density at each position
in the genome is calculated. This workflow allows the processing of production
DNA methylation and histone modification data. The workflow is composed of fourteen different tasks:

  1. `fastqSplit`
  2. `filterContams`
  3. `sol2sanger`
  4. `fast2bfq`
  5. `map`
  6. `mapMerge`
  7. `chr21`
  8. `pileup`

The figure below shows an overview of the Epigenomics workflow structure:

<img src="docs/images/epigenomics.png?raw=true" width="450">

### Research Publication

Details of the Epigenomics workflow description, computational jobs, and
performance metrics can be found in the following research publication:

- G. Juve, A. Chervenak, E. Deelman, S. Bharathi, G. Mehta, and K. Vahi,
 "Characterizing and Profiling Scientific Workflows," Future Generation
 Computer Systems, vol. 29, iss. 3, pp. 682-692, 2013.

## Execution Instances

Execution instances are formatted according to the
[WfCommons JSON format](https://github.com/wfcommons/workflow-schema)
for describing workflow executions. Execution instances from different
computing platforms are organized into sub-folders.

Instance files are named using the following convention:
`epigenomics-<COMPUTE_PLATFORM>-<DATASET>-<NUM_SEQ>-<BIN_SIZE>-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Pegasus workflow
  was executed (e.g., `chameleon`).
- `<DATASET>`: Input dataset (e.g., `hep`, `ilmn`).
- `<NUM_SEQ>`: Number of FASTQ files processed by the workflow.
- `<BIN_SIZE>`: Number of DNA and protein sequence information to be processed
  by each computational task.
- `<RUN_ID>`: The workflow execution identification.

### Workflow Structure

The Epigenomics workflow structure depends on the _dataset_ (`<DATASET>`),
_number of sequence_ (`<NUM_SEQ>`) files used from the dataset, and the
_bin size_ (`<BIN_SIZE>`). In this implementation, the workflow is composed of
**branches** that represent each sequence file in the dataset
(i.e., `<NUM_SEQ>`). Each branch is defined as follows:

- For each branch, there is a single `fastqSplit` task.
- Each `fastqSplit` tasks generates a number of `filterContams`, `sol2sanger`,
  `fast2bfq`, and `map` tasks that form pipelines. The _number of pipelines_
  is defined by the number of lines in the dataset sequence file divided by
  the `<BIN_SIZE>`.
- Each branch has a single `mapMerge` task.

For the **entire workflow**:

- There is an additional single `mapMerge` task that combines the output data
  generated by `mapMerge` tasks from each branch.
- There is only one instance for `chr_21` and `pileup` tasks.