<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://nextflow.io/img/nextflow2014_no-bg.png" width="180"/>

# Legacy Nextflow Execution Instances

This directory contains one execution instance per open-source pipeline hosted at
the [nf-co.re](https://nf-co.re) repository. The workflows were executed in March
2023 on the `dirt02` machine with a patched version of Nextflow v23.04.1, and the
instances were obtained with a now-defunct Nextflow log parser — hence the `legacy`
name. Newer instances, produced with the current RO-Crate-based parser, are in the
[`ro-crate`](../ro-crate) directory.

Instance files are named `<APPLICATION>-<COMPUTE_PLATFORM>-<RUN_ID>.json`.

> **Caveat:** as with all instances in the [`nextflow`](..) directory, it is likely
> that non-file-based inter-task dependencies are not captured.

### Workflow Instances

| Application | Description | Tasks | Files | Makespan |
| --- | --- | ---: | ---: | ---: |
| [airrflow](https://nf-co.re/airrflow) | B-cell and T-cell repertoire (AIRR) sequencing analysis | 212 | 935 | 4,706 s |
| [atacseq](https://nf-co.re/atacseq) | ATAC-seq chromatin accessibility analysis | 265 | 775 | 8,549 s |
| [bacass](https://nf-co.re/bacass) | Bacterial assembly and annotation | 11 | 67 | 4,243 s |
| [chipseq](https://nf-co.re/chipseq) | ChIP-seq peak calling | 210 | 649 | 5,689 s |
| [cutandrun](https://nf-co.re/cutandrun) | CUT&RUN and CUT&Tag chromatin profiling | 120 | 309 | 1,544 s |
| [fetchngs](https://nf-co.re/fetchngs) | Fetching raw sequencing data from public databases | 43 | 103 | 246 s |
| [hic](https://nf-co.re/hic) | Hi-C chromosome conformation analysis | 38 | 121 | 1,507 s |
| [mag](https://nf-co.re/mag) | Metagenome assembly and binning | 157 | 889 | 4,104 s |
| [methylseq](https://nf-co.re/methylseq) | Bisulfite sequencing (methylation) analysis | 36 | 132 | 528 s |
| [rnaseq](https://nf-co.re/rnaseq) | RNA sequencing analysis | 197 | 680 | 3,131 s |
| [sarek](https://nf-co.re/sarek) | Germline and somatic variant calling | 26 | 82 | 518 s |
| [scrnaseq](https://nf-co.re/scrnaseq) | Single-cell RNA sequencing analysis | 14 | 70 | 2,126 s |
| [smrnaseq](https://nf-co.re/smrnaseq) | Small RNA sequencing analysis | 197 | 608 | 9,404 s |
| [taxprofiler](https://nf-co.re/taxprofiler) | Taxonomic profiling of shotgun metagenomes | 127 | 362 | 3,731 s |
| [viralrecon](https://nf-co.re/viralrecon) | Viral genome assembly and variant calling | 203 | 877 | 4,309 s |
