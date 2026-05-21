"""
Safety Agent — Quectosoft Technologies LLP
Author: Subrit Dikshit <subrit@quectosofttech.com>

Cross-cutting safety checks applied to all agent outputs before delivery.
"""
from __future__ import annotations
import subprocess
from pathlib import Path


class SafetyAgent:
    """Runs Bandit + Semgrep on generated code before it enters the repo."""

    def scan_code(self, code_path: str) -> dict:
        results: dict = {"bandit": None, "semgrep": None, "passed": True}
        try:
            bandit = subprocess.run(
                ["bandit", "-r", code_path, "-f", "json", "-q"],
                capture_output=True, text=True
            )
            results["bandit"] = bandit.stdout
            if bandit.returncode != 0:
                results["passed"] = False
        except FileNotFoundError:
            results["bandit"] = "bandit not installed"

        try:
            semgrep = subprocess.run(
                ["semgrep", "--config=auto", code_path, "--json"],
                capture_output=True, text=True
            )
            results["semgrep"] = semgrep.stdout
            if semgrep.returncode not in (0, 1):
                results["passed"] = False
        except FileNotFoundError:
            results["semgrep"] = "semgrep not installed"

        return results
