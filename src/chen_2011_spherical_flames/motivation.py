"""Motivation — setup and research question for Chen 2011 reproduction.

Chen, Z. (2011). On the extraction of laminar flame speed and Markstein length
from outwardly propagating spherical flames. *Combustion and Flame* 158,
291-300 [@Chen2011]. This Gaia package formalizes the paper together with the
independent reproduction trace `chen-2011-cnf-158` [@ChenTrace2026].
"""

from gaia.lang import claim, question, setting

spherical_flame_setup = setting(
    "An outwardly propagating spherical (OPS) flame is ignited at the centre "
    "of a closed chamber. The flame-front radius $R_f(t)$ is tracked as a "
    "function of time; from the trajectory one extracts the unstretched "
    "laminar flame speed with respect to burned gas $S_b^0$ and the Markstein "
    "length with respect to burned gas $L_b$. Stretch rate is $K = (2/R_f)\\,dR_f/dt$.",
    title="Outwardly propagating spherical flame (OPS) setup",
)

setup_h2_air = setting(
    "Hydrogen/air mixture at initial temperature $T_u = 298$ K, pressure "
    "$P = 1$ atm, equivalence ratio $\\phi \\in \\{0.7, 1.0, 2.0, 3.0, 4.0, 5.0\\}$. "
    "Kinetic mechanism: Li et al. 2004 [@Li2004] (10 species, 21 reactions). "
    "Transport: mixture-averaged with Soret (thermal diffusion) term retained. "
    "Spherical domain $r \\in [0, 50]$ cm.",
    title="H2/air conditions (Figs. 10-11, 2011)",
)

setup_ch4_air = setting(
    "Methane/air mixture at $T_u = 298$ K, $\\phi \\in [0.6, 1.4]$, pressures "
    "$P \\in \\{0.5, 1.0, 2.0\\}$ atm. Kinetic mechanism: GRI-Mech 3.0 (53 species) "
    "or the reduced GRI30_noNOx_36sp variant (36 species, NOx removed). "
    "Used for Figs. 8, 9, and for cross-checking against Taylor 1991 data [@Taylor1991].",
    title="CH4/air conditions (Figs. 8-9, 12-14)",
)

research_question = question(
    "Given a measured $R_f(t)$ trajectory from an outwardly propagating "
    "spherical flame, which stretch-extrapolation model yields the most "
    "accurate unstretched laminar flame speed $S_L^0$ and Markstein length "
    "$L_b$, and over what fitting window is each model reliable?",
    title="Research question",
)

reproduction_task = question(
    "Are the methodological conclusions of Chen 2011 (three-model error "
    "ordering, Markstein-length behaviour, NQ fitting-window requirement, "
    "residual-based error definition in Eq. 6) reproducible using independent "
    "Cantera FreeFlame reference runs and pyASURF / Fortran ASURF spherical "
    "flame simulations in 2026?",
    title="Reproduction question (this package)",
)

__all__ = [
    "spherical_flame_setup",
    "setup_h2_air",
    "setup_ch4_air",
    "research_question",
    "reproduction_task",
]
