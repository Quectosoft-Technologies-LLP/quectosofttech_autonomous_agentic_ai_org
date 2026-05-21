from dataclasses import dataclass
from pathlib import Path

@dataclass
class AppSettings:
    repo_root: Path
    data_dir: Path
    db_path: Path
    log_dir: Path
    @classmethod
    def from_repo_root(cls, repo_root: str | Path):
        repo_root = Path(repo_root).resolve()
        data_dir = repo_root / 'data'; data_dir.mkdir(parents=True, exist_ok=True)
        log_dir = repo_root / 'logs'; log_dir.mkdir(parents=True, exist_ok=True)
        return cls(repo_root, data_dir, data_dir / 'runtime.db', log_dir)
