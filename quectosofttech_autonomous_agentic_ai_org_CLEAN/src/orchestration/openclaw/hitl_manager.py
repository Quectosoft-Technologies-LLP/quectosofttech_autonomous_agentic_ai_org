from dataclasses import dataclass
from typing import List

@dataclass
class HITLEvent:
    reason: str
    channels: List[str]
    status: str = 'triggered'

class HITLManager:
    def trigger(self, reason: str, channels: List[str]) -> HITLEvent:
        return HITLEvent(reason, channels)
