# CERBERUS Pages

Interactive research interface for **CERBERUS: Runtime Independence Budgeting for Layered Assurance in Autonomous Systems**.

This repository presents browser-based explanatory simulations for:

- the matched-model Vigil evidence pipeline;
- pessimistic Failure-Cause Overlap Index (FCOI) evidence;
- asymmetric authority contraction and evidence-gated restoration;
- Structural FCOI minimal-cut-set overlap and near-match reporting; and
- the planned Stress Suite v1 scenario families.

## Evidence boundary

This site is a research communication artifact. It is **not flight software, certification evidence, an operational detector, or a completed safety case**. Browser simulations are illustrative and must not be interpreted as extending the evidence boundary of the CERBERUS v3.5 manuscript or its supplemental roadmap.

The matched-model demonstration is intentionally aligned with its synthetic generator. Its purpose is pipeline verification and reproducibility, not realistic detector validation. Mission-specific authority thresholds require independent engineering and certification.

## Local use

Open `index.html` directly, or serve the repository with any static web server:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## Research basis

- CERBERUS v3.5 architecture manuscript, July 2026
- CERBERUS White Paper Update: Stress Suite v1 and Structural FCOI Engine v1, July 2026

## Copyright

Copyright © 2026 Emily Echterhoff. All rights reserved. See [`COPYRIGHT.md`](COPYRIGHT.md).
