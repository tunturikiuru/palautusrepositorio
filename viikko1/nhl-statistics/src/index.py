from player_reader import PlayerReader
from statistics_service import StatisticsService, SortBy


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = StatisticsService(reader)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print()  

    print("Top point getters:")
    for player in top_scorers:
        print(player)
    
    print("- - - - - - - - -")

    print("Top point getters:")
    for player in stats.top(5, SortBy.POINTS):
        print(player)

    print()
    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(5):
        print(player)

    print()
    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(5, SortBy.GOALS):
        print(player)

    print()
    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(5, SortBy.ASSISTS):
        print(player)


if __name__ == "__main__":
    main()