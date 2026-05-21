from dataclasses import dataclass

@dataclass
class MitigationPlan:
    entry_id: str
    actions: list[str]

class MitigationEngine:
    def suggest(self, raid_entry, raid_config: dict):
        return MitigationPlan(raid_entry.entry_id, list(raid_config.get('autonomousmitigations', [])))
