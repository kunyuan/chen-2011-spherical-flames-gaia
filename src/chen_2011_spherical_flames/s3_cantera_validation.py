"""S3 — Tier-1 validation: Cantera FreeFlame reference vs paper S_L values.

Before running any spherical-flame simulation, the reproduction trace computes
a cheap 1-D flat-flame reference with Cantera. Agreement here is a necessary
pre-condition for trusting anything downstream (mechanism and conditions are
correct); disagreement would have indicated a setup error.
"""

from gaia.lang import claim, induction, support

from .motivation import setup_h2_air

paper_sl_phi1 = claim(
    "The paper [@Chen2011] reports an unstretched laminar flame speed "
    "$S_L = 213.6$ cm/s for H2/air at $\\phi = 1.0$, $T_u = 298$ K, "
    "$P = 1$ atm.",
    title="Paper S_L at phi = 1.0 (H2/air)",
)
paper_sl_phi2 = claim(
    "The paper reports $S_L = 290.8$ cm/s for H2/air at $\\phi = 2.0$.",
    title="Paper S_L at phi = 2.0",
)
paper_sl_phi4 = claim(
    "The paper reports $S_L = 148.0$ cm/s for H2/air at $\\phi = 4.0$.",
    title="Paper S_L at phi = 4.0",
)

cantera_sl_phi1 = claim(
    "Cantera `FreeFlame` with the Li 2004 H2 mechanism "
    "[@Li2004] at $\\phi = 1.0$, $T_u = 298$ K, $P = 1$ atm, "
    "mixture-averaged transport, returns $S_L = 210.3$ cm/s.",
    title="Cantera S_L at phi = 1.0",
)
cantera_sl_phi2 = claim(
    "Cantera `FreeFlame` with Li 2004 at $\\phi = 2.0$ returns "
    "$S_L = 286.1$ cm/s.",
    title="Cantera S_L at phi = 2.0",
)
cantera_sl_phi4 = claim(
    "Cantera `FreeFlame` with Li 2004 at $\\phi = 4.0$ returns "
    "$S_L = 145.2$ cm/s.",
    title="Cantera S_L at phi = 4.0",
)

agreement_phi1 = claim(
    "The Cantera value (210.3 cm/s) and the paper value (213.6 cm/s) at "
    "$\\phi = 1.0$ H2/air agree to 1.5 % (|ΔS_L|/S_L).",
    title="Agreement at phi = 1.0",
)
agreement_phi2 = claim(
    "At $\\phi = 2.0$: Cantera 286.1 vs paper 290.8 cm/s — 1.6 % agreement.",
    title="Agreement at phi = 2.0",
)
agreement_phi4 = claim(
    "At $\\phi = 4.0$: Cantera 145.2 vs paper 148.0 cm/s — 1.9 % agreement.",
    title="Agreement at phi = 4.0",
)

cantera_validates_paper_sl = claim(
    "An independent Cantera `FreeFlame` computation using the Li 2004 "
    "mechanism and mixture-averaged transport reproduces the paper's "
    "H2/air unstretched laminar flame speeds to within ±2 % across a wide "
    "range of equivalence ratios ($\\phi \\in \\{1.0, 2.0, 4.0\\}$). "
    "This is the tier-1 validation gate: the mechanism, transport choice, "
    "and initial conditions are therefore consistent with the paper.",
    title="Cantera reproduces paper S_L to ±2 % (H2/air)",
)

strat_agree_phi1 = support(
    [paper_sl_phi1, cantera_sl_phi1],
    agreement_phi1,
    reason=(
        "Paper value 213.6 cm/s (@paper_sl_phi1) vs independent Cantera "
        "value 210.3 cm/s (@cantera_sl_phi1). Absolute deviation 3.3 cm/s, "
        "relative 1.5 %."
    ),
    prior=0.99,
    background=[setup_h2_air],
)
strat_agree_phi2 = support(
    [paper_sl_phi2, cantera_sl_phi2],
    agreement_phi2,
    reason=(
        "Paper 290.8 cm/s (@paper_sl_phi2) vs Cantera 286.1 cm/s "
        "(@cantera_sl_phi2) ⇒ 1.6 % deviation."
    ),
    prior=0.99,
    background=[setup_h2_air],
)
strat_agree_phi4 = support(
    [paper_sl_phi4, cantera_sl_phi4],
    agreement_phi4,
    reason=(
        "Paper 148.0 cm/s (@paper_sl_phi4) vs Cantera 145.2 cm/s "
        "(@cantera_sl_phi4) ⇒ 1.9 % deviation."
    ),
    prior=0.99,
    background=[setup_h2_air],
)

sub_ind_phi1 = support(
    [cantera_validates_paper_sl], agreement_phi1,
    reason=(
        "If an independent Cantera computation correctly reproduces the "
        "paper's $S_L$ curve (@cantera_validates_paper_sl), then in "
        "particular the $\\phi = 1.0$ case should agree to within a few "
        "percent (@agreement_phi1)."
    ),
    prior=0.95,
    background=[setup_h2_air],
)
sub_ind_phi2 = support(
    [cantera_validates_paper_sl], agreement_phi2,
    reason=(
        "The same global validation claim predicts agreement at $\\phi = 2.0$ "
        "(@agreement_phi2)."
    ),
    prior=0.95,
    background=[setup_h2_air],
)
sub_ind_phi4 = support(
    [cantera_validates_paper_sl], agreement_phi4,
    reason=(
        "And it predicts agreement at $\\phi = 4.0$ (@agreement_phi4)."
    ),
    prior=0.95,
    background=[setup_h2_air],
)

ind_cantera_12 = induction(
    sub_ind_phi1, sub_ind_phi2,
    law=cantera_validates_paper_sl,
    reason=(
        "The $\\phi = 1.0$ and $\\phi = 2.0$ Cantera runs are independent "
        "flat-flame computations spanning lean-to-mildly-rich conditions."
    ),
    background=[setup_h2_air],
)
ind_cantera_all = induction(
    ind_cantera_12, sub_ind_phi4,
    law=cantera_validates_paper_sl,
    reason=(
        "Adding the rich $\\phi = 4.0$ case (@agreement_phi4) — an independent "
        "point at Lewis number $\\mathrm{Le} > 1$, far from the lean/moderate "
        "regime already covered — extends the induction across the full "
        "equivalence-ratio range studied in the paper."
    ),
    background=[setup_h2_air],
)

__all__ = [
    "paper_sl_phi1", "paper_sl_phi2", "paper_sl_phi4",
    "cantera_sl_phi1", "cantera_sl_phi2", "cantera_sl_phi4",
    "agreement_phi1", "agreement_phi2", "agreement_phi4",
    "cantera_validates_paper_sl",
    "strat_agree_phi1", "strat_agree_phi2", "strat_agree_phi4",
    "sub_ind_phi1", "sub_ind_phi2", "sub_ind_phi4",
    "ind_cantera_12", "ind_cantera_all",
]
