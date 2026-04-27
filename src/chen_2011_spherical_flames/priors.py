"""Priors for the 29 independent claims of this package.

Prior-setting policy
--------------------

Independent claims in this package fall into five buckets:

1. **Paper-reported numerical values** (Chen 2011 published S_L, L_b, Taylor
   extraction result). These are peer-reviewed and quoted verbatim from the
   paper, so their truth-as-reported is essentially a matter of transcription
   accuracy — prior ≈ 0.97.
2. **Paper methodological definitions** (Eq. 6 residual definition, L_b → 0 at
   Le = 1). These are definitional / theoretical results in the paper, again
   prior ≈ 0.97.
3. **Reproduction measurements with run provenance** (Cantera `FreeFlame`
   numbers for H2/air and CH4/air, pyASURF Bohrium jobs with job-IDs, the
   ignition/AMR/Soret failure-and-fix outcomes). These are the outputs of
   specific, re-runnable jobs whose numerical values are logged in the trace.
   Prior is slightly lower (0.93-0.95) because the trace itself could mis-
   transcribe them and we cannot easily verify here.
4. **QG audit verdicts** (11 ACCEPT, Fig. 4 fix, Fig. 9 partial, Fig. 1
   skipped). These are recorded verdicts by an independent review agent.
   Prior ≈ 0.95 — the audit itself is documented and the verdicts are
   explicitly enumerated in the trace.
5. **Hypotheses being tested**:
    - ``chen2011_not_reproducible`` — the counter-hypothesis to the top-level
      conclusion. Low prior (0.10): most published combustion-modelling
      papers from an established group do reproduce when the pipeline is
      correct, but we do not rule it out a priori.
    - ``fig4_def_rel_is_faithful`` — Hypothesis A of the Fig-4 episode. Very
      low prior (0.05): the relative-error convention is a plausible naive
      choice a reproducer might make, but the paper's Eq. 6 explicitly
      prescribes the residual form, so this hypothesis is unlikely to be the
      faithful reading.
    - ``pred_amr_resolution_insensitive`` — counter-prediction that AMR
      level does not matter. Prior 0.20: possible in principle if the paper
      used coarser grids than we estimate, but the documented 86 % L_b error
      at AMR 4-5 is direct evidence against it; we leave some weight for the
      possibility that the pipeline lesson is over-generalised.
    - ``pred_amr7_needed`` — prediction that AMR ≥ 7 is needed to see the
      paper's error ordering. Prior 0.78: consistent with the reproduction's
      own AMR-level findings, and the paper's ASURF code almost certainly
      used comparable local resolution, but we leave a tail for the
      possibility that AMR-6 on modern hardware is already sufficient for
      some regimes.
"""

from .s1_extraction_models import error_def_residual_eq6, lb_vanishes_at_le1
from .s2_nq_window import (
    paper_lb_phi4_value,
    repro_lb_phi4_fixed_window_matches,
    repro_lb_phi4_tight_window_fails,
)
from .s3_cantera_validation import (
    cantera_sl_phi1,
    cantera_sl_phi2,
    cantera_sl_phi4,
    paper_sl_phi1,
    paper_sl_phi2,
    paper_sl_phi4,
)
from .s4_asurf_reproduction import (
    amr_level8_grid_indep,
    cantera_ref_phi1_ch4,
    ignition_kernel_constraint,
    large_mech_impractical,
    pred_amr7_needed,
    pred_amr_resolution_insensitive,
    pyasurf_fig3_curves,
    pyasurf_fig7_deltas,
    pyasurf_phi06_amr6,
    pyasurf_phi14_sb_noisy,
    pyasurf_phi1_sb,
    soret_rich_h2_neglig,
)
from .s5_taylor_reanalysis import paper_taylor_phi134, repro_taylor_phi134
from .s6_qg_audit import (
    chen2011_not_reproducible,
    fig1_skipped,
    fig4_def_rel_is_faithful,
    qg_11_accept,
    qg_fig4_fix,
    qg_fig9_partial,
)

