class MemoryRBACEnforcer:
    def authorize(self, requested_mode: str, granted_mode: str) -> bool:
        return granted_mode == 'write' or requested_mode == granted_mode
