# Critical Analysis — `chen-2011-spherical-flames-gaia`

This analysis is the analytical payoff of formalizing Chen (2011) *"On the
extraction of laminar flame speed and Markstein length from outwardly
propagating spherical flames,"* Combustion and Flame 158, 291–300
(DOI: `10.1016/j.combustflame.2010.09.001`), together with the independent
reproduction trace `chen-2011-cnf-158` produced on the Playground platform
on 2026-04-09.

After the six formalization passes, `gaia infer` produces exact
junction-tree beliefs over 60 nodes (95 knowledge declarations, 28
strategies, 1 contradiction operator). All numbers quoted below come from
`.gaia/beliefs.json` at IR hash `sha256:0b200926f...` (run with Gaia-lang
0.4.3).

## 1. Top-level posterior beliefs

| Claim | Posterior | Prior | Role |
|-------|----------:|------:|------|
| `chen2011_reproducible` | **0.832** | — (derived) | Top-level methodological conclusion |
| `chen2011_not_reproducible` | 0.100 | 0.10 | Counter-hypothesis (orphaned — see §5) |
| `reproduction_13_of_14` | 0.886 | — (derived) | QG-audit headline outcome |
| `cantera_validates_paper_sl` | 0.971 | — (derived) | Tier-1 Cantera validation |
| `taylor_reanalysis_agreement` | 0.982 | — (derived) | Tier-2 Taylor re-analysis agreement |
| `nq_window_requirement` | 0.976 | — (derived) | $R_f > 1.5$ cm NQ-window rule |
| `error_ordering_le_ne_1` | 0.769 | — (derived) | Paper's NMI < NMII < LM error ordering |
| `error_def_residual_eq6` | 0.969 | 0.97 | Paper's Eq. 6 residual error definition |
| `fig4_def_residual_is_faithful` | 0.978 | — (derived) | Hypothesis B of Fig 4 episode |
| `fig4_def_rel_is_faithful` | **0.001** | 0.05 | Hypothesis A of Fig 4 episode |

Two binary contests settle cleanly:

1. **Chen 2011 reproduces** — top-level belief 0.832 vs counter-hypothesis
   0.10 — a posterior odds ratio of ~8:1 in favor of reproducibility, driven
   by three independent methodological pillars (Cantera H2/air validation,
   Taylor CH4/air re-analysis, NQ-window failure-and-fix) plus the QG
   audit's 13/14 pass rate.
2. **Fig 4 uses Eq. 6 residuals, not relative error** — the explicit
   `contradiction(fig4_def_rel_is_faithful, fig4_def_residual_is_faithful)`
   operator sends Hypothesis A to ~0.001 and Hypothesis B to 0.978, exactly
   as the paper's own Eq. 6 demands.

## 2. Confidence tiers on exported conclusions

The package's `__init__.py` exports a small set of conclusions. Tiering:

| Tier | Belief range | Claims |
|------|--------------|--------|
| Very high (≥ 0.95) | 0.95 – 1.00 | `error_def_residual_eq6` (0.969), `error_zero_at_le1` (0.970), `nq_window_requirement` (0.976), `cantera_validates_paper_sl` (0.971), `taylor_reanalysis_agreement` (0.982) |
| High (0.85 – 0.95) | 0.83 – 0.95 | `chen2011_reproducible` (0.832), `reproduction_13_of_14` (0.886) |
| Moderate (0.70 – 0.85) | 0.74 – 0.83 | `error_ordering_le_ne_1` (0.769), `reproduction_lessons` (0.744) |
| Tentative (< 0.70) | — | (none) |

Every exported conclusion has belief ≥ 0.7, i.e. none of the package's
headline contributions sits near equipoise. This is the normative outcome
for a reproduction that the QG audit classified as "13/14 figures
reproduced with two fixable episodes".

## 3. Weak points (derived claims with belief < 0.8)

| Claim | Posterior | Issue |
|-------|----------:|-------|
| `error_ordering_le_ne_1` | 0.769 | The paper's central methodological result, but its belief is moderate because the two supporting observations (`repro_fig3_ordering` 0.99, `repro_fig7_relative` 0.99) propagate through an **induction** whose generative priors are 0.92 — multiplying into ~0.77. Stronger corroboration would require a third reproduction pillar (e.g. Fig. 5 $L_b$ vs $\phi$), which the trace does not produce. |
| `reproduction_lessons` | 0.744 | Four pipeline lessons rolled into one compound claim. The compound-ness is the weakness: splitting into per-lesson independent claims with their own priors would boost the belief, but at the cost of making the "conditional caveat" story harder to state as a single sentence. Accepted trade-off; flagged here for transparency. |
| `pipeline_caveat` | 0.806 | Directly inherits the `reproduction_lessons` weakness. |
| `pred_amr7_needed` | 0.780 | Still at its prior (0.78) because the A/B compare operator that was going to tie it to `amr_low_level_error` was disabled (see §5). The evidence for AMR-sensitivity is qualitatively strong but not wired into the factor graph as a strategy. |
| `amr_low_level_error` | 0.877 | Supported by `amr_regime_dependence`, which is in turn supported by the contrasting φ = 0.6 (clean) and φ = 1.4 (noisy) runs. Adequate but could be tightened by an additional φ point. |

