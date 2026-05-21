from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelSelection:
    provider: str
    model: str
    fallbackprovider: Optional[str]
    fallbackmodel: Optional[str]
    selected: str
    reason: str

class ModelRouter:
    def select_model(self, card: dict, task_risk: str | None = None, override: Optional[dict] = None) -> ModelSelection:
        model = dict(card.get('model', {}))
        if override:
            model.update(override)
        selected = model.get('fallbackmodel') if task_risk == 'high' and model.get('fallbackmodel') else model.get('model', 'unknown')
        reason = 'high_risk_fallback' if task_risk == 'high' and model.get('fallbackmodel') else 'default_card_model'
        return ModelSelection(model.get('provider','unknown'), model.get('model','unknown'), model.get('fallbackprovider'), model.get('fallbackmodel'), selected, reason)
