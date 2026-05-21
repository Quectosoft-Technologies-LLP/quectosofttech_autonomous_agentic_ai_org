from dataclasses import dataclass, field

@dataclass
class MetricsRegistry:
    counters: dict[str,int] = field(default_factory=dict)
    def increment(self, name: str, value: int = 1): self.counters[name] = self.counters.get(name,0)+value; return self.counters[name]
    def set_value(self, name: str, value: int): self.counters[name] = value; return value
    def prometheus_text(self):
        lines=[]
        for k in sorted(self.counters):
            safe=k.replace('.','_').replace('-','_'); lines.append(f'# TYPE {safe} counter'); lines.append(f'{safe} {self.counters[k]}')
        return '\n'.join(lines) + ('\n' if lines else '')
