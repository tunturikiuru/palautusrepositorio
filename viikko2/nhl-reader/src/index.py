from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich import print


def main():

    print('Season [magenta][2018-19/2019-2020/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/magenta] [cyan](2024-25)[/cyan]: ', end='')
    season = input()
    valid_seasons = ["2018-19", "2019-2020", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]

    if season not in valid_seasons:
        season = "2024-25"

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = reader.get_nationalities()

    while True:
        print(f'Nationality [magenta][{nationalities}] [/magenta]:', end='')
        nationality = input().upper()
        if nationality == '':
            break
        try:
            players = stats.top_scorers_by_nationality(nationality)

            table = Table(title=f"Season {season} players from {nationality}:")

            table.add_column("player", style="cyan")
            table.add_column("teams", style="magenta")
            table.add_column("goals", style="green")
            table.add_column("assists", style="green")
            table.add_column("points", style="green")

            for player in players:
                table.add_row(str(player.name), str(player.team), str(player.goals), str(player.assists), str(player.goals + player.assists))

            console = Console()
            console.print(table)

        except:
            continue


if __name__ == "__main__":
    main()
