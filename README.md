# Resistance-based cable temperature estimation from two-end phasor measurements

**BSc Thesis** | Mittuniversitetet (Mid Sweden University), 2026  
Author: Sævar Ingi Sveinsson

## Overview

This repository contains code and generated outputs for a BSc thesis on **resistance-based temperature estimation** using synchronized voltage and current measurements at both ends of a power cable or transmission line.

### Research Questions

- How can temperature information be extracted from synchronized phasor measurements?
- How well do forward models predict the electrical temperature signal magnitude?
- How do three backward methods (Singh, SI/Z-drop, Power) behave on real two-end data?
- How sensitive are the methods to small magnitude and angle deviations?
- What measurement requirements are needed for practical deployment?

## Repository Structure

```
SIS/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
├── TEST_REGISTER.md                   # Test and notebook register
│
├── src/                               # Reusable Python modules
│   ├── __init__.py
│   ├── data_loader.py                # Load and synchronize phasor data
│   ├── forward_model.py              # Forward model implementations
│   ├── backward_methods.py           # Singh, SI, Power methods
│   ├── sensitivity.py                # Sensitivity sweep functions
│   └── utils.py                      # Helper functions
│
├── notebooks/                         # Final analysis notebooks (run in order)
│   ├── 01_data_preprocessing.ipynb   # Load, sync, validate raw data
│   ├── 02_forward_model.ipynb        # Forward model predictions
│   ├── 03_backward_methods.ipynb     # Backward method comparisons
│   ├── 04_sensitivity_analysis.ipynb # Measurement sensitivity tests
│   ├── 05_plot_generation.ipynb      # Generate thesis figures and tables
│   │
│   └── diagnostics/                  # Supporting diagnostic notebooks
│       ├── T8_Singh_diagnostics.ipynb
│       ├── T9_Singh_corrected_B_diagnostics.ipynb
│       └── README.md
│
├── data/                              # Data folder
│   └── README.md                      # Data availability notice
│
├── results/                           # Output folder for thesis figures/tables
│   ├── final_figures/                # Figures used in report/presentation
│   ├── final_tables/                 # Summary result tables
│   └── appendix_outputs/             # Extended output tables/figures
│
└── archive_old_tests/                # Older exploratory notebooks (not final results)
    ├── old_forward_tests/
    ├── old_zdrop_tests/
    ├── old_singh_tests/
    ├── old_sensitivity_tests/
    └── exploratory_tests/
```

## Recommended Run Order

Execute the final notebooks in this sequence:

1. **`notebooks/01_data_preprocessing.ipynb`**
   - Load measurement data from two-end phasor system
   - Synchronize sender and receiver timestamps
   - Filter and validate signal angles and magnitudes

2. **`notebooks/02_forward_model.ipynb`**
   - Test forward model on measured data
   - Compare theoretical vs. observed voltage/power changes
   - Validate temperature-resistance relationship

3. **`notebooks/03_backward_methods.ipynb`**
   - Apply Singh method to measured data
   - Apply SI/Z-drop (voltage-drop impedance) method
   - Apply Power method
   - Compare results and discuss discrepancies

4. **`notebooks/04_sensitivity_analysis.ipynb`**
   - Sweep angle offsets (±0.5° to ±2°)
   - Sweep magnitude offsets (±0.5% to ±5%)
   - Evaluate method robustness
   - Determine practical measurement requirements

5. **`notebooks/05_plot_generation.ipynb`**
   - Generate all final thesis figures
   - Create summary tables
   - Export to `results/final_figures/` and `results/final_tables/`

## Supporting Diagnostics

Additional diagnostic notebooks are available in `notebooks/diagnostics/`:

- **T8_Singh_diagnostics.ipynb** – Detailed Singh method control and rowwise pairing
- **T9_Singh_corrected_B_diagnostics.ipynb** – Singh method with matrix corrections

These provide deeper validation but are not required for the main thesis narrative.

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip or conda

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter

```bash
jupyter lab
```

Then navigate to `notebooks/` and open the notebooks in order.

## Data Availability

**Raw measurement data is NOT included in this public repository** due to:
- Confidentiality agreements with data provider
- Operational security of the measured power system
- Proprietary measurement infrastructure

The code and analysis methods are public. If you have access to compatible phasor measurement data, you can run the analysis pipeline as described in `data/README.md`.

## Project Contents

### Core Contributions

- **Theoretical framework** for resistance-based temperature estimation
- **Three backward estimation methods** (Singh, SI/Z-drop, Power)
- **Sensitivity analysis** of methods to measurement uncertainties
- **Practical measurement requirements** for two-end phasor systems
- **Python implementation** of all methods with validation against real data

### Methods Implemented

1. **Singh Method**: Uses two-end voltage/current with line impedance assumption
2. **SI/Z-drop (Voltage-drop)**: Based on voltage drop across line impedance
3. **Power Method**: Uses active and reactive power flow symmetry

## Notes

- In the codebase, the voltage-drop method is sometimes referred to as **"Z-drop"** (working name)
- All measurements assume a 50 Hz power system
- Temperature coefficient for resistance: α ≈ 0.004 1/K (typical for copper)
- Archive folders contain exploratory work and preliminary tests not used in final results

## License

This project is **not licensed**. Code and figures may **not be used, copied, or distributed** without explicit permission.

## Contact

For questions about this thesis, contact:
**Sævar Ingi Sveinsson**  
Mittuniversitetet, 2026
