# Sportsbook Edge Finder (MVP)

This repository contains a starter app for your idea: ingest lines from multiple sportsbooks and highlight where a bettor may have edge.

## What this MVP does

- Normalizes sportsbook lines into a common model (`MarketLine`).
- Converts American odds to implied probability.
- Estimates a market consensus fair probability for each selection.
- Scores each book's line as an edge percentage vs consensus.
- Prints top edges from sample data.

## Why this is useful

If one mainstream sportsbook is slower to move its line, it can present a better number than the rest of the market. This app surfaces those opportunities automatically.

## Run locally

```bash
python -m app.main
```

## Run tests

```bash
pytest -q
```

## Next steps to turn this into a real product

1. **Data ingestion layer**
   - Pull lines from API partners/aggregators (Odds API, Sportradar, etc.) on a schedule.
   - Store snapshots in Postgres for historical analysis.
2. **More robust fair-price engine**
   - Remove vig from two-sided markets before calculating fair probabilities.
   - Blend consensus with your own model probabilities.
3. **User personalization**
   - Let users set min edge %, max stake size, and allowed books.
4. **Alerts and execution speed**
   - Push notifications when edge exceeds threshold.
   - Add stale-line detection and latency monitoring.
5. **Risk and compliance**
   - Geolocation and legal disclaimers by state/country.
   - Responsible gambling settings and limits.

This gives you a foundation for an edge-scanning app while staying simple enough to iterate quickly.
