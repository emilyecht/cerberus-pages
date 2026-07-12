# CERBERUS Pages

Interactive research interface for **CERBERUS: Runtime Independence Budgeting for Layered Assurance in Autonomous Systems**.

This repository presents browser-based explanatory simulations for:

- the matched-model Vigil evidence pipeline;
- pessimistic Failure-Cause Overlap Index (FCOI) evidence;
- asymmetric authority contraction and evidence-gated restoration;
- Structural FCOI minimal-cut-set overlap and near-match reporting;
- the planned Stress Suite v1 scenario families;
- a satellite operations suite covering autonomous collision avoidance, deployment sequencing, and fault recovery during communications loss;
- a communications-blackout survival simulation; and
- a HAL-inspired fictional containment case that tests whether authority separation actually prevents harmful actuation.

## Incident Theatre

Open [`scenarios.html`](scenarios.html) for the satellite operations suite, communications-blackout run, and HAL containment simulation.

The satellite suite makes the mission mapping explicit:

- **Pilot** optimizes maneuvering, deployment, and recovery proposals but has no direct actuator path;
- **Vigil** tracks FCOI pressure, independent sensor agreement, command provenance, and safety-invariant health;
- **Watchdog** applies deterministic mission envelopes before actuation; and
- **Anchor** preserves attitude, power, thermal limits, beaconing, and a safe communications posture whenever authority contracts.

Restoration is sequential and requires sustained fresh independent evidence rather than a one-shot all-clear.

## Evidence boundary

This site is a research communication artifact. It is **not flight software, certification evidence, an operational detector, or a completed safety case**. Browser simulations are illustrative and must not be interpreted as extending the evidence boundary of the CERBERUS v3.5 manuscript or its supplemental roadmap.

The matched-model demonstration is intentionally aligned with its synthetic generator. Its purpose is pipeline verification and reproducibility, not realistic detector validation. Mission-specific authority thresholds require independent engineering and certification.

The satellite cases use illustrative authority thresholds and simplified mission envelopes. They do not establish operational collision-avoidance performance, deployment safety, flight readiness, or validated fault-recovery behavior. The communications-blackout scenario declares an illustrative A2 authority cap during loss of authenticated ground contact. The HAL containment case is an original educational thought experiment: it does not reproduce film dialogue, claim that the fictional system had CERBERUS architecture, or establish real-world validation.

## Local use

Open `index.html` directly, or serve the repository with any static web server:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## Scenario notes

Detailed architecture mapping and non-claims are documented in [`SCENARIO_NOTES.md`](SCENARIO_NOTES.md).

## Research basis

- CERBERUS v3.5 architecture manuscript, July 2026
- CERBERUS White Paper Update: Stress Suite v1 and Structural FCOI Engine v1, July 2026

## Copyright

Copyright © 2026 Emily Echterhoff. All rights reserved. See [`COPYRIGHT.md`](COPYRIGHT.md).
