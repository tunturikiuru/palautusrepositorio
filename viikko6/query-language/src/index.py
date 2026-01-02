from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher2 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    matcher3 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    matcher4 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcher5 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("COL"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    query2 = QueryBuilder()
    matcher6 = query2.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()

    query = QueryBuilder()
    matcher7= (
        query
            .one_of(
            query.plays_in("PHI")
                .has_at_least(10, "assists")
                .has_fewer_than(10, "goals"),
            query.plays_in("EDM")
                .has_at_least(50, "points")
            )
            .build()
        )
    
    for player in stats.matches(matcher6):
        print(player)
    print('- '*25)

    for player in stats.matches(matcher7):
        print(player)




if __name__ == "__main__":
    main()
