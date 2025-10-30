from player_reader import PlayerReader
from player_stats import PlayerStats
from rich_output import get_season, get_nationality, print_stats

def loop(stats, nationalities, season):
    # aivan turha, mutta pylint vaatii
    while True:
        nationality = get_nationality(nationalities)
        if nationality == "":
            break
        if nationality not in nationalities:
            continue
        players = stats.top_scorers_by_nationality(nationality)
        print_stats(players, season, nationality)

def main():
    season = get_season()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = reader.get_nationalities()

    loop(stats, nationalities, season)

if __name__ == "__main__":
    main()
