# Test Register

This document tracks all test notebooks and their purpose in the thesis.

| Test ID | Notebook / Folder | Purpose | Used in Thesis | Archive Location |
|---------|-------------------|---------|---|---|
| T01 | overview_currents_voltages_angles_power | Data check and signal overview | Yes – Method section | exploratory_tests |
| T02 | Bild på strömkorrigering | 180° receiver current correction check | Yes – Current direction | exploratory_tests |
| T03 | test7_singh_3ph_rowwise_pairing | Rowwise pairing and Singh validation | Yes – Results | exploratory_tests |
| T04 | 10-90_grader_fast_last / 02_forward_model.ipynb | Forward fixed-load model | Yes – Forward model results | old_forward_tests |
| T05 | Framåtriktad_länkmodell_med_fasvinkel | Amplitude/phase comparison | Yes – Forward model table | old_forward_tests |
| T06 | thermal_model_temperature_vs_current | Simple thermal model | Yes – Temperature vs current | exploratory_tests |
| T07 | T8 / T9 Singh diagnostics | Singh diagnostics and validation | Yes – Discussion | notebooks/diagnostics |
| T08 | bohus_v02.2_delta_U or 03b_zdrop_baseline_bohus.ipynb | Voltage-drop baseline (Z-drop method) | Yes – SI/Z-drop baseline | notebooks/diagnostics or old_zdrop_tests |
| T09 | bohus_power_angle_offset_sweep | Power method diagnostics | Yes – Explains high R in direct power method | old_sensitivity_tests |
| T10 | Vinkel_offset_sweep_Z_drop_metoden | Angle sensitivity (Z-drop method) | Yes – Sensitivity results | old_sensitivity_tests |
| T11 | Vinkel_offset_sweep_effekt_metoden | Angle sensitivity (Power method) | Yes – Sensitivity results | old_sensitivity_tests |
| T12 | Z_drop_magnitud_swep | Magnitude sensitivity (Z-drop method) | Yes – Sensitivity results | old_sensitivity_tests |
| T13 | Effekt_magnitud_sweep | Magnitude sensitivity (Power method) | Yes – Sensitivity results | old_sensitivity_tests |
| T14 | diagnostik_stromspikar | Periodic current spike diagnostics | No – GitHub only | exploratory_tests |
| T15 | Kabel_synthetic | Synthetic cable model testing | Preliminary | old_forward_tests |
| T16 | JÄMFÖRELSE_actual_vs_bias_zero | Angle bias comparison | Preliminary | exploratory_tests |
| T17 | Kent_vill_se_I_U_vinklar_P | Phase angle visualization | Ad-hoc request | exploratory_tests |
| T18 | kan_X_användas_som_baslinje | Reactance as baseline exploration | Preliminary | old_zdrop_tests |
| T19 | T6 - X ankare | Reactance anchoring test | Preliminary | old_zdrop_tests |
| T20 | T7_full_trefas_simultan_Singh | Full three-phase simultaneous Singh | Preliminary/diagnostic | old_singh_tests |
| T21 | Untitled5 | Miscellaneous | No | exploratory_tests |

## Mapping to Archived Notebooks

### old_forward_tests/
- 10-90_grader_V01.ipynb (T04 variant)
- 10-90_grader_fast_last.ipynb (T04 primary)
- Framåtriktad_länkmodell.ipynb (T05 variant)
- Framåtriktad_länkmodell_med_fast_last.ipynb (T05 primary)
- Kabel_synthetic.ipynb (T15)

### old_zdrop_tests/
- Spänningsfall_V01.ipynb (voltage-drop exploration)
- bohus_v02.2_delta_U.ipynb (T08 – only if moved here)
- T6 - X ankare.ipynb (T19)
- kan_X_användas_som_baslinje_för_att_förbättra_R-och_temperaturtolkningen.ipynb (T18)

### old_singh_tests/
- T7_full_trefas_simultan_Singh.ipynb (T20)
- T7_full_trefas_simultan_Singh-Copy1.ipynb (T20 backup)
- # T7_full_trefas_simultan_singh.txt (metadata)

### old_sensitivity_tests/
- Effekt_magnitud_sweep.ipynb (T13)
- Vinkel_offset_sweep_Z_drop_metoden.ipynb (T10)
- Vinkel_offset_sweep_effekt_metoden.ipynb (T11)
- Z_drop_magnitud_swep.ipynb (T12)

### exploratory_tests/
- JÄMFÖRELSE_actual_vs_bias_zero_vs_perfect_angles.ipynb (T16)
- Kent_vill_se_I_U_vinklar_P_med excell_filar.ipynb (T17)
- Untitled5.ipynb (T21)

### notebooks/diagnostics/
- T8_Singh_diagnostics.ipynb (T07)
- T9_Singh_corrected_B_diagnostics.ipynb (T07)
- 03b_zdrop_baseline_bohus.ipynb (T08 – if moved here)

## Notes

- Tests marked "Yes – [section]" are explicitly discussed or referenced in the thesis
- Tests marked "Preliminary" provide supporting evidence but are not primary results
- Tests marked "Ad-hoc" were generated on request but not part of the core methodology
- Test register can be updated as final thesis chapters are finalized
