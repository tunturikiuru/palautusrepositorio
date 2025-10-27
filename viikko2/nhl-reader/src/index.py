import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    filtered_players = filter(lambda x: x.nationality == 'FIN', players)
    sorted_players = sorted(filtered_players, key=lambda player: player.goals + player.assists, reverse=True)

    print("Players from FIN: \n")

    for player in sorted_players:
        print(player)


if __name__ == "__main__":
    main()
