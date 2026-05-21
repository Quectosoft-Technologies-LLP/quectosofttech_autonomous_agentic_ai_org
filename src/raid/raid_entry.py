from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime, timezone

class RAIDEntry(BaseModel):
    entry_id: str
    agent_id: str
    task_id: str
    raid_type: Literal['RISK','ASSUMPTION','ISSUE','DEPENDENCY']
    title: str
    description: str
    likelihood: int = Field(ge=1, le=5)
    impact: int = Field(ge=1, le=5)
    category: str = 'GENERAL'
    status: str = 'OPEN'
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    @property
    def severity_score(self) -> int:
        return self.likelihood * self.impact