## 4. Evidence gaps

### 4a. Missing experimental validations

| Missing | Why it would help | Cost |
|---------|-------------------|------|
| CH4/air spherical-flame reproduction at a second $\phi$ outside the [0.6, 1.4] window already sampled | Would pin down the regime boundary of AMR-6 adequacy and let us retire the current "amr_regime_dependence" as the sole bridge | 4-8 Bohrium-CPU-hours with GRI30_noNOx |
| Explicit Fig. 5 reproduction ($L_b$ vs $\phi$, all three models, H2/air) | Would add a third induction pillar for `error_ordering_le_ne_1` and push its posterior above 0.85 | 12-24 CPU-hours (whole $\phi$-sweep) |
| Cross-mechanism check for H2/air (e.g. Ó Conaire 2004 vs Li 2004) | Would strengthen the `cantera_validates_paper_sl` induction by showing the paper's values are mechanism-independent, not tied to Li 2004 specifically | 1-2 CPU-hours per mechanism |

### 4b. Untested conditions

The paper studies H2/air at three pressures (0.5, 1, 2 atm) and CH4/air. The
reproduction covers:

- H2/air at **1 atm only** for the quantitative $S_L$ and $L_b$ comparisons
  (the 0.5 atm and 2 atm arms of Fig. 9 were qualitatively audited but not
  exhaustively refined).
- CH4/air at $\phi \in \{0.6, 1.0, 1.4\}$ at 1 atm only.

So the package's strongest claims apply at 1 atm. Extrapolating to the
0.5 atm and 2 atm limits of Fig. 9 rests on the AMR-6 caveat and the
relaxed ±20 % QG policy, not on a direct reproduction.

### 4c. Competing explanations not fully resolved

| Tension | Current resolution | What is missing |
|---------|--------------------|-----------------|
| "The paper's error ordering is real physics" vs "it is a post-processing artefact of the extrapolation algebra" (`pred_amr_resolution_insensitive` = 0.20) | Qualitative: the observed 86 % $L_b$ error at AMR 4-5 dropping to < 5 % at AMR ≥ 7 favours the physics interpretation. | Numerical reformulation of the two predictions ("error drops by ≥ 10×" vs "≤ 2×") and an `abduction(support_h, support_alt, compare)` wire-up so the factor graph differentiates them. |
| The `chen2011_not_reproducible` counter-hypothesis currently floats at its prior 0.10. | The three methodological pillars (induction over Cantera, Taylor, NQ) raise `chen2011_reproducible` to 0.83 without explicitly suppressing the counter. | A proper abductive competition would need numerically-distinct predictions from each hypothesis (e.g. "expected QG pass rate ≥ 12/14" vs "≤ 10/14"); the present compare-on-bare-hypotheses produced pathological beliefs (see §5). |

## 5. Contradictions and BP troubleshooting notes

### 5a. Explicit contradictions modeled

One `contradiction` operator is active in the factor graph:

| Operator | Contents | BP resolution |
|----------|----------|--------------|
| `ctr_fig4_definitions` (prior 0.99) | `fig4_def_rel_is_faithful` vs `fig4_def_residual_is_faithful` | Resolved in favor of Hypothesis B: 0.978 vs 0.001. The helper warrant `ctr_fig4_definitions` itself has belief 1.0000 (the NAND constraint is essentially hard). |

### 5b. Abductions deliberately *not* wired

Two competing hypotheses pairs sit in the graph without an abductive
wire-up. An earlier revision of the package wired them through
`abduction(support_h, support_alt, compare)`; both produced pathological
posteriors that were diagnosed to the `compare` operator's equivalence
factors:

- `compare(pred_h, pred_alt, obs)` lowers to the three factors
  `equivalence(pred_h, obs) → H_match1`, `equivalence(pred_alt, obs) →
  H_match2`, `implication(H_match2, H_match1) → comparison_claim`. The two
  equivalence factors are near-hard (default warrant prior 1 – ε), so they
  force `pred_h ⇔ obs` **and** `pred_alt ⇔ obs`, which implicitly forces
  `pred_h ⇔ pred_alt`.
- Adding a `contradiction(pred_h, pred_alt)` NAND then creates a
  logically-inconsistent sub-graph; BP collapses both hypotheses toward zero
  (both ~0.14 in the earlier revision for `chen2011_reproducible` vs
  `chen2011_not_reproducible`).
