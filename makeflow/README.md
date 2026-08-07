<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://raw.githubusercontent.com/cooperative-computing-lab/cctools/master/doc/manuals/logos/makeflow-logo.png" width="160" />

# Makeflow Workflow Execution Instances

This directory contains workflow execution instances generated from
[Makeflow](https://ccl.cse.nd.edu/software/makeflow/) workflow executions. The
instances hosted in this directory use
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

### Directory Structure

Each sub-directory represents a _workflow application_ and contains:

- a `README.md` describing the workflow, its tasks, its structure, and the naming
  convention of the instance files;
- a `docs/images/` directory with a figure of the workflow structure;
- one JSON file per execution instance, whose name encodes the computing platform
  and the execution parameters.

### Provenance

Instances were obtained by parsing Makeflow execution logs with the Makeflow log
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
| [BLAST](./blast) | Bioinformatics | Compute-intensive | Chameleon |
| [BWA](./bwa) | Bioinformatics | Data-intensive | Chameleon |

Both applications come from the
[makeflow-examples](https://github.com/cooperative-computing-lab/makeflow-examples)
repository, and each was executed in three configurations (`small`, `medium`, and
`large`), repeated several times.
