from app.edge_finder import (
    MarketLine,
    american_to_implied_probability,
    best_edges,
    compute_edges,
)


def test_american_probability_conversion():
    assert round(american_to_implied_probability(-110), 4) == 0.5238
    assert round(american_to_implied_probability(+150), 4) == 0.4


def test_compute_edges_orders_by_edge_descending():
    lines = [
        MarketLine("A", "Game 1", "moneyline", "Home", +150),
        MarketLine("B", "Game 1", "moneyline", "Home", +140),
        MarketLine("C", "Game 1", "moneyline", "Home", +130),
    ]

    results = compute_edges(lines)

    assert results[0].line.sportsbook == "A"
    assert results[-1].line.sportsbook == "C"


def test_best_edges_filters_threshold():
    lines = [
        MarketLine("A", "Game 2", "moneyline", "Away", +170),
        MarketLine("B", "Game 2", "moneyline", "Away", +150),
        MarketLine("C", "Game 2", "moneyline", "Away", +130),
    ]

    filtered = best_edges(lines, min_edge_percent=2.0)
    assert len(filtered) == 1
    assert filtered[0].line.sportsbook == "A"