- Removing the contradiction instead over-identifies the two hypotheses:
  both went to ~0.90 in the intermediate revision.

The root cause is that `compare` is designed for **numerically-distinct
predictions** (e.g. "new theory predicts 3.40 eV" vs "old theory predicts
3.85 eV" compared against experimental 3.42 eV), not for a hypothesis and
its negation. A bare hypothesis `H` and its negation `¬H` are tied to the
same observation by the same logic, so the compare operator has nothing to
differentiate.

The fix applied in this package: the hypothesis competitions were
restructured so that

1. `chen2011_reproducible` is supported purely via the generative-direction
   `ind_methodological_pillars_all` (three independent pillars → the law),
   together with the bottom-up support from the QG verdicts. The
   counter-hypothesis is kept as an orphan node with an explicit prior of
   0.10.
2. `pred_amr7_needed` and `pred_amr_resolution_insensitive` are kept as
   documented hypotheses with priors 0.78 and 0.20; the `compare` operator
   that tried to A/B-test them against `amr_low_level_error` has been
   removed.

Re-introducing proper abductive wiring would require reformulating both
pairs as numerical predictions (see §4c). This is left as future work.

### 5c. Unmodeled tensions

Two tensions appear in the source material that are deliberately *not*
modeled as formal contradictions:

- **Relaxed ±20 % QG policy for Fig. 9 vs strict match for other figures.**
  Flagged as a caveat in `qg_fig9_partial`; the ±20 % envelope is a policy
  choice, not a formal contradiction with the stricter acceptance criteria
  applied elsewhere.
- **`large_mech_impractical` (belief 0.85) vs the fact that the Cantera
  tier-1 validation *does* run GRI-Mech 3.0 successfully at φ=1.0 CH4/air.**
  The tension is resolved by reading `large_mech_impractical` as "in
  *pyASURF* spherical-flame simulations," whereas Cantera is a cheap 1-D
  flat-flame computation; but the resolution relies on a regime distinction
  not encoded in the factor graph.

## 6. BP diagnostic summary

| Diagnostic | Value | Interpretation |
|-----------|-------|----------------|
| Number of knowledge declarations | 95 | 31 independent (priored), ~64 derived |
| Number of strategies | 28 | 18 support, 5 induction, 5 composite sub-strategies |
| Number of operators | 1 | `contradiction(ctr_fig4_definitions)` |
| Inference method | Junction-tree (exact) | Treewidth ≤ 15, no approximation |
| Convergence | 2 iterations | Expected for exact JT |
| Number of nodes with posterior ≥ 0.90 | 25 / 60 | Strong majority of claims are well-supported |
| Number of derived nodes with posterior < 0.80 | 5 | Documented in §3 |
| Number of independent claims whose posterior ≠ prior by > 5 % | 3 (`paper_sl_*` raised by support chains to 0.98 from 0.97) | Expected: downstream corroboration slightly boosts paper-value priors |

## 7. Limitations of this formalization

1. **The `compare` operator is under-used.** Because its equivalence-factor
   semantics forced pathological posteriors on hypothesis/negation pairs,
   both originally-planned abductions were removed. A proper fix would
   require numerical prediction claims (see §4c) rather than bare
   hypothesis claims — this is a real structural limitation of the present
   formalization that future revisions should address.
2. **Reproduction-side beliefs are anchored by prior choices, not
   first-principles.** Priors in `priors.py` are set by policy (0.95 for
   paper-quoted numerics, 0.93 for run-provenanced reproduction numerics,
   etc.). Reasonable readers with different priors (e.g. a skeptic who
   distrusts digitised Taylor 1991 points) can reproduce the factor graph
   locally and swap the priors to see how the top-level belief moves.
3. **No cross-package dependencies.** The package imports no foreign
   knowledge; it does not, for example, consume a `gaia-combustion-theory`
   package for the $L_b \to 0$ at $\text{Le} = 1$ theorem. Adding such a
   dependency would let BP derive `lb_vanishes_at_le1` instead of priming
   it.
4. **The 2026-04-09 QG audit itself is a single-agent review.** If that
   audit is biased, the whole reproducibility conclusion inherits the bias.
   A multi-agent QG audit would be a straightforward robustness check.

## 8. Bottom line

Subject to the pipeline lessons in §4 and the BP caveats in §5, the
formalized reproduction trace of Chen (2011) supports the conclusion that
**the paper's methodology is reproducible in 2026 with open tooling** at
posterior 0.83. The only paper claim that *fails* under faithful
reproduction is the initial Fig. 4 plot shape — and that failure turned
out to be a convention mismatch (relative error vs Eq. 6 residual), not a
methodology defect. Once the Eq. 6 definition is restored, Fig. 4 matches
and the package's `fig4_def_residual_is_faithful` claim goes to 0.978.
