from app.edge_finder import best_edges
from app.sample_data import SAMPLE_LINES


def main() -> None:
    print("Top detected edges (sample data):")
    for result in best_edges(SAMPLE_LINES, min_edge_percent=0.5):
        print(
            f"- {result.line.event} | {result.line.selection} @ {result.line.sportsbook} "
            f"{result.line.american_odds:+d} | edge={result.edge_percent:.2f}%"
        )


if __name__ == "__main__":
    main()
