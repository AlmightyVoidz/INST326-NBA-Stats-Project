# main.py
from models.player_metric import PointGuardAssists, CenterAssists, GuardRebounds, BigManRebounds
from evaluator.evaluator import Evaluator
from io.importer import import_csv
from io.exporter import export_csv
from io.persistence import save_data, load_data

def main():
    # Load previously saved data
    data = load_data()

    evaluator = Evaluator()

    # Example: import new players from CSV
    players = import_csv("data/sample_nba.csv")
    for p in players:
        if p["Position"] == "PG":
            evaluator.add_metric(PointGuardAssists(p["Name"], float(p["Assists"])))
        elif p["Position"] == "C":
            evaluator.add_metric(CenterAssists(p["Name"], float(p["Assists"])))
        elif p["Position"] == "G":
            evaluator.add_metric(GuardRebounds(p["Name"], float(p["Rebounds"])))
        else:
            evaluator.add_metric(BigManRebounds(p["Name"], float(p["Rebounds"])))

    results = evaluator.run_all()
    for r in results:
        print(f"{r['player']} - {r['metric']}: {r['rating']} ({r['score']})")

    # Save results for next session
    save_data(results)

    # Optional: export to CSV
    export_csv("data/player_ratings.csv", results)

if __name__ == "__main__":
    main()
