from dataclasses import dataclass
from pathlib import Path
from .logger import configure_logging, log_event
from .metrics import MetricsRegistry

@dataclass
class ObservabilityService:
    log_dir: Path
    logger_name: str = 'quectosoft_agentic_org'
    def __post_init__(self):
        self.logger = configure_logging(self.log_dir); self.metrics = MetricsRegistry()
    def record(self, event_type: str, metric_name: str | None = None, **payload):
        if metric_name: self.metrics.increment(metric_name)
        log_event(self.logger, event_type, **payload)
