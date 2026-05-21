from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml
from jsonschema import Draft7Validator

@dataclass
class ValidationIssue:
    file: str
    agent_id: str
    level: str
    message: str
    path: str

@dataclass
class AgentCard:
    id: str
    path: Path
    data: Dict[str, Any]

class AgentLoader:
    def __init__(self, schema_path: str | Path, catalog_root: str | Path):
        self.schema_path = Path(schema_path)
        self.catalog_root = Path(catalog_root)
        self.schema = yaml.safe_load(self.schema_path.read_text(encoding='utf-8'))
        self.validator = Draft7Validator(self.schema)
    def iter_card_paths(self):
        yield from sorted(self.catalog_root.rglob('*.yaml'))
    def load_all(self, strict: bool = True) -> Dict[str, AgentCard]:
        cards = {}
        for p in self.iter_card_paths():
            data = yaml.safe_load(p.read_text(encoding='utf-8'))
            errs = list(self.validator.iter_errors(data))
            if strict and errs:
                raise ValueError(errs[0].message)
            cards[data['id']] = AgentCard(id=data['id'], path=p, data=data)
        return cards
    def validate_all(self) -> List[ValidationIssue]:
        issues = []
        for p in self.iter_card_paths():
            data = yaml.safe_load(p.read_text(encoding='utf-8'))
            for err in self.validator.iter_errors(data):
                issues.append(ValidationIssue(str(p), str(data.get('id','<missing>')), 'ERROR', err.message, '.'.join(str(x) for x in err.path) or '<root>'))
        return issues
    def validate_relationships(self, cards: Optional[Dict[str, AgentCard]] = None) -> List[ValidationIssue]:
        cards = cards or self.load_all(strict=False)
        ids = set(cards.keys())
        issues = []
        for card in cards.values():
            for field in ('reportsto','escalationto'):
                value = card.data.get(field)
                if not value or value in ids or value in {'shareholders','board','human_operator','human'}:
                    continue
                issues.append(ValidationIssue(str(card.path), card.id, 'WARN', f'unresolved {field}: {value}', field))
        return issues
