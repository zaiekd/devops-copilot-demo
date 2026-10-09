from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BuildResult:
    status: str
    summary: str


def parse_build_log(log: str) -> BuildResult:
    """Parse a tiny CI log and return a simplified build status."""
    normalized = log.lower()
    if "failed" in normalized or "error" in normalized:
        return BuildResult(status="failed", summary="The build log contains a failure marker.")
    return BuildResult(status="passed", summary="No failure marker found.")

