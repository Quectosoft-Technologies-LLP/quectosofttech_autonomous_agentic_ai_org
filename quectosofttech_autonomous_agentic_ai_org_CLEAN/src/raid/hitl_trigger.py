class HITLTrigger:
    def channels_for(self, action: str):
        if action == 'HUMAN_HITL': return ['slack','email']
        if action == 'CSUITE_GATE': return ['slack']
        return []
