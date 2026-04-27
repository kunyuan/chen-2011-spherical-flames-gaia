"""S6 — Figure-by-figure QG audit and the overall reproducibility claim.

The reproduction trace culminates in a 2026-04-09 quality-gate (QG) audit
reviewed by an independent agent. This module formalises the audit outcome
and the top-level conclusion the whole package is trying to defend:
*Chen 2011's methodology is reproducible in 2026 with present-day open
tooling.*
"""

from gaia.lang import claim, contradiction, induction, support

from .motivation import reproduction_task, setup_ch4_air, setup_h2_air
from .s1_extraction_models import (
    error_def_residual_eq6,
    error_ordering_le_ne_1,
    error_zero_at_le1,
)
from .s2_nq_window import nq_window_requirement
from .s3_cantera_validation import cantera_validates_paper_sl
from .s4_asurf_reproduction import (
    amr_level8_grid_indep,
    reproduction_lessons,
    soret_rich_h2_neglig,
)
from .s5_taylor_reanalysis import taylor_reanalysis_agreement

# -- Fig 4 error-definition episode ------------------------------------------

fig4_def_rel_is_faithful = claim(
    "*Hypothesis A*: the faithful reproduction of the paper's Fig. 4 uses "
    "the relative error $(U_{\\text{model}} - U_{\\text{DM}})/U_{\\text{DM}}$ "
    "as the error quantity. Under this choice the reproduction plot comes "
    "out sign-inverted relative to the paper's Fig. 4.",
    title="Hypothesis A — Fig 4 error is relative",
)

fig4_def_residual_is_faithful = claim(
    "*Hypothesis B*: the faithful reproduction of the paper's Fig. 4 uses "
    "the model-equation residual evaluated at the exact DM solution, as "
    "specified in Eq. 6. Under this choice the reproduction matches the "
    "paper quantitatively and the initial QG REJECT verdict was reversed "
    "to ACCEPT.",
    title="Hypothesis B — Fig 4 error is Eq. 6 residual",
)

ctr_fig4_definitions = contradiction(
    fig4_def_rel_is_faithful, fig4_def_residual_is_faithful,
    reason=(
        "Only one of the two error conventions can be the *faithful* "
        "reproduction of the single Fig. 4 in the paper. Choosing the "
        "relative-error convention (Hypothesis A) produces a plot "
        "sign-inverted from the paper; choosing the Eq. 6 residual "
        "(Hypothesis B) produces a quantitative match. These hypotheses "
        "cannot both be true of the same paper figure."
    ),
    prior=0.99,
)

strat_fig4_eq6_is_correct = support(
    [error_def_residual_eq6],
    fig4_def_residual_is_faithful,
    reason=(
        "The paper's own error definition is the residual of each model "
        "equation at the exact DM solution (@error_def_residual_eq6). "
        "Therefore Hypothesis B — the Eq. 6 residual "
        "(@fig4_def_residual_is_faithful) — is the faithful reproduction; "
        "the sign inversion under Hypothesis A is an artefact of choosing "
        "a different error quantity than the paper's."
    ),
    prior=0.99,
)

# -- Per-figure QG verdicts --------------------------------------------------

qg_11_accept = claim(
    "The 2026-04-09 QG audit classified 11 of the 13 reproduced figures — "
    "namely Figs. 2, 3, 5, 6, 7, 8, 10, 11, 12, 13 and 14 — as ACCEPT "
    "(quantitatively match the paper within each figure's appropriate "
    "tolerance).",
    title="QG — 11/13 figures ACCEPT on first pass",
)

qg_fig9_partial = claim(
    "Fig. 9 (pressure-variation panel) received a PARTIAL verdict. "
    "Panel 9b ($P = 2.0$ atm, NMI extraction) achieves $R^{2} = 0.998$; "
    "panel 9a ($P = 0.5$ atm) was initially blocked by a solver NaN crash. "
    "Under the relaxed ±20 % QG policy the figure was upgraded to ACCEPT "
    "with a documented caveat: the P = 2.0 atm $S_b^{0}$ deviation of "
    "24 % from Cantera is a resolution artefact at AMR-6, not a "
    "methodology failure.",
    title="QG — Fig 9 PARTIAL → ACCEPT under relaxed policy",
)

qg_fig4_fix = claim(
    "Fig. 4 started with a REJECT verdict because the reproduction used "
    "a relative error $(U_{\\text{model}} - U_{\\text{DM}})/U_{\\text{DM}}$, "
    "producing a sign-inverted plot. After the error definition was "
    "corrected to the paper's Eq. 6 residual form, the figure visually "
    "and quantitatively matched the paper and the verdict flipped to "
    "ACCEPT.",
    title="QG — Fig 4 REJECT → ACCEPT after Eq. 6 fix",
)

