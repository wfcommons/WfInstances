<a href="https://wfcommons.org" target="_blank"><img src="https://wfcommons.org/images/wfcommons-horizontal.png" width="350" /></a>

<img src="https://pegasus.isi.edu/documentation/_static/pegasus_circular_white_logo.png" width="100"/>

# Execution Instances for the Montage Workflow

## Workflow Description

[Montage](http://montage.ipac.caltech.edu) is a toolkit for assembling Flexible
Image Transport System (FITS) images into custom mosaics. The test case implemented
as a [Pegasus workflow](https://github.com/pegasus-isi/montage-workflow-v2) aims to
re-project, background correct, and add astronomical images into custom mosaics.
This test case is composed of eight different tasks:

  1. `mProject` – reprojects a single image to the scale defined in an alternate
     FITS header template.
  2. `mDiffFit` – runs mDiff immediately followed by mFitplane, and checks the first
     to decide whether to run the second.
  3. `mConcatFit` – merges multiple plane fit parameter files (from mFitplane) into
     one file.
  4. `mBgModel` – a modelling/fitting program.
  5. `mBackground` – subtracts a planar background from a FITS image.
  6. `mImgtbl` – extracts the FITS header geometry information from a set of files
     and creates an ASCII image metadata table which is used by several of the other
     programs.
  7. `mAdd` – coadds the reprojected images in an input list to form an output
     mosaic with FITS header keywords specified in a header file.
  8. `mViewer` – command line application for visualizing FITS images, overlaying
     content (grids, symbols, etc.) on them and creating PNG or JPEG files.

The figure below shows an overview of the Montage workflow structure:

<img src="docs/images/montage.png?raw=true" width="600">

### Research Publication

Details of the Montage workflow description, computational jobs, and performance
metrics can be found in the following research publication:

- M. Rynge, G. Juve, J. Kinney, J. Good, B. G. Berriman, A. Merrihew, and
  E. Deelman, "Producing an Infrared Multiwavelength Galactic Plane Atlas
  using Montage, Pegasus and Amazon Web Services," in 23rd Annual Astronomical
  Data Analysis Software and Systems (ADASS) Conference, 2013.

## Execution Instances

Execution instances are formatted according to
[WfFormat](https://github.com/wfcommons/WfFormat) (version 1.6) for describing
workflow executions.

Instance files are named using the following convention:
`montage-<COMPUTE_PLATFORM>-<SURVEY>-<DEGREE>d-<RUN_ID>.json`, where:

- `<COMPUTE_PLATFORM>`: The compute platform where the actual Pegasus workflow was
  executed (`chameleon`).
- `<SURVEY>`: The data set and band to use for the mosaic (**2mass**: Two-Micron
  All-Sky Survey; **dss**: STScI Digitized Sky Survey).
- `<DEGREE>`: The size (in degrees) to be used for the width/height of the final
  mosaic, written without a decimal separator. The values used per survey are listed
  in increasing mosaic size in the table below.
- `<RUN_ID>`: The workflow execution identification.

The table below summarizes the parameter combinations available in this directory,
which include some of the largest workflows in this repository:

| `<SURVEY>` | `<DEGREE>` | Tasks | Files | Makespan |
| --- | --- | ---: | ---: | ---: |
| `2mass` | `005d` | 58 | 111 | 1,060 s |
| `2mass` | `01d` | 103 | 183 | 1,362 s |
| `2mass` | `015d` | 310 | 471 | 3,185 s |
| `2mass` | `02d` | 619 | 906 | 7,331 s |
| `2mass` | `025d` | 619 | 906 | 812 s |
| `2mass` | `03d` | 748 | 1,089 | 982 s |
| `2mass` | `04d` | 1,312 | 1,869 | 1,520 s |
| `2mass` | `05d` | 1,738 | 2,475 | 2,554 s |
| `2mass` | `10d` | 4,846 | 7,050 | 7,109 s |
| `2mass` | `15d` | 7,117 | 10,941 | 10,354 s |
| `2mass` | `20d` | 9,805 | 15,540 | 14,522 s |
| `dss` | `05d` | 58 | 111 | 870 s |
| `dss` | `075d` | 178 | 276 | 681 s |
| `dss` | `10d` | 472 | 633 | 2,172 s |
| `dss` | `125d` | 1,066 | 1,308 | 1,933 s |
| `dss` | `15d` | 2,122 | 2,463 | 6,197 s |
| `dss` | `20d` | 6,448 | 7,041 | 13,298 s |

### Workflow Structure

The Montage workflow structure depends on the _data set and band_ (`<SURVEY>`) used
for the mosaic and the _size (in degrees)_ (`<DEGREE>`) to be used for the
width/height of the final mosaic. In this implementation, the workflow has **3
bands** (red, blue, and green), where each band defines "**a branch**" of the
workflow. For each branch:

- The degree defines the number of tasks in a branch. The number of `mProject` and
  `mBackground` tasks are the same.
- An `mDiffFit` task is generated from pairs of `mProject` tasks. The number of
  `mDiffFit` tasks depends on the number of overlapped tiles.
- Each branch has only one instance of the `mConcatFit`, `mBgModel`, `mImgtbl`,
  `mAdd`, and `mViewer` tasks, regardless of the workflow degree.

An additional `mViewer` task at the bottom of the workflow combines all 3 bands to
create a colored JPEG.
