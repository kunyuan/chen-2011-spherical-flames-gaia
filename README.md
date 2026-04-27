# chen-2011-spherical-flames-gaia

Gaia knowledge package formalizing Chen (2011) 'Extraction of laminar flame speed and Markstein length from outwardly propagating spherical flames' (Combust. Flame 158, 291–300) together with the 2026-04-09 Bohrium reproduction trace (chen-2011-cnf-158).

<!-- badges:start -->
<!-- badges:end -->

## Overview

> [!TIP]
> **Reasoning graph information gain: `2.5 bits`**
>
> Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    error_zero_at_le1["★ Zero error at Le=1 (all three models)\n(0.50 → 0.97)"]:::exported
    error_ordering_le_ne_1["★ Error ordering NMI < NMII < LM at Le ≠ 1\n(0.50 → 0.77)"]:::exported
    lb_vanishes_at_le1["Markstein length vanishes at Le=1\n(0.96 → 0.96)"]:::premise
    nq_window_requirement["★ NQ fitting window Rf > 1.5 cm (paper)\n(0.50 → 0.98)"]:::exported
    paper_lb_phi4_value["Paper Lb value at phi = 4.0 (H2/air)\n(0.97 → 0.98)"]:::premise
    repro_lb_phi4_tight_window_fails["Reproduction — NMI with Rf > 1.0 cm yields negative Lb\n(0.94 → 0.96)"]:::premise
    repro_lb_phi4_fixed_window_matches["Reproduction — NMI with Rf > 1.5 cm matches paper\n(0.94 → 0.96)"]:::premise
    paper_sl_phi1["Paper S_L at phi = 1.0 (H2/air)\n(0.97 → 0.98)"]:::premise
    paper_sl_phi2["Paper S_L at phi = 2.0\n(0.97 → 0.98)"]:::premise
    paper_sl_phi4["Paper S_L at phi = 4.0\n(0.97 → 0.98)"]:::premise
    cantera_sl_phi1["Cantera S_L at phi = 1.0\n(0.95 → 0.97)"]:::premise
    cantera_sl_phi2["Cantera S_L at phi = 2.0\n(0.95 → 0.97)"]:::premise
    cantera_sl_phi4["Cantera S_L at phi = 4.0\n(0.95 → 0.97)"]:::premise
    agreement_phi1["Agreement at phi = 1.0\n(0.50 → 1.00)"]:::premise
    agreement_phi2["Agreement at phi = 2.0\n(0.50 → 1.00)"]:::premise
    agreement_phi4["Agreement at phi = 4.0\n(0.50 → 1.00)"]:::premise
    cantera_validates_paper_sl["★ Cantera reproduces paper S_L to ±2 % (H2/air)\n(0.50 → 0.97)"]:::exported
    pyasurf_phi14_sb_noisy["pyASURF phi = 1.4 AMR-6 result is noisy (R² = 0.555)\n(0.93 → 0.93)"]:::premise
    pyasurf_phi06_amr6["pyASURF phi = 0.6 AMR-6 clean\n(0.93 → 0.93)"]:::premise
    amr_level8_grid_indep["Grid independence at AMR level 8 (Δ < 0.5 %)\n(0.92 → 0.92)"]:::premise
    soret_rich_h2_neglig["Soret effect < 2 % at phi = 4.0 rich H2\n(0.92 → 0.92)"]:::premise
    ignition_kernel_constraint["Ignition kernel constraint dx_base < 2 R_kernel\n(0.88 → 0.88)"]:::premise
    large_mech_impractical["Large mechanisms (>15 sp) are impractical in pyASURF\n(0.85 → 0.85)"]:::premise
    pyasurf_fig3_curves["pyASURF Fig. 3 — raw error-convergence curves\n(0.93 → 0.95)"]:::premise
    pyasurf_fig7_deltas["pyASURF Fig. 7 — raw model-spread numbers at Le=3\n(0.92 → 0.95)"]:::premise
    repro_fig3_ordering["Reproduction Fig. 3 — ordering confirmed\n(0.50 → 0.99)"]:::premise
    repro_fig7_relative["Reproduction Fig. 7 — quantitative match at Le=3\n(0.50 → 0.99)"]:::premise
    reproduction_lessons["★ Four pipeline lessons (OPS reproducibility check-list)\n(0.50 → 0.74)"]:::exported
    paper_taylor_phi134["Paper NMI extraction of Taylor phi = 1.34\n(0.95 → 0.97)"]:::premise
    repro_taylor_phi134["Reproduction NMI extraction of Taylor phi = 1.34\n(0.93 → 0.95)"]:::premise
    taylor_reanalysis_agreement["★ Taylor re-analysis reproduced to 0.1 % at phi = 1.34\n(0.50 → 0.98)"]:::exported
    qg_11_accept["QG — 11/13 figures ACCEPT on first pass\n(0.95 → 0.95)"]:::premise
    qg_fig9_partial["QG — Fig 9 PARTIAL → ACCEPT under relaxed policy\n(0.93 → 0.93)"]:::premise
    qg_fig4_fix["QG — Fig 4 REJECT → ACCEPT after Eq. 6 fix\n(0.95 → 0.95)"]:::premise
    fig1_skipped["Fig 1 — intentionally skipped\n(0.97 → 0.97)"]:::premise
    reproduction_13_of_14["★ Overall — 13/14 figures reproduced\n(0.50 → 0.89)"]:::exported
    chen2011_reproducible["★ Chen 2011 methodology is reproducible (top-level conclusion)\n(0.50 → 0.83)"]:::exported
    strat_0(["infer\n0.71 bits"]):::weak
    agreement_phi1 --> strat_0
    agreement_phi2 --> strat_0
    agreement_phi4 --> strat_0
    cantera_sl_phi1 --> strat_0
    cantera_sl_phi2 --> strat_0
    cantera_sl_phi4 --> strat_0
    chen2011_reproducible --> strat_0
    paper_sl_phi1 --> strat_0
    paper_sl_phi2 --> strat_0
    paper_sl_phi4 --> strat_0
    strat_0 --> cantera_validates_paper_sl
    strat_1(["infer\n0.28 bits"]):::weak
    amr_level8_grid_indep --> strat_1
    ignition_kernel_constraint --> strat_1
    large_mech_impractical --> strat_1
    pyasurf_phi06_amr6 --> strat_1
    pyasurf_phi14_sb_noisy --> strat_1
    soret_rich_h2_neglig --> strat_1
    strat_1 --> reproduction_lessons
    strat_2(["infer\n0.42 bits"]):::weak
    cantera_validates_paper_sl --> strat_2
    nq_window_requirement --> strat_2
    taylor_reanalysis_agreement --> strat_2
    strat_2 --> chen2011_reproducible
    strat_3(["infer\n0.15 bits"]):::weak
    chen2011_reproducible --> strat_3
    paper_lb_phi4_value --> strat_3
    repro_lb_phi4_fixed_window_matches --> strat_3
    repro_lb_phi4_tight_window_fails --> strat_3
    strat_3 --> nq_window_requirement
    strat_4(["infer\n0.13 bits"]):::weak
    chen2011_reproducible --> strat_4
    paper_taylor_phi134 --> strat_4
    repro_taylor_phi134 --> strat_4
    strat_4 --> taylor_reanalysis_agreement
    strat_5(["infer\n0.25 bits"]):::weak
    fig1_skipped --> strat_5
    qg_11_accept --> strat_5
    qg_fig4_fix --> strat_5
    qg_fig9_partial --> strat_5
    strat_5 --> reproduction_13_of_14
    strat_6(["infer\n0.09 bits"]):::weak
    lb_vanishes_at_le1 --> strat_6
    strat_6 --> error_zero_at_le1
    strat_7(["infer\n0.52 bits"]):::weak
    pyasurf_fig3_curves --> strat_7
    pyasurf_fig7_deltas --> strat_7
    repro_fig3_ordering --> strat_7
    repro_fig7_relative --> strat_7
    strat_7 --> error_ordering_le_ne_1

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| cantera_validates_paper_sl | An independent Cantera `FreeFlame` computation using the Li 2004 mechanism an... | 0.50 | 0.97 |
| chen2011_reproducible | The methodological conclusions of Chen 2011 — the three stretch-extrapolation... | 0.50 | 0.83 |
| error_def_residual_eq6 | The paper defines each model's extraction error as the equation residual of t... | 0.97 | 0.97 |
| error_ordering_le_ne_1 | For $\mathrm{Le} \neq 1$, the magnitudes of the residual-based extraction err... | 0.50 | 0.77 |
| error_zero_at_le1 | At Lewis number $\mathrm{Le} = 1$, the flame-speed response has no stretch de... | 0.50 | 0.97 |
| nq_window_requirement | Paper Section 3.2 requires that the NQ (nonlinear, NMI-based) extraction be f... | 0.50 | 0.98 |
| reproduction_13_of_14 | Overall reproduction outcome: 13 of the paper's 14 figures are reproducible (... | 0.50 | 0.89 |
| reproduction_lessons | The reproduction campaign establishes four pipeline-level lessons that are ne... | 0.50 | 0.74 |
| taylor_reanalysis_agreement | The reproduction's independent digitisation and NMI extraction of Taylor 1991... | 0.50 | 0.98 |

<!-- content:start -->
<!-- content:end -->
