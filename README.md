# chen-2011-spherical-flames-gaia

A Gaia knowledge package formalizing **Chen (2011)**,
*"On the extraction of laminar flame speed and Markstein length from outwardly
propagating spherical flames,"* Combustion and Flame **158**, 291–300
(DOI: [`10.1016/j.combustflame.2010.09.001`](https://doi.org/10.1016/j.combustflame.2010.09.001)),
together with an independent 2026-04-09 reproduction trace (`chen-2011-cnf-158`)
produced on the Playground platform.

## 1. Scope

The package captures two formally-related layers of knowledge:

1. **Paper-level methodological claims.** The three stretch-extrapolation
   models (LM, NMI, NMII) and their accepted synthetic benchmark (SM); the
   error ordering
   $|\varepsilon_{\text{NMI}}| < |\varepsilon_{\text{NMII}}| < |\varepsilon_{\text{LM}}|$
   for $\mathrm{Le} \ne 1$; the vanishing of $L_b$ at $\mathrm{Le} = 1$;
   the $R_f > 1.5$ cm NQ fitting-window requirement; and the residual-based
   error definition (Eq. 6).
2. **Reproduction-level observations.** Cantera `FreeFlame` reference
   values for H2/air and CH4/air; pyASURF / Fortran ASURF spherical-flame
   runs logged on the Bohrium platform; the figure-by-figure Quality-Gate
   (QG) audit (13/14 figures reproduced); and the four pipeline lessons
   distilled from concrete failure-and-fix cycles.

The two layers are connected by **`support`** and **`induction`**
strategies in the generative direction: each paper-level law predicts
reproduction observations; independent observations collectively confirm
the law.

## 2. Headline result

`gaia infer .` produces exact junction-tree beliefs over 95 knowledge
declarations, 28 strategies, and 1 operator. The top-level conclusion

> `chen2011_reproducible` — "the paper's methodological conclusions are
> reproducible in 2026 with independent open tooling, given the four
> pipeline lessons of `reproduction_lessons`"

has posterior belief **0.832**, compared with 0.100 for the counter-
hypothesis. Every exported conclusion has belief ≥ 0.74; the only claim
that goes to ~0 is `fig4_def_rel_is_faithful`, the rejected convention of
the Fig. 4 episode. See [`ANALYSIS.md`](ANALYSIS.md) for the full critical
analysis, confidence tiers, weak points, and BP troubleshooting notes.

## 3. Package layout

```
chen-2011-spherical-flames-gaia/
├── README.md                    # this file
├── ANALYSIS.md                  # critical analysis (top-level beliefs + weak points)
├── pyproject.toml               # [tool.gaia] uuid, type, deps
├── references.json              # CSL-JSON bibliography ([@Chen2011], [@Li2004], …)
├── artifacts/
│   ├── trace.md                 # 96-step reproduction trace (agent-readable)
│   └── trace-raw.json           # raw trace data from the Playground API
├── src/chen_2011_spherical_flames/
│   ├── __init__.py              # re-exports + __all__
│   ├── motivation.py            # research setting + questions
│   ├── s1_extraction_models.py  # LM / NMI / NMII / SM; Eq. 6 residual definition
│   ├── s2_nq_window.py          # R_f > 1.5 cm NQ fitting-window rule
│   ├── s3_cantera_validation.py # Tier-1 Cantera FreeFlame vs paper S_L
│   ├── s4_asurf_reproduction.py # pyASURF spherical-flame runs + pipeline lessons
│   ├── s5_taylor_reanalysis.py  # Taylor 1991 CH4/air re-analysis
│   ├── s6_qg_audit.py           # Per-figure QG verdicts + top-level conclusion
│   └── priors.py                # 31 priors on independent claims
└── .gaia/                       # produced by `gaia compile` + `gaia infer`
    ├── ir.json
    ├── ir_hash
    └── beliefs.json
```

## 4. Reproducing the inference

Requires Python 3.12+, `gaia-lang >= 0.4.3`, and `uv`:

```bash
cd chen-2011-spherical-flames-gaia
uv sync
gaia compile .
gaia check --hole .   # should report "All independent claims have priors assigned"
gaia infer .          # writes .gaia/beliefs.json
gaia render . --target docs   # generates docs/detailed-reasoning.md (per-module graphs)
```

## 5. Exported conclusions

The package exposes the following conclusions as its external interface
(see `src/chen_2011_spherical_flames/__init__.py`):

| Claim | Role | Posterior |
|-------|------|----------:|
| `chen2011_reproducible` | Top-level methodological conclusion | 0.832 |
| `reproduction_13_of_14` | QG-audit headline outcome | 0.886 |
| `cantera_validates_paper_sl` | Tier-1 validation via Cantera | 0.971 |
| `taylor_reanalysis_agreement` | Tier-2 Taylor re-analysis agreement | 0.982 |
| `nq_window_requirement` | $R_f > 1.5$ cm NQ-window rule | 0.976 |
| `error_ordering_le_ne_1` | Paper's NMI < NMII < LM ordering | 0.769 |
| `error_zero_at_le1` | Paper's $L_b \to 0$ at $\mathrm{Le} = 1$ | 0.970 |
| `error_def_residual_eq6` | Paper's Eq. 6 residual-error definition | 0.969 |
| `reproduction_lessons` | Four pipeline caveats for trustworthy OPS runs | 0.744 |

## 6. Citing

The underlying scientific result is due to Chen 2011 — cite the journal
paper. The reproduction trace is cited internally as `[@ChenTrace2026]`.
If you re-use this Gaia package, please cite both.