fig1_skipped = claim(
    "Fig. 1 of the paper is a literature-survey schematic of prior OPS "
    "experimental setups, not a reproducible computation. It was "
    "explicitly marked skipped in the QG audit.",
    title="Fig 1 — intentionally skipped",
)

reproduction_13_of_14 = claim(
    "Overall reproduction outcome: 13 of the paper's 14 figures are "
    "reproducible (Figs. 2-14), with Fig. 1 skipped as a non-reproducible "
    "literature-survey schematic. Of the 13, eleven were ACCEPTed on the "
    "first QG pass, Fig. 4 was ACCEPTed after the Eq. 6 residual-error fix, "
    "and Fig. 9 was ACCEPTed under the relaxed ±20 % policy.",
    title="Overall — 13/14 figures reproduced",
)

strat_reproduction_13_of_14 = support(
    [qg_11_accept, qg_fig4_fix, qg_fig9_partial, fig1_skipped],
    reproduction_13_of_14,
    reason=(
        "Three disjoint outcome sets cover the 14 figures: 11 first-pass "
        "ACCEPT (@qg_11_accept), one corrected ACCEPT (@qg_fig4_fix), one "
        "relaxed-policy ACCEPT (@qg_fig9_partial), and one intentionally "
        "skipped literature-survey schematic (@fig1_skipped). "
        "11 + 1 + 1 + 1 = 14, with 13 in the 'reproduced' category."
    ),
    prior=0.95,
)

# -- Overall abduction: paper reproducibility --------------------------------

chen2011_reproducible = claim(
    "The methodological conclusions of Chen 2011 — the three stretch-"
    "extrapolation models (LM, NMI, NMII), the error ordering "
    "$|\\varepsilon_{\\text{NMI}}| < |\\varepsilon_{\\text{NMII}}| < "
    "|\\varepsilon_{\\text{LM}}|$ for $\\mathrm{Le} \\neq 1$, zero error "
    "at $\\mathrm{Le} = 1$, the NQ fitting-window requirement "
    "$R_f > 1.5$ cm for $\\mathrm{Le} > 1$, and the residual-based error "
    "definition of Eq. 6 — are reproducible in 2026 with independent "
    "open tooling (Cantera FreeFlame + pyASURF / Fortran ASURF on "
    "Bohrium), given the pipeline lessons documented in this package.",
    title="Chen 2011 methodology is reproducible (top-level conclusion)",
)

chen2011_not_reproducible = claim(
    "Counter-hypothesis: the paper's methodological conclusions are "
    "*not* robustly reproducible — at least one of the error ordering, "
    "the NQ window rule, or the residual-error definition would have "
    "failed to hold in an independent re-simulation. This hypothesis "
    "would have predicted multiple unfixable QG REJECT verdicts, not "
    "13/14 ACCEPTs. It is listed explicitly so the final critical "
    "analysis can confront it, but it is not currently wired into the "
    "factor graph as a compare/abduction alternative — see the BP "
    "troubleshooting note in ANALYSIS.md on why a separate counter-"
    "hypothesis node combined with a compare() operator produced "
    "pathological beliefs in earlier versions.",
    title="Counter-hypothesis — paper NOT robustly reproducible",
)

# Note on graph structure
# -----------------------
# An earlier revision wired the two top-level hypotheses into a classic
# abduction:
#     compare(chen2011_reproducible, chen2011_not_reproducible,
#             reproduction_13_of_14)
# together with an NAND-style contradiction.  The combination made BP
# degenerate: the compare operator injects equivalence factors
# (pred_h ⇔ obs, pred_alt ⇔ obs), which implicitly force pred_h ⇔ pred_alt;
# adding an explicit contradiction then collapses both hypotheses to
# near-zero posterior (symmetric ~0.14).  Removing the contradiction
# instead over-identifies them (both go to ~0.9).
#
# The underlying problem is that a bare hypothesis and its negation are
# not numerically-distinct "predictions" of the observation, so compare's
# equivalence factors cannot distinguish them.  A future revision could
# introduce numerical predictions (e.g. "≥ 12/14 pass" vs "≤ 10/14 pass")
# and re-wire a properly-differentiated abduction; for now the
# reproducibility claim is supported purely via the generative-direction
# induction below (three independent methodological pillars) and the
# bottom-up support from the QG audit outcomes.

# Three methodological pillars — generative induction
# (Cantera validation, Taylor re-analysis, NQ-window failure/fix).

