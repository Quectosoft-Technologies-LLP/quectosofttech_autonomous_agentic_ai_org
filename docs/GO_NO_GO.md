# Go / No-Go

## Go criteria
- Health, readiness, workflow, memory, and RAID staging checks pass.
- Required release assets exist.
- Security workflow, CI workflow, and rollback runbook are present.
- Canary manifest, HPA, PDB, and deployment manifests are present.
- Load validation completes with zero functional errors.

## No-Go criteria
- Missing config catalog, broken runtime boot, unresolved hierarchy links, or failing staging checks.
- Missing rollback instructions or missing deployment manifests.
- Security workflow absent or untriaged blocking findings.
