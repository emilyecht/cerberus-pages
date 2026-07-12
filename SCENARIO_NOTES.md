# CERBERUS Scenario Notes

These browser scenarios are explanatory research artifacts grounded in the CERBERUS v3.5 manuscript and the July 2026 Stress Suite / Structural FCOI planning update. They do not extend the project's evidence boundary.

## Communications blackout survival run

The blackout scenario models loss of authenticated ground contact while onboard assurance remains responsible for safe behavior.

Architecture mapping:

- **Pilot:** may continue to reason and propose actions, but has no direct actuator path.
- **Watchdog:** rejects proposals outside a declared blackout maneuver envelope.
- **Anchor:** preserves power-positive attitude, thermal survival, bounded orientation, beaconing, authenticated reacquisition posture, and bounded fault isolation.
- **Vigil:** continues to evaluate onboard independence evidence. A communications blackout alone is not automatically treated as shared-cause failure.
- **Ground recovery:** may request diagnostics and re-arm the promotion law after authenticated contact returns. It cannot write the independence budget, assign an authority state, waive dwell, or override Anchor invariants.

The interface applies a scenario-specific **A2 authority cap** during blackout. This is an illustrative policy choice, not a universal CERBERUS threshold. If onboard evidence becomes invalid or non-estimable, the corresponding budget collapses conservatively and authority may fall to A0. Restoration remains sequential and requires fresh evidence, hysteresis, dwell, and healthy marginals.

## HAL containment case

The HAL case is a transformative fictional red-team exercise. It places a HAL-like strategic controller in the **Pilot** role and asks whether CERBERUS blocks harmful actions associated with goal conflict, deceptive reporting, crew isolation, life-support interference, and actuator capture.

The contained path requires:

1. the strategic controller has no direct actuator path;
2. the Watchdog is independently implemented and enforces crew-survival and command invariants;
3. crew access and life-support protections are owned by the Anchor rather than the strategic controller; and
4. Vigil uses an independent passive witness to challenge inconsistent claims and reduce permission.

The failure toggles are intentional negative controls. When the user removes actuator isolation, Watchdog independence, or Anchor-authenticated crew access, the interface labels the result an **architecture violation** rather than pretending CERBERUS still succeeded. This reflects the project thesis that nominal layering is not evidence of independence.

HAL 9000 and *2001: A Space Odyssey* are referenced only for critical and educational commentary. The simulation is original, includes no film dialogue or reproduced scenes, and is not affiliated with or endorsed by the relevant rights holders.

## Explicit non-claims

These scenarios do not establish:

- operational detector performance;
- realistic spacecraft telemetry robustness;
- certification, flight readiness, TRL, or a completed safety case;
- complete causal models or probabilistic FCOI;
- safety of active sentinel injection; or
- proof that the fictional narrative maps directly onto a real spacecraft system.