PRIORS = {
    # ---- Bucket 1: paper-reported numerical values ------------------------
    paper_sl_phi1: (
        0.97,
        "Peer-reviewed value $S_L = 201.5$ cm/s quoted verbatim from Chen 2011 "
        "Table 1. The only uncertainty is transcription; the paper's own report "
        "is taken as ground truth for the reproduction campaign.",
    ),
    paper_sl_phi2: (
        0.97,
        "Peer-reviewed value $S_L = 290.8$ cm/s at $\\phi = 2.0$, H2/air, "
        "transcribed from Chen 2011.",
    ),
    paper_sl_phi4: (
        0.97,
        "Peer-reviewed value $S_L = 148.0$ cm/s at $\\phi = 4.0$, H2/air, "
        "transcribed from Chen 2011.",
    ),
    paper_lb_phi4_value: (
        0.97,
        "Peer-reviewed $L_b \\approx 0.35$ cm for rich H2/air $\\phi = 4.0$ "
        "(Fig. 5 of Chen 2011). Value is a definitional fact about the paper.",
    ),
    paper_taylor_phi134: (
        0.95,
        "Paper-reported NMI-extracted $S_b^{0} = 285$ cm/s from Taylor 1991 "
        "CH4/air $\\phi = 1.34$ data. Slightly lower prior than direct S_L "
        "values because this is a derived quantity whose extraction depends "
        "on the paper's own fitting choices; but the number itself is still "
        "a paper-reported fact.",
    ),
    # ---- Bucket 2: paper methodological definitions -----------------------
    error_def_residual_eq6: (
        0.97,
        "Definitional: the paper's Eq. 6 explicitly prescribes each model's "
        "extraction error as the residual at the exact DM solution. This is a "
        "mathematical statement inside the paper, essentially beyond dispute.",
    ),
    lb_vanishes_at_le1: (
        0.96,
        "Analytic / theoretical result: at $\\mathrm{Le} = 1$ the effective "
        "stretch coefficient in the quasi-steady analysis vanishes, forcing "
        "$L_b = 0$ for all three models. This is paper theory (Section 2.1-2.3) "
        "and is consistent with every textbook derivation of Markstein length.",
    ),
    # ---- Bucket 3: reproduction measurements (run-provenanced) ------------
    cantera_sl_phi1: (
        0.95,
        "Cantera FreeFlame with Li 2004 mechanism is a standard reference "
        "computation; the reported $S_L = 204.7$ cm/s for $\\phi = 1.0$ is a "
        "logged numerical output and is easy to regenerate. We leave a small "
        "tail for mechanism/installation drift.",
    ),
    cantera_sl_phi2: (
        0.95,
        "Cantera FreeFlame + Li 2004 at $\\phi = 2.0$ giving 286.1 cm/s; "
        "logged numerical output of a deterministic re-runnable computation.",
    ),
    cantera_sl_phi4: (
        0.95,
        "Cantera FreeFlame + Li 2004 at $\\phi = 4.0$ giving 145.2 cm/s; "
        "same justification as the other two Cantera H2/air values.",
    ),
    cantera_ref_phi1_ch4: (
        0.95,
        "Cantera FreeFlame with GRI-Mech 3.0 at CH4/air $\\phi = 1.0$ giving "
        "$\\sim$ 39 cm/s is a textbook result; used as the Tier-1 reference "
        "for the CH4/air arm of the reproduction.",
    ),
    pyasurf_phi1_sb: (
        0.93,
        "pyASURF spherical-flame result at CH4/air $\\phi = 1.0$, AMR 7, base "
        "grid 125/25 cm, GRI30_noNOx, $S_b^{0} \\approx 32$ cm/s. Logged as a "
        "Bohrium job with a specific job-ID. Slightly lower than Cantera "
        "because the spherical-flame extraction is more sensitive to grid / "
        "mechanism choices.",
    ),
    pyasurf_phi14_sb_noisy: (
        0.93,
        "pyASURF AMR 6 at CH4/air $\\phi = 1.4$ produced $S_b^{0}$ values "
        "spanning $\\approx$ 38-65 cm/s with spurious oscillations. The high-"
        "variance observation is itself reliably recorded in the trace even "
        "though the numerical values are noisy.",
    ),
    pyasurf_phi06_amr6: (
        0.93,
        "pyASURF AMR 6 at CH4/air $\\phi = 0.6$ produced a clean "
        "$S_b^{0} \\approx 11$ cm/s agreeing with Cantera. Contrast with the "
        "$\\phi = 1.4$ noisy result is the central observation; the clean "
        "extraction itself is a logged Bohrium job.",
    ),
    pyasurf_fig3_curves: (
        0.93,
        "Raw pyASURF Fig. 3 error curves: slope-2 convergence plus NMI < "
        "NMII < LM ordering at every sampled $R_f$. Logged numerical output "
        "of a specific Bohrium job; the slope-and-ordering pattern is "
        "directly visible in the logs.",
    ),
    pyasurf_fig7_deltas: (
        0.92,
        "Raw pyASURF Fig. 7 model-spread numbers at Le=3 "
        "($\\approx 7.3 \\%$ and $2.4 \\%$). Logged output of a specific "
        "spherical-flame job; slightly lower prior than Fig. 3 because the "
        "Le=3 reproduction is extrapolated from $\\phi = 4.0$ H2/air and "
        "has more room for a transcription error.",
    ),
    repro_taylor_phi134: (
        0.93,
        "Digitised Taylor 1991 experimental points at $\\phi = 1.34$ "
        "re-analysed with the reproduction's own NMI extraction, giving "
        "$S_b^{0}$ = 288 $\\pm$ 4 cm/s. The digitisation step is the only "
        "significant source of uncertainty.",
    ),
    repro_lb_phi4_tight_window_fails: (
        0.94,
        "Initial NMI extraction at $\\phi = 4.0$ with a fitting window "
        "starting near ignition ($R_f > 1.0$ cm) returned a negative $L_b$. "
        "This is a directly observed failure mode logged in the trace.",
    ),
    repro_lb_phi4_fixed_window_matches: (
        0.94,
        "Correcting the fitting window to $R_f > 1.5$ cm recovered "
        "$L_b \\approx 0.35$ cm, matching the paper. Another directly "
        "observed and logged outcome.",
    ),
    soret_rich_h2_neglig: (
        0.92,
        "Toggling Soret on/off for rich H2/air changed $S_b^{0}$ by less "
        "than 1 %. Consistent with the general literature expectation that "
        "thermal diffusion is minor for heavy-component mixtures once the "
        "main species are H2O; the reproduction confirmed this by explicit "
        "toggle.",
    ),
    amr_level8_grid_indep: (
        0.92,
        "At AMR level 8 the extracted $S_b^{0}$ and $L_b$ agreed with AMR 7 "
        "to better than 1 %, establishing grid independence of the used "
        "resolution. This is an explicit convergence test in the trace.",
    ),
    # ---- Bucket 4: QG audit verdicts --------------------------------------
    qg_11_accept: (
        0.95,
        "Recorded verdict of the 2026-04-09 QG audit: 11 figures (Figs 2, 3, "
        "5, 6, 7, 8, 10, 11, 12, 13, 14) ACCEPTed on first pass. Enumerated "
        "in the trace and cross-checked against the figure-by-figure table.",
    ),
    qg_fig9_partial: (
        0.93,
        "Recorded PARTIAL verdict for Fig. 9, upgraded to ACCEPT under the "
        "relaxed $\\pm$20 % policy with a documented AMR-6 caveat. Policy "
        "adjudication adds a small ambiguity, hence slightly lower than the "
        "pure 11-ACCEPT verdict.",
    ),
    qg_fig4_fix: (
        0.95,
        "Recorded REJECT-then-ACCEPT episode for Fig. 4: initial REJECT due "
        "to the relative-error convention, upgraded to ACCEPT after the Eq. 6 "
        "residual fix. Fully enumerated in the trace with before/after plots.",
    ),
    fig1_skipped: (
        0.97,
        "Fig. 1 of Chen 2011 is a literature-survey schematic of prior OPS "
        "experimental setups, not a computable figure. 'Skipped' is the "
        "documented and obviously-correct disposition.",
    ),
    # ---- Bucket 3 (cont.): pipeline lessons -------------------------------
    ignition_kernel_constraint: (
        0.88,
        "Established by direct failure-and-fix in the trace: $N_{\\text{base}} "
        "= 50$ failed to ignite; raising the ignition-kernel / base grid "
        "resolution ignited reliably. Lower prior than the specific numerical "
        "measurements because the quantitative boundary is regime-dependent.",
    ),
    large_mech_impractical: (
        0.85,
        "Generalisation from multiple attempts with mechanisms of $\\gtrsim$ "
        "15 species: wall-clock per FreeFlame call becomes several minutes, "
        "and spherical-flame AMR runs become impractical on the Bohrium nodes "
        "used. Prior is lower because 'impractical' is task-specific: for a "
        "one-off Cantera point with hours of budget this might not apply.",
    ),
    # ---- Bucket 5: hypotheses being tested -------------------------------
    chen2011_not_reproducible: (
        0.10,
        "Low prior on the counter-hypothesis. Chen 2011 comes from an "
        "established combustion group, the mechanism (Li 2004) and tooling "
        "(Cantera, ASURF-class codes) are mainstream, and the paper's "
        "mathematical claims are elementary. A priori we expect it to "
        "reproduce; we do not set the prior to zero because the field has "
        "seen occasional non-reproducible combustion-modelling papers.",
    ),
    fig4_def_rel_is_faithful: (
        0.05,
        "The paper's Eq. 6 explicitly specifies the residual form, so the "
        "relative-error convention is almost certainly not the faithful "
        "reproduction. We leave a small $\\approx$ 5 % tail because papers "
        "occasionally use a different error definition in one figure than "
        "the rest of the text.",
    ),
    pred_amr_resolution_insensitive: (
        0.20,
        "Counter-hypothesis to the AMR-dependence claim. The observed 86 % "
        "$L_b$ error at AMR 4-5 is direct evidence against it, but we leave "
        "meaningful weight because the AMR level adequacy is known to be "
        "regime-dependent (clean at $\\phi = 0.6$, noisy at $\\phi = 1.4$) "
        "and the counter-hypothesis could survive in specific regimes.",
    ),
    pred_amr7_needed: (
        0.78,
        "Prediction consistent with (i) the reproduction's own AMR-level "
        "sensitivity study, (ii) the requirement to reproduce the paper's "
        "error-ordering claim, and (iii) general numerical-combustion "
        "experience. Not higher because the 'needed' threshold is somewhat "
        "mechanism- and geometry-dependent.",
    ),
}
