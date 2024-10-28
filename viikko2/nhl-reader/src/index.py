import player
from rich import print
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    season = get_season()
    if season == "":
        return
    url = f'https://studies.cs.helsinki.fi/nhlstats/{season}/players'
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.nationalities()
    print_stats(stats, nationalities, season)


def get_season():
    print("[italic]NHL statistics by nationality[/italic]\n")
    while True:
        print("Select season [bold magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/bold magenta]:")
        season = input()
        if season == "":
            return ""
        if season == "2018-19" or "2019-20" or "2020-21" or "2021-22" or "2022-23" or "2023-24" or "2024-25":
            return season

def print_stats(stats, nationalities, season):
    while True:
        print(f'Select nationality [bold magenta][{nationalities}][/bold magenta]:')
        nationality = input()
        if nationality == "":
            break
        players = stats.top_scorers_by_nationality(nationality)
        print_table(players, nationality, season)


def print_table(players, nationality, season):
    table = Table(title=f"Top scorers of {nationality} season {season}")
    table.add_column("name", justify="left", style="cyan")
    table.add_column("team", justify="left", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))
    
    print(table)


if __name__ == "__main__":
    main()