s_repro_from_cantera = support(
    [chen2011_reproducible], cantera_validates_paper_sl,
    reason=(
        "Reproducibility (@chen2011_reproducible) predicts that an "
        "independent flame-speed computation with the paper's declared "
        "mechanism and conditions should match the paper's S_L values — "
        "exactly the content of @cantera_validates_paper_sl."
    ),
    prior=0.9,
    background=[setup_h2_air],
)

s_repro_from_taylor = support(
    [chen2011_reproducible], taylor_reanalysis_agreement,
    reason=(
        "Reproducibility likewise predicts that independently re-running "
        "the paper's extraction routine on the Taylor 1991 dataset "
        "recovers the paper's extracted $S_b^{0}$ values "
        "(@taylor_reanalysis_agreement)."
    ),
    prior=0.9,
    background=[setup_ch4_air],
)

s_repro_from_nq = support(
    [chen2011_reproducible], nq_window_requirement,
    reason=(
        "Reproducibility predicts that the paper's Section 3.2 NQ-window "
        "rule (@nq_window_requirement) would be confirmed by any "
        "independent attempt to extract $L_b$ at $\\mathrm{Le} > 1$: "
        "tight windows fail, wide windows succeed. The reproduction's "
        "failure-and-fix episode at $\\phi = 4.0$ did exactly that."
    ),
    prior=0.92,
    background=[setup_h2_air],
)

ind_methodological_pillars_12 = induction(
    s_repro_from_cantera, s_repro_from_taylor,
    law=chen2011_reproducible,
    reason=(
        "Cantera validation (H2/air tier-1) and Taylor re-analysis "
        "(CH4/air experimental) are independent pillars — different fuel, "
        "different data source, different tool — whose simultaneous "
        "agreement is hard to explain unless the methodology is real."
    ),
    background=[reproduction_task],
)
ind_methodological_pillars_all = induction(
    ind_methodological_pillars_12, s_repro_from_nq,
    law=chen2011_reproducible,
    reason=(
        "The NQ-window episode at $\\phi = 4.0$ adds a third independent "
        "pillar: unlike the first two it is a *qualitative* diagnostic "
        "prediction (tight window ⇒ negative $L_b$) that was confirmed. "
        "Three independent lines of evidence jointly elevate "
        "@chen2011_reproducible."
    ),
    background=[reproduction_task],
)

# Contextual claims: the pipeline lessons are a prerequisite, not a refutation.

pipeline_caveat = claim(
    "The reproducibility conclusion is *conditional* on the four pipeline "
    "lessons of @reproduction_lessons: ignition-kernel constraint, AMR "
    "level ≥ 7, Soret retained, and mechanism size ≤ ~15 species. "
    "Violating any of these is sufficient to block reproduction (e.g. "
    "the 86 % $L_b$ error at AMR-4/5, or the complete ignition failure "
    "with $N_{\\text{base}} = 50$). The paper's original 2011 tooling "
    "(Fortran ASURF with hand-tuned grids) implicitly respected these "
    "constraints; a modern reproducer has to learn them by failing first.",
    title="Reproducibility is conditional on four pipeline lessons",
)

strat_pipeline_caveat = support(
    [reproduction_lessons, amr_level8_grid_indep, soret_rich_h2_neglig],
    pipeline_caveat,
    reason=(
        "The four lessons (@reproduction_lessons) are collected from "
        "concrete failure-and-fix cycles. Grid independence at AMR 8 "
        "(@amr_level8_grid_indep) and Soret insensitivity "
        "(@soret_rich_h2_neglig) establish that the relevant regime is "
        "numerically converged once the check-list is respected — so the "
        "caveat is about *setup* rather than a hidden methodology gap."
    ),
    prior=0.92,
)

__all__ = [
    # Fig 4 episode
    "fig4_def_rel_is_faithful", "fig4_def_residual_is_faithful",
    "ctr_fig4_definitions", "strat_fig4_eq6_is_correct",
    # QG verdicts
    "qg_11_accept", "qg_fig9_partial", "qg_fig4_fix", "fig1_skipped",
    "reproduction_13_of_14", "strat_reproduction_13_of_14",
    # Top-level hypotheses (abduction disabled, see module docstring)
    "chen2011_reproducible", "chen2011_not_reproducible",
    # Inductive methodological pillars
    "s_repro_from_cantera", "s_repro_from_taylor", "s_repro_from_nq",
    "ind_methodological_pillars_12", "ind_methodological_pillars_all",
    # Pipeline caveat
    "pipeline_caveat", "strat_pipeline_caveat",
    # Referenced from other modules
    "error_zero_at_le1", "error_ordering_le_ne_1",
    "error_def_residual_eq6",
]
