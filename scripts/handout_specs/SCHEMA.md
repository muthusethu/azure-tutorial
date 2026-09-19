# Handout SPEC schema

Each batch file exports `SPECS: dict[int, dict]`.

```python
SPECS[22] = {
    "topic": "Microsoft-hosted vs Self-hosted Agents",
    "subtitle": "Pick the agent like a capacity decision, not a personality trait",
    "phase": "3 - Continuous Integration",
    "tables": [
        {
            "title": "Architecture A — hosted vs self-hosted (same YAML job, different product)",
            "columns": ["Dimension", "Microsoft-hosted", "Self-hosted"],
            "rows": [
                ["YAML", "pool: vmImage: ubuntu-latest", "pool: Default (named pool)"],
                ["Bill", "Hosted minutes + parallel job", "Parallel job PLUS the VM"],
            ],
            "widths": [32, 75, 75],
        },
        {
            "title": "Architecture B — decide with a constraint, not a blog title",
            "columns": ["Constraint", "Default", "Move off hosted when"],
            "rows": [["Private network hop", "Hosted cannot see it", "VNet-only feed / private AKS API"]],
            "widths": [42, 58, 82],
        },
        {
            "title": "Architecture C — pitfalls that queue jobs forever",
            "columns": ["Pitfall", "What you see", "Fix"],
            "rows": [["Capability folklore", "Job waits on 'the Java agent'", "Demand a registered capability"]],
            "widths": [40, 71, 71],
        },
    ],
    "one_liner": "Hosted is Uber. Self-hosted is owning the car — insurance and the 2am flat tyre included.",
    "lab_intro": "Personal Azure DevOps org only. Project azure-100-labs.",
    "lab": [
        "Org settings → Agent pools. List hosted vs self-hosted.",
        "Confirm YAML still uses pool: vmImage: ubuntu-latest.",
    ],
    "code_title": "Starter YAML — hosted stays the default",
    "code": "pool:\n  vmImage: ubuntu-latest\n",
    "checklist": ["Can explain hosted vs self-hosted without saying we wanted control"],
    "tomorrow": "YAML pipeline basics",
}
```

Rules:

- 2 or 3 tables. Prefer Architecture A = map of the system, B = decision, C = failure modes.
- Cells are technically specific (YAML keys, Azure resource types, failure symptoms). No fluff.
- 5–7 lab steps with click paths. Personal subscription / personal Azure DevOps org only.
- `widths` integers millimetres summing to 182.
- `code` is real YAML or Azure CLI, not pseudocode.
- No IBM, no employer, no client names, no Health Check CTA.
