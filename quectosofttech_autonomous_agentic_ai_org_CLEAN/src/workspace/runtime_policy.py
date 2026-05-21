from dataclasses import dataclass

@dataclass
class RuntimePolicy:
    run_as_non_root: bool = True
    allow_privilege_escalation: bool = False
    network_policy: str = 'default-deny'
    filesystem_mode: str = 'read-write-workdir'
    seccomp_profile: str = 'runtime/default'

    def as_dict(self):
        return {
            'run_as_non_root': self.run_as_non_root,
            'allow_privilege_escalation': self.allow_privilege_escalation,
            'network_policy': self.network_policy,
            'filesystem_mode': self.filesystem_mode,
            'seccomp_profile': self.seccomp_profile,
        }
