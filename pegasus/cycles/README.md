<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://pegasus.isi.edu/documentation/_static/pegasus_circular_white_logo.png" width="100"/>

# Execution Instances for the Cycles Workflow

## Workflow Description

Cycles is a user-friendly, multi-crop, multi-year, process-based agroecosystem model
with daily time step simulations of crop production and the water, carbon (C) and
nitrogen (N) cycles in the soil-plant-atmosphere continuum. The model can simulate
perturbations of biogeochemical processes caused by agronomic practices such as
tillage, irrigation, organic and inorganic nutrient applications, annual and
perennial crops selection, grain and forage harvest, poly-cultures, relay cropping
and grazing. Cycles allows unlimited crop species to be specified by the user. The
workflow is composed of seven different tasks:

  1. `baseline_cycles`: computes the model reference or baseline.
  2. `fertilizer_increase_cycles`: Cycles execution with increased fertilizer rate
     of 10% – key to forecasting the economic impact of grain yields.
  3. `cycles`: Cycles execution.
  4. `cycles_output_summary`: aggregates and summarizes all outputs for a single
     crop.
  5. `cycles_fertilizer_increase_output_parser`: parses the outputs of the
     increased-fertilizer executions.
  6. `cycles_fertilizer_increase_output_summary`: aggregates and summarizes all
     increased-fertilizer outputs for a single crop.
  7. `cycles_plots`: ensembles all summaries and produces visualization outputs.

The figure below shows an overview of the Cycles workflow structure:

<img src="docs/images/cycles.png?raw=true" width="750">

### Research Publication

Details of the Cycles workflow description, computational jobs, and performance
metrics can be found in the following research publication:

- Ferreira da Silva, R., Mayani, R., Shi, Y., Kemanian, A. R., Rynge, M., &
  Deelman, E. (2019). "Empowering Agroecosystem Modeling with HTC Scientific
  Workflows: The Cycles Model Use Case". In First International Workshop on
  Big Data Tools, Methods, and Use Cases for Innovative Scientific Discovery
  (BTSD) (pp. 4545–4552). https://doi.org/10.1109/BigData47090.2019.9006107

## Execution Instances

Execution instances are formatted according to
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

Instance files are named using the following convention:
`cycles-<COMPUTE_PLATFORM>-<LOCATIONS>l-<CROPS>c-<PARAMS>p-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Pegasus workflow was
  executed (`chameleon`).
- `<LOCATIONS>`: The number of points of the spatial grid cell (1, 2, 5, or 10).
- `<CROPS>`: Number of crops being evaluated (1, 2, or 3).
- `<PARAMS>`: Number of parameter values from the simulation matrix (9 or 12).
- `<RUN_ID>`: The workflow execution identification.

The table below summarizes the parameter combinations available in this directory.
Cycles produces by far the largest data footprints in this repository (over 50,000
files for a single execution):

| Locations | Crops | Tasks (`9p`) | Files (`9p`) | Tasks (`12p`) | Files (`12p`) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 67 | 522 | 219 | 1,738 |
| 1 | 2 | 134 | 1,037 | 438 | 3,469 |
| 1 | 3 | 201 | 1,552 | 657 | 5,200 |
| 2 | 1 | 133 | 1,037 | 437 | 3,469 |
| 2 | 2 | 266 | 2,066 | 874 | 6,930 |
| 2 | 3 | 399 | 3,095 | 1,311 | 10,391 |
| 5 | 1 | 331 | 2,582 | 1,091 | 8,662 |
| 5 | 2 | 662 | 5,153 | 2,182 | 17,313 |
| 5 | 3 | 993 | 7,724 | 3,273 | 25,964 |
| 10 | 1 | 661 | 5,157 | 2,181 | 17,317 |
| 10 | 2 | 1,322 | 10,298 | 4,362 | 34,618 |
| 10 | 3 | 1,983 | 15,439 | 6,543 | 51,919 |

### Workflow Structure

The Cycles workflow structure depends on the _number of points_ (`<LOCATIONS>`),
_number of crops_ (`<CROPS>`), and the _number of parameter values_ (`<PARAMS>`). In
this implementation, the workflow is composed of **branches** that represent each
point of the spatial grid. For each branch:

- The number of tasks is first steered by the number of different crops being
  evaluated.
- For each **tuple** of `(point, crop)`, a number of product combinations defined by
  the number of parameters generates workflow segments of `baseline_cycles`,
  `fertilizer_increase_cycles`, `cycles`, and
  `cycles_fertilizer_increase_output_parser` tasks — these four task types always
  appear in equal numbers (16 of each per tuple for `9p`, and 54 for `12p` in these
  executions).
- For each **tuple** of `(point, crop)`, there is one `cycles_output_summary` and
  one `cycles_fertilizer_increase_output_summary` task.
- There is a `cycles_plots` task for each crop type in the workflow — e.g., if the
  workflow evaluates two crops, then there will be 2 tasks of that type.
