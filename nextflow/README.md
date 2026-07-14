<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://nextflow.io/img/nextflow2014_no-bg.png" width="180"/>

# Nextflow Execution Instances

This directory contains workflow execution instances generated from
[Nextflow](https://nextflow.io) executions. The instances hosted in 
this directory use [WfFormat](https://github.com/wfcommons/wfformat)
for describing workflow executions.

### Workflow Applications

The workflow execution instances recorded in this directory are from
open-source applications hosted at the [nf-co.re](https://nf-co.re)
repository.


### Provenance

The instances in the `not-from-ro-crate` directory were obtained circa 2023 using a now-defunct Nextflow log parser for executions conducted with a patched version of Nextflow v23.04.1. 

The instanced in the `from-ro-crate` directory were obtained with the current Nextflow log parser implementation in WfCommons, which relies on the Nextflow-generated trace file and the RO-Crate data produced by the `nf-prov` Nextflow plugin. 

In both the above, it is likely that non-file-based inter-task dependencies are not captured by the workflow instances.


### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that implements
[WfFormat](https://github.com/wfcommons/wfformat).
