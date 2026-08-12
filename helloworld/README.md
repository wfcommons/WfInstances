<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

# Sample "hello world!" Workflow Execution Instances

This directory contains small, made-up workflow execution instances for **testing
purposes**, described using [WfFormat](https://github.com/wfcommons/WfFormat)
(version 1.6). They have been constructed from real executions of purely synthetic
benchmark workflows run with [Pegasus](http://pegasus.isi.edu) 5.0, and are useful
as minimal fixtures for tools that consume WfFormat.

These instances are *not* representative of any scientific application — see the
other directories of this repository for production workflow executions.

#### Workflow Instances

| Instance | Structure | Tasks | Files | Makespan |
| --- | --- | ---: | ---: | ---: |
| `helloworld-chain-5-chameleon.json` | linear chain | 5 | 6 | 661 s |
| `helloworld-forkjoin-10-chameleon.json` | fork-join | 10 | 11 | 437 s |

All tasks are synthetic CPU-bound kernels (`cpuhog_chain_*` and
`cpuhog_forkjoin_*`), so the recorded runtimes reflect pure compute with negligible
I/O.

#### Workflow Simulator

The execution instances provided in this directory are compatible with any
[simulation framework](https://wfcommons.org/simulation) that implements
[WfFormat](https://github.com/wfcommons/WfFormat).
