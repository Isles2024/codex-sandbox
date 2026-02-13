"""Sample lines to demonstrate the edge-finding workflow."""

from app.edge_finder import MarketLine

SAMPLE_LINES = [
    MarketLine("DraftKings", "LAL vs BOS", "moneyline", "LAL", +140),
    MarketLine("FanDuel", "LAL vs BOS", "moneyline", "LAL", +155),
    MarketLine("BetMGM", "LAL vs BOS", "moneyline", "LAL", +150),
    MarketLine("Caesars", "LAL vs BOS", "moneyline", "LAL", +145),
    MarketLine("DraftKings", "LAL vs BOS", "moneyline", "BOS", -162),
    MarketLine("FanDuel", "LAL vs BOS", "moneyline", "BOS", -170),
    MarketLine("BetMGM", "LAL vs BOS", "moneyline", "BOS", -165),
    MarketLine("Caesars", "LAL vs BOS", "moneyline", "BOS", -160),
]
