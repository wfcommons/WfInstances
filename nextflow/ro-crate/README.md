<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350"/></a>

<img src="https://nextflow.io/img/nextflow2014_no-bg.png" width="180"/>

# RO-Crate-based Nextflow Execution Instances

This directory contains execution instances of open-source pipelines hosted at the
[nf-co.re](https://nf-co.re) repository, obtained with the current Nextflow log
parser of [WfCommons](https://github.com/wfcommons/wfcommons). The parser relies on
the Nextflow-generated trace file together with the RO-Crate data produced by the
[`nf-prov`](https://github.com/nextflow-io/nf-prov) plugin.

All executions were performed with Nextflow 26.04.x on the `disco` cluster.

| Content | Application |
| --- | --- |
| [`sarek_germline/`](./sarek_germline) | [sarek](https://nf-co.re/sarek) — germline variant calling |
| [`sarek_somatic/`](./sarek_somatic) | [sarek](https://nf-co.re/sarek) — somatic variant calling |
| `rnaseq-*.json` | [rnaseq](https://nf-co.re/rnaseq), e.g. on the GSE110004 dataset |

> **Caveat:** as with all instances in the [`nextflow`](..) directory, it is likely
> that non-file-based inter-task dependencies are not captured.

## Sarek Campaigns

The Sarek instances come from two systematic campaigns. Files are named
`sarek_<ANALYSIS>_w<GROUP>_t<CONFIG>.json`, where:

- `<ANALYSIS>`: `germline` or `somatic` variant-calling analysis.
- `w<GROUP>`: run group — `w1`–`w5` for germline, `w1`–`w3` for somatic. Instances
  that share a `<CONFIG>` index have **identical structure** across run groups and
  differ only in their measured performance; makespans grow monotonically from `w1`
  to the last group.
- `t<CONFIG>`: configuration index, `t01`–`t10`, with the workflow size increasing
  with the index.

This makes the campaigns well suited to studying performance variability at a fixed
workflow structure (vary `w`, fix `t`) or scalability across workflow sizes
(fix `w`, vary `t`).

### Germline campaign

| Config | Tasks | Makespan `w1` → `w5` |
| --- | ---: | --- |
| `t01` | 344 | 4,278 – 9,986 s |
| `t02` | 396 | 4,386 – 10,167 s |
| `t03` | 428 | 4,535 – 10,503 s |
| `t04` | 480 | 4,492 – 10,615 s |
| `t05` | 516 | 4,616 – 10,456 s |
| `t06` | 556 | 4,688 – 10,511 s |
| `t07` | 612 | 4,868 – 10,634 s |
| `t08` | 668 | 4,874 – 10,674 s |
| `t09` | 740 | 4,951 – 10,842 s |
| `t10` | 772 | 4,976 – 10,978 s |

### Somatic campaign

| Config | Tasks | Makespan `w1` → `w3` |
| --- | ---: | --- |
| `t01` | 164 | 8,679 – 22,121 s |
| `t02` | 354 | 8,755 – 23,183 s |
| `t03` | 624 | 10,036 – 24,941 s |
| `t04` | 844 | 10,396 – 24,881 s |
| `t05` | 1,144 | 11,437 – 25,955 s |
| `t06` | 1,364 | 12,349 – 26,898 s |
| `t07` | 1,764 | 13,758 – 28,218 s |
| `t08` | 2,024 | 14,803 – 29,760 s |
| `t09` | 2,184 | 15,821 – 31,421 s |
| `t10` | 2,324 | 16,422 – 31,491 s |
