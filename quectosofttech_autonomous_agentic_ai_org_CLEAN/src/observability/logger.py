import json, logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def configure_logging(log_dir):
    log_dir = Path(log_dir); log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger('quectosoft_agentic_org'); logger.setLevel(logging.INFO)
    if not logger.handlers:
        h = RotatingFileHandler(log_dir / 'app.log', maxBytes=1_000_000, backupCount=3); h.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s')); logger.addHandler(h)
    return logger

def log_event(logger, event_type, **payload):
    logger.info(json.dumps({'event_type': event_type, **payload}, sort_keys=True))
