from dataclasses import dataclass

@dataclass
class TraceExporter:
    backend: str = 'otlp'
    endpoint: str = 'http://otel-collector:4318'
    enabled: bool = True

    def config(self):
        return {'backend': self.backend, 'endpoint': self.endpoint, 'enabled': self.enabled}
