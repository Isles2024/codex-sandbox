"""Core utilities for spotting betting edges across sportsbooks."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class MarketLine:
    """A single market line from one sportsbook."""

    sportsbook: str
    event: str
    market: str
    selection: str
    american_odds: int


@dataclass(frozen=True)
class EdgeResult:
    """Computed edge for a single line."""

    line: MarketLine
    implied_probability: float
    fair_probability: float
    edge_percent: float


def american_to_implied_probability(american_odds: int) -> float:
    """Convert American odds to implied probability.

    Examples:
    -110 -> 52.38%
    +150 -> 40.00%
    """

    if american_odds == 0:
        raise ValueError("american_odds cannot be 0")

    if american_odds > 0:
        return 100 / (american_odds + 100)

    return abs(american_odds) / (abs(american_odds) + 100)


def _group_key(line: MarketLine) -> tuple[str, str, str]:
    return (line.event, line.market, line.selection)


def compute_edges(lines: Iterable[MarketLine]) -> list[EdgeResult]:
    """Compute edge for each line relative to market consensus.

    Consensus is the simple average implied probability across books
    for the same (event, market, selection).
    """

    grouped: dict[tuple[str, str, str], list[MarketLine]] = {}
    for line in lines:
        grouped.setdefault(_group_key(line), []).append(line)

    results: list[EdgeResult] = []
    for group_lines in grouped.values():
        probabilities = [american_to_implied_probability(l.american_odds) for l in group_lines]
        fair_probability = sum(probabilities) / len(probabilities)

        for line, implied_probability in zip(group_lines, probabilities, strict=True):
            edge_percent = (fair_probability - implied_probability) * 100
            results.append(
                EdgeResult(
                    line=line,
                    implied_probability=implied_probability,
                    fair_probability=fair_probability,
                    edge_percent=edge_percent,
                )
            )

    return sorted(results, key=lambda r: r.edge_percent, reverse=True)


def best_edges(lines: Iterable[MarketLine], min_edge_percent: float = 1.0) -> list[EdgeResult]:
    """Return only lines with a positive edge over the threshold."""

    return [result for result in compute_edges(lines) if result.edge_percent >= min_edge_percent]
