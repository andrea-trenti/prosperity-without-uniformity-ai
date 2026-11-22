# Mathematical research appendix: formalising the spoken ideas without inventing results

**IMPORTANT:** Everything below is a **model proposed after the recordings to make their questions mathematically testable**. It is **not** a verbatim formula uttered by the author. It contains **no fitted coefficients, external datasets, invented statistical estimates, empirically optimal migration quota, or simulated proof**.

## A. A welfare objective with multiple relevant outcomes

Let `r` index local territories, `i` individuals, `t` time and `p` a policy vector. The recordings ask about prosperity, subjective wellbeing, diversity, administrative quality and safety. One possible **research** definition is:

\[
\max_{p\in\mathcal P} W(p)=\sum_{t=0}^{T}\beta^t\sum_{i=1}^{N_t}\omega_i\,u_i\big(y_{it}(p),s_{it}(p),q_{it}(p),c_{it}(p),e_{it}(p)\big),
\]

where `y` is material living standard, `s` is security, `q` is experienced public-service quality, `c` is the cultural environment and `e` is ecological quality. The parameter `β` discounts future outcomes and `ω_i` assigns welfare weights. **Neither the weights nor the functional form was selected in the voice recordings.** This structure prevents the mistake of claiming that GDP alone measures the social objective.

Diversity can enter through individuals' own utility from cultural opportunities and local traditions, rather than through a scientifically ungrounded rule that more diversity is *always* better. An alternative is to treat cultural continuity as a constraint or as a second independent objective. These choices are **normative**, not identified from the audio.

## B. A two-objective question, without assuming the optimum is the average

Define two indexes on a common scale:

- `H(p)`: a clearly specified welfare outcome under policy `p`;
- `D(p)`: a clearly specified measure of valuable diversity under policy `p`.

The theoretical problem is:

\[
\max_{p\in\mathcal P} \big(H(p),D(p)\big),
\]

under institutional, budgetary, legal and rights-based feasibility constraints. The result generally is a **Pareto frontier**, not a single optimum. Policy `p_a` dominates `p_b` if both its welfare and its diversity scores are at least as high, with one strictly higher.

A scalarised illustration is:

\[
J_{\lambda}(p)=H(p)+\lambda D(p),\quad \lambda\geq 0.
\]

But **λ is not known**. If preserving diversity is understood as part of subjective wellbeing rather than a separate independent end, adding it independently could double-count its effects. The author's preference for an «intermediate» position does **not** establish that the mathematical optimum lies at the arithmetic midpoint of two extremes.

## C. Why 5%, 10% or 15% cannot yet be an estimated optimum

A migration share must have a denominator. Two non-equivalent measures are:

\[
m_{rt}=\frac{\text{new arrivals during period }t}{\text{resident population at start of period }t},
\qquad
z_{rt}=\frac{\text{residents satisfying a stated stock criterion}}{\text{total residents at }t}.
\]

`m` is a **flow ratio**, while `z` is a **stock share**. Citizenship, birth country, legal status and cultural integration would also produce distinct stock definitions. The recorded intuitive percentages have **no unambiguous identification with these variables**.

Even if a policy share `m` were defined, the claim that an optimum is interior would require a credible outcome function. For example:

\[
H(m)=a+b m-cm^2,\qquad c>0
\]

has an unconstrained stationary point at `m*=b/(2c)` only under the **hypothetical assumptions** of that functional form and stable positive parameters. If `c=0`, the result changes; if cultural, housing or individual-rights costs are omitted, the result is incomplete. Without observed outcomes, estimates, identification and a feasible policy domain, **there is no numerical optimum**.

## D. Diversity must be measured by dimension

Let each area `r` have a vector:

\[
\mathbf d_{rt}=\big(d^{\mathrm{language}}_{rt}, d^{\mathrm{traditions}}_{rt},
 d^{\mathrm{products}}_{rt}, d^{\mathrm{institutions}}_{rt}, d^{\mathrm{ecology}}_{rt}\big).
\]

Different empirical questions require different measures. Within-area variety and **between-area distinctiveness** are not the same: two cities may each offer more cuisines while becoming more similar to each other. An optional between-area distance index is:

