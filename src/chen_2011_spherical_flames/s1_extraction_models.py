"""S1 — Three stretch-extrapolation models (LM, NMI, NMII).

The paper benchmarks three extraction models against an exact Synthetic-Model
(SM) solution of $f \\ln f = c$. The model definitions are mathematical
settings; the error ordering and the Le=1 vanishing behaviour are claims
subject to review.
"""

from gaia.lang import claim, setting, support

from .motivation import spherical_flame_setup

def_lm = setting(
    "Linear model (LM, also called linear extrapolation, LC): "
    "$S_b = S_b^{0} - L_b \\, K$, where $S_b$ is the burned-gas flame speed, "
    "$S_b^{0}$ the unstretched flame speed, $L_b$ the Markstein length with "
    "respect to burned gas, and $K = (2/R_f)\\,dR_f/dt$ the stretch rate.",
    title="LM — linear stretch model",
)

def_nmi = setting(
    "Nonlinear model I (NMI), due to Kelley-Law [@KelleyLaw2009]: the "
    "implicit relation $(S_b/S_b^{0})^{2}\\,\\ln\\!\\big[(S_b/S_b^{0})^{2}\\big] "
    "= -2\\, L_b\\, K / S_b^{0}$. Used in the 'NQ' (nonlinear quasi-steady) "
    "extraction procedure.",
    title="NMI — Kelley-Law nonlinear model",
)

def_nmii = setting(
    "Nonlinear model II (NMII): a different nonlinear form derived from "
    "asymptotic analysis of the quasi-steady stretched flame. Explicit "
    "functional form is given in the paper [@Chen2011]; for the purpose of "
    "this package it suffices to distinguish it from LM and NMI as a third "
    "extrapolation scheme.",
    title="NMII — second nonlinear model",
)

def_sm = setting(
    "Synthetic Model (SM): the implicit equation $f \\ln f = c$ used by the "
    "paper as an exact reference. Given $c$, solving for $f$ gives the exact "
    "(unstretched) burned-gas flame speed; LM, NMI and NMII are asymptotic "
    "approximations to this reference, making SM the natural benchmark.",
    title="SM — exact synthetic reference",
)

error_def_residual_eq6 = claim(
    "The paper defines each model's extraction error as the equation "
    "residual of the model evaluated at the exact SM solution (Eq. 6 of "
    "[@Chen2011]): "
    "LM residual: $U - 1 + L^{0}\\,(2U/R)$; "
    "NMI residual: $U - 1 + L^{0}\\,(2/R)$; "
    "NMII residual: $\\ln(U) + L^{0}\\,(2/(R\\,U))$. "
    "This is a *residual* definition, not the naive relative error "
    "$(U_{\\text{model}} - U_{\\text{DM}})/U_{\\text{DM}}$.",
    title="Error definition is residual-based (Eq. 6)",
)

error_zero_at_le1 = claim(
    "At Lewis number $\\mathrm{Le} = 1$, the flame-speed response has no "
    "stretch dependence ($L_b \\to 0$), so LM, NMI and NMII all give the "
    "exact unstretched flame speed — the extraction error is zero for all "
    "three models.",
    title="Zero error at Le=1 (all three models)",
)

error_ordering_le_ne_1 = claim(
    "For $\\mathrm{Le} \\neq 1$, the magnitudes of the residual-based "
    "extraction errors of the three models obey "
    "$|\\varepsilon_{\\mathrm{NMI}}| \\,<\\, |\\varepsilon_{\\mathrm{NMII}}| "
    "\\,<\\, |\\varepsilon_{\\mathrm{LM}}|$: the linear model has the "
    "largest error, NMI the smallest. In the paper this ordering is shown "
    "in Figs. 3, 4 and 7.",
    title="Error ordering NMI < NMII < LM at Le ≠ 1",
)

lb_vanishes_at_le1 = claim(
    "At Lewis number $\\mathrm{Le} = 1$, the Markstein length $L_b$ "
    "vanishes: the flame-speed response has no stretch dependence. This is "
    "a direct consequence of the asymptotic expansion: the leading "
    "stretch coefficient is proportional to $\\mathrm{Le} - 1$ (Markstein "
    "1964 result recovered in Matalon-Matkowsky asymptotics).",
    title="Markstein length vanishes at Le=1",
)

error_zero_from_definition = support(
    [lb_vanishes_at_le1],
    error_zero_at_le1,
    reason=(
        "At $\\mathrm{Le}=1$ the Markstein length $L_b$ vanishes "
        "(@lb_vanishes_at_le1). Substituting $L_b = 0$ into the LM, NMI "
        "and NMII definitions (@def_lm, @def_nmi, @def_nmii) reduces each "
        "to $S_b = S_b^{0}$, which exactly matches the SM reference "
        "(@def_sm). Hence all three residuals vanish identically "
        "(@error_zero_at_le1)."
    ),
    prior=0.98,
    background=[def_lm, def_nmi, def_nmii, def_sm, spherical_flame_setup],
)

__all__ = [
    "def_lm",
    "def_nmi",
    "def_nmii",
    "def_sm",
    "error_def_residual_eq6",
    "error_zero_at_le1",
    "error_ordering_le_ne_1",
    "lb_vanishes_at_le1",
    "error_zero_from_definition",
]
