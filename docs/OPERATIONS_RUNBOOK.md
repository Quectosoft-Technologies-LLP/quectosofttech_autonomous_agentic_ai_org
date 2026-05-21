# Operations Runbook

## Health
- Check `/health`, `/ready`, and `/metrics`.
- Confirm `logs/app.log` is updating and `data/runtime.db` is writable.

## Rollback
- Redeploy previous application image tag.
- Restore previous config catalog and database snapshot.
- Re-run smoke validation: health, readiness, access-approval, memory read/write, RAID evaluation.

## Incident response
- Review metrics counters for request volume.
- Inspect recent RAID entries and access decisions.
- Pause high-risk changes when RAID action is `CSUITE_GATE` or `HUMAN_HITL`.
