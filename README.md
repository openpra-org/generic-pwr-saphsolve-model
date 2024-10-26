<!-- TOC -->
* [Generic SAPHSOLVE Models](#generic-saphsolve-models)
  * [1. SAPHSOLVE Model Format](#1-saphsolve-model-format)
  * [2. About Generic PWR v1.2 Model](#2-about-generic-pwr-v12-model)
  * [3. Export Models in JSON Format](#3-export-models-in-json-format)
  * [4. Usage](#4-usage)
  * [5. Additional References Related to Synthetic Models](#5-additional-references-related-to-synthetic-models)
<!-- TOC -->

# Generic SAPHSOLVE Models

This repository includes generic PWR v1.2 model in SAPHSOLVE JSON format. The goals of including these models are to:

- Serve as test cases for various PRA tools, including [Open-PRA](https://github.com/openpra-org/openpra-monorepo).
- Familiarize users with different modeling approaches and formats.
- Provide a reference for PRA model exchange.
- And more.

The repository also maintains a `schema` for the models to give users valuable insights.


## 1. SAPHSOLVE Model Format
SAPHSOLVE is the quantification engine of legacy PRA tool SAPHIRE. SAPHSOLVE input and output format are detailed in a [report](https://www.osti.gov/biblio/2203095) published by Idaho National Laboratory.

## 2. About Generic PWR v1.2 Model
Since 1995, Idaho National Laboratory (INL) has developed Standardized Plant Analysis Risk (SPAR) models for the United States (US) Nuclear Regulatory Commission (NRC) to provide critical risk-informed input to the regulatory process.

The generic PWR model is available as a SAPHIRE model, accompanied by a report detailing the foundations of the modeling phenomena and referencing failure data. The current version of the SAPHIRE model is `v1.2`; however, the documented model information corresponds to `v1.0`. This model is continuously evolving, with researchers and PRA practitioners actively working to improve it. 

At present, the model considers various initiating events, including seismic activity, internal flooding, internal fires, hurricanes, high winds, ISLOCA (Interfacing Systems LOCA), upset conditions leading to transients, large break LOCA, loss of CCW (Component Cooling Water), loss of DC bus, loss of feedwater, loss of offsite power, large steam line breaks, medium break LOCA, steam generator tube ruptures, small LOCA, tornadoes, and excessive LOCA.
`v1.0` of the model includes 56 event trees linked with 140 fault trees.

## 3. Export Models in JSON Format
Users should have the latest version of `SAPHIRE`. They should define `SAPHSOLVE` as an external solver within `SAPHIRE` and ensure that the defined external solver is used when solving models. 

It is recommended that users refer to the `SAPHIRE` manual or contact the `SAPHIRE` development team at INL for any inquiries.


## 4. Usage
This model can be used to test quantification engines. Additionally, they enable the creation of a verification platform between quantification engines, allowing developers or practitioners to cross-check their results. Moreover, these models serve as a foundation for benchmarking efforts for any quantification tool.


## 5. Additional References Related to Synthetic Models

- E. M. Aras, A. S. Amin Aly Farag, S. T. Wood, and J. T. Boyce, “Refining Processing Engines from SAPHIRE: Initialization of Fault Tree/Event Tree Solver,” Idaho National Laboratory (INL), Idaho Falls, ID (United States), INL/RPT-23-75066-Rev000, Oct. 2023. doi: 10.2172/2203095.
- C. Smith, “Generic Pressurized Water Reactor Model for SAPHIRE,” INL/EXT-21-62553-Rev000, 1804754, Apr. 2021. doi: 10.2172/1804754.
- S. Wood, J. Boyce, E. Aras, A. Farag, and M. Diaconeasa, “Advancing SAPHIRE: Transitioning from Legacy to State-of-Art Excellence,” in Advanced Reactor Safety (ARS), Las Vegas, NV: American Nuclear Society, 2024, pp. 532–541. doi: 10.13182/T130-43357.
- E. Aras, S. Wood, J. Boyce, A. Farag, and M. Diaconeasa, “Enhancing the SAPHIRE Solve Engine: Initial Progress and Efforts,” in Advanced Reactor Safety (ARS), Las Vegas, NV: American Nuclear Society, 2024, pp. 542–551. doi: 10.13182/T130-43361.
- E. M. Aras, “Enhancement Methodology for Probabilistic Risk Assessment Tools through Diagnostics, Optimization, and Parallel Computing,” Doctor of Philosophy, North Carolina State University, Raleigh, North Carolina, 2024. [Online]. Available: https://repository.lib.ncsu.edu/items/bb05f7f5-1cff-4beb-9312-331bc94b0b95
- A. Farag, S. Wood, A. Earthperson, E. Aras, J. Boyce, and M. Diaconeasa, “Evaluating PRA Tools for Accurate and Efficient Quantifications: A Follow-Up Benchmarking Study Including FTREX,” in Advanced Reactor Safety (ARS), Las Vegas, NV: American Nuclear Society, 2024, pp. 573–582. doi: 10.13182/T130-43377.
- E. M. Aras, S. T. Wood, A. S. A. A. Farag, and J. T. Boyce, “Diagnostics and Strategic Plan for Advancing the SAPHIRE Engine,” Idaho National Laboratory, Idaho Falls, ID, INL/COM-23-74428, Aug. 2023. [Online]. Available: https://inldigitallibrary.inl.gov/sites/sti/sti/Sort_67446.pdf
- M. Hamza, A. Tezbasaran, E. Aras, A. S. Farag, and M. A. Diaconeasa, “Model Exchange Methodology Between Probabilistic Risk Assessment Tools: SAPHIRE and CAFTA Case Study,” in 18th International Probabilistic Safety Assessment and Analysis (PSA 2023), Knoxville, TN: American Nuclear Society, 2023, pp. 150–158.