\[
D_t^{\mathrm{between}}=\frac{2}{R(R-1)}\sum_{r<k}\delta\big(\mathbf d_{rt},\mathbf d_{kt}\big),
\]

where `δ` is a carefully selected distance metric. This formalises, but does **not verify**, the recorded concern that Modena and Bologna may become less recognisably different.

One must also define whether a higher `D` corresponds to **valuable pluralism** or simply any difference whatsoever. The author clearly distinguishes positive and harmful differences in V04.

## E. Learning from the best without copying mechanically

For an administrative unit `r`, define an outcome vector `\mathbf k_r` (for example: reliability, response time, compliance, quality and cost), and a context vector `\mathbf x_r` (needs, scale, institutional constraints). A transfer policy could be evaluated as:

\[
\Delta_r=\operatorname{Outcome}_r(\text{adapted practice})
       -\operatorname{Outcome}_r(\text{status quo}).
\]

The audio suggests benchmarking the top **20–30%**, but it does not supply a ranking criterion. A serious study must choose one and account for differences in caseload, economic structure, demographics and law. A policy trial could compare changes before and after adoption with a credible comparison group; **none has yet been performed** in this source-only dossier.

The most important mathematical distinction is between the *best observed outcome* and its *causal explanation*. A high-performing country is not evidence that every one of its institutions should be transplanted wholesale.

## F. Adapting external innovation instead of simply cloning

Let `K_{r,t}` represent a body of local practices and know-how, and `I_{r,t}` incoming external knowledge. A conceptual dynamic is:

\[
K_{r,t+1}=K_{r,t}+A_r(I_{r,t},K_{r,t})-L_{r,t},
\]

where `A_r` is locally adapted learning and `L` is abandonment of earlier practices. The audio's iPhone metaphor motivates the distinction between **adoption** and **adaptation**. It does not specify, and this appendix does not estimate, the functions or coefficients.

## G. Direct democracy: a design specification is not an efficacy result

The spoken proposal mentions a consultation frequency of roughly **one event every 14–21 days**, multiple alternatives (approximately **three or four**) and elected legislatures responsible for drafting and operational detail. A research implementation would need to specify:

\[
\operatorname{Decision}_t=F(\text{eligible voters},\text{ballots},\text{options},\text{aggregation rule},\text{legal constraints}).
\]

`F` is **not given in the audio**. Neither are how votes become binding, how options are written, the treatment of abstention or how secret, equal and secure participation would be protected. None should be portrayed as solved.

## H. A proper empirical programme (not yet executed)

| Spoken question | Needed measurement | Validation problem |
|---|---|---|
| Are territories losing recognisable identity? | Consistent local cultural indicators over time | Identifying genuine change rather than better measurement |
| Does integration raise wellbeing? | Individual wellbeing before/after credible exposure variation | Reverse causality, selection into mobility |
| Can cultural continuity coexist with economic growth? | Welfare and between-region diversity over time | Confounding by technology and institutions |
| Do better-administered places offer portable solutions? | Comparable public-service outcomes and reform histories | Different local conditions |
| Does more municipal responsibility improve service response? | Decision authority, complaint resolution, cost and quality | Selection of better-governed municipalities |
| Do direct digital votes improve representation? | Turnout, accessibility, policy stability, legitimacy | Design differences and selection |
| Can market integration create innovation without uniformity? | Product differentiation and local knowledge creation | Multiple simultaneous drivers |

**Mathematical integrity rule:** All equations are proposed research *notations*. They are not completed analyses, validated welfare functions, or established optimal thresholds. They must never be presented as words or numbers actually calculated by the speaker.

## Key takeaways

The essential mathematical requirement is **to define variables before seeking an optimum**. The present archive supports the questions, thought experiments and preferences, not a parameterised model. A Pareto frontier is possible; a universal numerical «middle» is not implied. Demographic ratios, cultural continuity and quality of integration must be operationalised separately.

## Further analytical questions

Which indices can jointly measure intra-city variety and inter-city distinctiveness? Does an individual's welfare already incorporate their cultural preferences, making extra weights redundant? Can a credible quasi-experiment identify the causal effects of administrative decentralisation? When might two policies have equal measured economic benefits but very different local cultural consequences?
