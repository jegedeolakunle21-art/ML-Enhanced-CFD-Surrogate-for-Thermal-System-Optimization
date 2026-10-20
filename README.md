# ML-Enhanced-CFD-Surrogate-for-Thermal-System-Optimization
CFD-ML ENHANCED FOR COUNTER FLOW HEAT EXCHANGER SYSTEM
# ML-Enhanced CFD Surrogate for Heat Exchanger Optimization

## Project Overview

This project develops a machine-learning-enhanced Computational Fluid Dynamics (CFD) surrogate model to predict and optimize the thermal-hydraulic performance of a heated circular-tube system. It combines engineering correlations, synthetic data generation, machine learning, constrained optimization, and a planned CFD validation workflow using SimScale.

The primary objective is to maximize heat-transfer rate while satisfying pressure-drop and outlet-temperature constraints. The project explores how machine learning can reduce the computational cost of evaluating candidate thermal-system designs.

**Project status:** Phases 1–4 executed; Phase 5 CFD validation is in progress and has not yet been completed.

## Objectives

- Generate a physically consistent synthetic heat-exchanger dataset.
- Train and evaluate machine-learning surrogate models.
- Predict pressure drop, outlet temperature, Nusselt number, and heat-transfer coefficient.
- Optimize heat-transfer rate subject to engineering constraints.
- Compare surrogate predictions against analytical correlations.
- Validate the optimized design using CFD simulations in SimScale.

## System Description

The initial system is a straight circular tube carrying turbulent water flow with a prescribed uniform wall heat flux.

The initial model assumes steady-state, single-phase flow, approximately constant fluid properties, negligible heat loss, and simplified thermal-hydraulic correlations.

## Engineering Formulation

The Reynolds number is defined as:

\[
Re=\frac{4\dot{m}}{\pi D\mu}
\]

The Dittus–Boelter correlation estimates the Nusselt number:

\[
Nu=0.023Re^{0.8}Pr^{0.4}
\]

The convective heat-transfer coefficient is:

\[
h=\frac{Nu\,k}{D}
\]

The imposed wall heat-transfer rate is:

\[
Q=q''_w\pi DL
\]

The Darcy–Weisbach equation estimates pressure drop:

\[
\Delta P=f\frac{L}{D}\frac{\rho u^2}{2}
\]

These relations support the initial dataset and analytical consistency checks. Their applicability depends on the flow regime, geometry, boundary conditions, and fluid-property assumptions.

## Machine-Learning Workflow

Five input variables are used:

- Mass flow rate
- Inlet temperature
- Wall heat flux
- Tube diameter
- Tube length

The model predicts four targets:

- Pressure drop
- Outlet temperature
- Nusselt number
- Heat-transfer coefficient

The candidate algorithms include Linear Regression, Random Forest, XGBoost, and a Multilayer Perceptron neural network.

Model evaluation includes mean absolute error (MAE), root mean squared error (RMSE), coefficient of determination (\(R^2\)), cross-validation RMSE, and inference time. The best model for each target is selected using training-fold cross-validation rather than test-set performance.

## Optimization Strategy

A constrained optimization procedure searches the design space to maximize heat-transfer rate.

The prototype constraints are:

- Pressure drop no greater than 60,000 Pa.
- Outlet temperature no greater than 60°C.

The optimizer uses surrogate predictions to assess constraint feasibility, while heat-transfer rate is calculated from the imposed wall heat flux and tube geometry.

These limits are illustrative project assumptions and must be reviewed against the requirements of a real system before engineering application.

## Project Phases

| Phase | Description | Status |
|---|---|---|
| 1 | Engineering formulation and governing equations | Completed |
| 2 | Synthetic dataset generation and consistency checks | Completed |
| 3 | Surrogate training and model evaluation | Executed; numerical metrics to be documented |
| 4 | Constrained thermal-system optimization | Executed; optimal-design results to be documented |
| 5 | CFD validation using SimScale | In progress; no validated CFD results yet |

## CFD Validation Plan

The next stage uses SimScale to simulate the baseline and optimized tube designs under consistent conditions.

The validation procedure will include:

1. Reconstructing the geometry from the selected design variables.
2. Assigning water properties and the appropriate turbulent-flow and thermal models.
3. Applying consistent inlet, outlet, and heated-wall boundary conditions.
4. Checking mesh quality and mesh independence.
5. Monitoring residual convergence and mass and energy conservation.
6. Comparing pressure drop, outlet temperature, heat-transfer rate, Nusselt number, and heat-transfer coefficient.
7. Evaluating surrogate prediction errors against completed CFD results.

CFD results will be reported only after simulations have actually completed and the relevant quality checks have passed.

## Data and Reproducibility

The initial dataset is synthetic and generated using analytical engineering correlations. It is not measured experimental data or genuine CFD output.

The project is organized around the following expected artifacts:

```text
ml-cfd-thermal-optimization/
├── README.md
├── synthetic_heat_exchanger_dataset.csv
├── dataset_metadata.json
├── models/
│   └── best_surrogate_models.joblib
├── phase3_results/
│   ├── cross_validation_results.csv
│   ├── test_metrics_all_models.csv
│   └── best_model_test_predictions.csv
├── phase4_results/
│   ├── optimal_design_candidate.csv
│   └── optimization_metadata.json
└── phase5_openfoam_or_simscale/
    └── phase5_validation_results.csv
```

The structure describes the intended repository organization. Include only files that have actually been generated and verified in the published repository.

## Limitations

- Synthetic data cannot establish agreement with real experimental or CFD results.
- The initial correlations have limited applicability outside their assumed operating regime.
- Constant fluid properties may not capture significant temperature-dependent effects.
- Surrogate predictions near optimization constraints require independent verification.
- CFD validation remains outstanding.

## Future Improvements

- Complete SimScale CFD simulations for baseline and optimized designs.
- Perform mesh-independence and conservation checks.
- Compare multiple turbulence models where appropriate.
- Investigate temperature-dependent fluid properties.
- Expand the dataset using validated CFD simulations.
- Retrain the surrogate on CFD-generated data and quantify prediction errors.
- Develop a Streamlit application for interactive prediction and optimization.

## Technologies

Python, NumPy, pandas, scikit-learn, XGBoost, SciPy, joblib, Google Colab, Streamlit, and SimScale.

## Conclusion

This project establishes a machine-learning workflow for surrogate-assisted thermal-system optimization. Its current contribution is the development and execution of a synthetic-data-based modelling and optimization pipeline. Independent CFD validation is the next major milestone required to assess whether the predicted design improvements transfer to a higher-fidelity numerical simulation.

**Research integrity statement:** Synthetic, analytical, machine-learning, and CFD results are distinct evidence types and will be labelled separately throughout this project.

