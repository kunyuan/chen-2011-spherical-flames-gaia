"""S2 — NQ fitting-window requirement for Le > 1.

The paper's Section 3.2 prescribes a specific fitting window
($R_f > 1.5$ cm) for the NQ (nonlinear quasi-steady) extraction; the
reproduction trace empirically confirmed this via a failure-then-fix cycle.
"""

from gaia.lang import claim, support

from .motivation import setup_h2_air

nq_window_requirement = claim(
    "Paper Section 3.2 requires that the NQ (nonlinear, NMI-based) "
    "extraction be fitted only to the portion of the $R_f(t)$ trajectory "
    "with $R_f > 1.5$ cm. For rich flames with $\\mathrm{Le} > 1$ (e.g. "
    "$\\phi = 4.0$ H2/air), fitting windows that include smaller radii "
    "produce unphysical negative Markstein length from NMI.",
    title="NQ fitting window Rf > 1.5 cm (paper)",
)

paper_lb_phi4_value = claim(
    "For $\\phi = 4.0$ H2/air at $T_u = 298$ K, $P = 1$ atm, the paper "
    "reports a Markstein length $L_b = 0.044$ cm using NMI with the "
    "fitting window $R_f > 1.5$ cm.",
    title="Paper Lb value at phi = 4.0 (H2/air)",
)

repro_lb_phi4_tight_window_fails = claim(
    "The reproduction attempt initially used a fitting window "
    "$R_f > 1.0$ cm for NMI extraction at $\\phi = 4.0$ H2/air. The fit "
    "returned a negative $L_b$, which is unphysical for $\\mathrm{Le} > 1$.",
    title="Reproduction — NMI with Rf > 1.0 cm yields negative Lb",
)

repro_lb_phi4_fixed_window_matches = claim(
    "After switching the NMI fitting window to $R_f > 1.5$ cm (matching the "
    "paper's Section 3.2), the reproduction yields $L_b(\\phi=4.0) = 0.042$ "
    "cm. Paper value: $0.044$ cm. Deviation: 4.5 %.",
    title="Reproduction — NMI with Rf > 1.5 cm matches paper",
)

strat_nq_window_confirmed = support(
    [repro_lb_phi4_tight_window_fails, repro_lb_phi4_fixed_window_matches,
     paper_lb_phi4_value],
    nq_window_requirement,
    reason=(
        "The reproduction provides a before/after pair of observations. "
        "With a tight window (@repro_lb_phi4_tight_window_fails) NMI fails "
        "with negative $L_b$; with the paper's prescribed window "
        "(@repro_lb_phi4_fixed_window_matches) NMI returns $L_b = 0.042$ cm, "
        "within 5 % of the paper's reported value (@paper_lb_phi4_value). "
        "The contrast demonstrates that $R_f > 1.5$ cm is not merely "
        "suggested but *necessary* for stable extraction at $\\mathrm{Le} > 1$, "
        "confirming the paper's Section 3.2 claim."
    ),
    prior=0.90,
    background=[setup_h2_air],
)

__all__ = [
    "nq_window_requirement",
    "paper_lb_phi4_value",
    "repro_lb_phi4_tight_window_fails",
    "repro_lb_phi4_fixed_window_matches",
    "strat_nq_window_confirmed",
]
