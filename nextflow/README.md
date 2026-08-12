<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://nextflow.io/img/nextflow2014_no-bg.png" width="180"/>

# Nextflow Workflow Execution Instances

This directory contains workflow execution instances generated from
[Nextflow](https://nextflow.io) executions. The instances hosted in this directory
use [WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

### Workflow Applications

All instances are executions of open-source pipelines hosted at the
[nf-co.re](https://nf-co.re) repository.

| Directory | Content |
| --- | --- |
| [`ro-crate/`](./ro-crate) | RNA-Seq runs plus the Sarek germline and somatic campaigns |
| [`legacy/`](./legacy) | One instance per nf-core pipeline, from a 2023 execution campaign |

### Provenance

The instances in the [`ro-crate`](./ro-crate) directory were obtained with the
current Nextflow log parser implementation in
[WfCommons](https://github.com/wfcommons/wfcommons), which relies on the
Nextflow-generated trace file and on the RO-Crate data produced by the
[`nf-prov`](https://github.com/nextflow-io/nf-prov) Nextflow plugin. They were
executed with Nextflow 26.04.4 on the `disco` cluster.

The instances in the [`legacy`](./legacy) directory were obtained circa 2023 using a
now-defunct Nextflow log parser, for executions conducted with a patched version of
Nextflow v23.04.1 on the `dirt02` machine.

In both cases, it is likely that non-file-based inter-task dependencies are not
captured by the workflow instances.

### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that implements
[WfFormat](https://github.com/wfcommons/WfFormat).
