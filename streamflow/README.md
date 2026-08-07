<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://streamflow.di.unito.it/wp-content/uploads/2020/07/streamflow_logo_name_tag_270x90.png" width="200"/>

# StreamFlow/RO-Crate Execution Instances

This directory contains workflow execution instances generated from
[StreamFlow](https://streamflow.di.unito.it/) executions. The instances hosted in
this directory use [WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6)
for describing workflow executions.

### Workflow Applications

| Application | Instance files |
| --- | --- |
| [1000Genome (CWL)](https://github.com/alpha-unito/cwl-1000genome-workflow) | `1000genome-streamflow-<RUN_ID>.json` |

The 1000Genome workflow identifies mutational overlaps using data from the
[1000 Genomes Project](https://www.internationalgenome.org). This CWL implementation
is functionally equivalent to the
[Pegasus implementation](../pegasus/1000genome), which is a useful basis for
cross-runtime-system comparisons. Task names in the instance are CWL step
identifiers (e.g., `main.cwl#chromosome/run/individuals`) and cover
`get_chromosome`, `get_intervals`, `individuals`, `individuals_merge`, `sifting`,
`mutation_overlap`, and `frequency`.

### Provenance

Instances were obtained with the RO-Crate parser of the
[WfCommons Python package](https://github.com/wfcommons/wfcommons), applied to the
[Workflow Run RO-Crate](https://w3id.org/workflowhub/workflow-ro-crate/1.0) produced
by StreamFlow (recorded as runtime system `Streamflow-ROCrate` v1.5-dev). Because
provenance is reconstructed from the RO-Crate, per-machine information is not
recorded in these instances.

### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that implements
[WfFormat](https://github.com/wfcommons/WfFormat).
