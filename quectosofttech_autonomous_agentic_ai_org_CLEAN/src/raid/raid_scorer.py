from dataclasses import dataclass

@dataclass
class RAIDScore:
    likelihood: int
    impact: int
    score: int
    zone: str

class RAIDScorer:
    def score(self, likelihood: int, impact: int) -> RAIDScore:
        score = int(likelihood) * int(impact)
        if score <= 6:
            zone = 'LOW'
        elif score <= 12:
            zone = 'MEDIUM'
        elif score <= 19:
            zone = 'HIGH'
        else:
            zone = 'CRITICAL'
        return RAIDScore(likelihood=likelihood, impact=impact, score=score, zone=zone)
