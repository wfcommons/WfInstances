<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Snakemake_logo_dark.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail_unscaled&_=20220226072335" width="180"/>

# Snakemake Workflow Execution Instances

This directory contains workflow execution instances generated from
[Snakemake](https://snakemake.readthedocs.io/en/stable/) executions. The instances
hosted in this directory use [WfFormat](https://github.com/wfcommons/WfFormat)
(version 1.6) for describing workflow executions.

### Workflow Applications

| Directory | Application | Science Domain | Platform |
| --- | --- | --- | --- |
| [`RASflow/`](./RASflow) | [RASflow](https://github.com/zhxiaokang/RASflow) — RNA-Seq analysis | Bioinformatics | `dirt02` |
| [`rna-seq-star-deseq2/`](./rna-seq-star-deseq2) | [rna-seq-star-deseq2](https://github.com/snakemake-workflows/rna-seq-star-deseq2) — RNA-Seq with STAR and DESeq2 | Bioinformatics | `disco` |
| [`varlociraptor/`](./varlociraptor) | [dna-seq-varlociraptor](https://github.com/snakemake-workflows/dna-seq-varlociraptor) — variant calling | Bioinformatics | `disco` |

### Instance Naming Conventions

Each application encodes its execution parameters in the instance file name:

- **RASflow** — `RASflow-snakemake-n<NUM_TASKS>.json`, where `<NUM_TASKS>` is the
  number of tasks in the executed workflow (11, 19, 31, 51, 101, 201, and 501).
- **rna-seq-star-deseq2** —
  `rna-seq-star-deseq2_<N>sample_<trim|notrim>_<pca|nopca>_<N>contrast_<MODEL>.json`,
  where `<N>sample` is the number of input samples (4 to 24), `trim`/`notrim`
  indicates whether read trimming was enabled, `pca`/`nopca` whether the PCA report
  was produced, `<N>contrast` the number of differential-expression contrasts, and
  `<MODEL>` the DESeq2 model used (`default` or `additive`).
- **varlociraptor** — `varlociraptor_<PLATFORM>_<N>pct_<N>scatter.json`, where
  `<PLATFORM>` is the machine on which the workflow was executed, `<N>pct` the
  percentage of the input dataset processed, and `<N>scatter` the number of scatter
  units the calling step was split into (2 to 96). The number of scatter units drives
  the width of the workflow, and hence its task count.

### Provenance

Instances were obtained with the Snakemake log parser of the
[WfCommons Python package](https://github.com/wfcommons/wfcommons), applied to the
execution metadata and logs produced by Snakemake 9.20.0.

### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that implements
[WfFormat](https://github.com/wfcommons/WfFormat).
