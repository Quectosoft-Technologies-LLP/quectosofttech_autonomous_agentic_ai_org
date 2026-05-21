# Load Testing

Current staging validator:
- 40 concurrent threads
- Exercises health, access-approval, memory write/read, and RAID evaluate
- Captures p95 latency and error count

Promotion rule:
- Zero functional errors required
- Review p95 latency regressions before production promotion
