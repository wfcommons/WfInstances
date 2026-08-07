<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://pegasus.isi.edu/documentation/_static/pegasus_circular_white_logo.png" width="100"/>

# Pegasus Workflow Execution Instances

This directory contains workflow execution instances generated from
[Pegasus](http://pegasus.isi.edu) workflow executions. The instances hosted in this
directory use [WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for
describing workflow executions.

### Directory Structure

Each sub-directory represents a _workflow application_ and contains:

- a `README.md` describing the workflow, its tasks, its structure, and the naming
  convention of the instance files;
- a `docs/images/` directory with a figure of the workflow structure;
- one JSON file per execution instance, whose name encodes the computing platform
  and the execution parameters that determine the size and shape of the workflow.

### Provenance

Instances were obtained by parsing Pegasus execution logs with the Pegasus log
parser of the [WfCommons Python package](https://github.com/wfcommons/wfcommons).
All executions in this directory were performed on the
[Chameleon](https://www.chameleoncloud.org) cloud testbed.

### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that implements
[WfFormat](https://github.com/wfcommons/WfFormat).

## Summary of Workflow Execution Instances

| Application | Science Domain | Category | Platform |
| --- | --- | --- | --- |
| [1000Genome](./1000genome) | Bioinformatics | Data-intensive | Chameleon |
| [Cycles](./cycles) | Agroecosystem | Compute-intensive | Chameleon |
| [Epigenomics](./epigenomics) | Bioinformatics | Data-intensive | Chameleon |
| [Montage](./montage) | Astronomy | Compute-intensive | Chameleon |
| [Seismic Cross Correlation](./seismology) | Seismology | Data-intensive | Chameleon |
| [SoyKB](./soykb) | Bioinformatics | Data-intensive | Chameleon |
| [SRA Search](./srasearch) | Bioinformatics | Data-intensive | Chameleon |

Purely synthetic Pegasus executions used for testing are kept separately, in the
[`helloworld`](../helloworld) directory.
