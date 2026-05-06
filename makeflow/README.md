<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="http://ccl.cse.nd.edu/software/makeflow/MakeflowLogoSmall.png" width=160 />

# Makeflow Workflow Execution Instances

This directory contains workflow execution instances generated from
[Makeflow](http://ccl.cse.nd.edu/software/makeflow/) workflow
executions. The instances hosted in this directory use the
[WfCommons JSON format](https://github.com/wfcommons/workflow-schema)
for describing workflow executions.

#### Repository Structure

Workflow execution instances are organized into sub-directories within this
directory. Each sub-directory represents a _workflow application_, which
itself contains sub-directory for workflow executions in different
_computing platforms_.

#### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that
implements the
[WfCommons JSON format](https://github.com/wfcommons/workflow-schema).

## Summary of Workflow Execution Instances

| Application | Science Domain | Category | Computing Platforms | # Execution Instances |
| --- | --- | --- | --- | --- |
| BLAST | Bioinformatics | Compute-intensive | 1 | 15 |
| BWA | Bioinformatics | Data-intensive | 1 | 15 |
