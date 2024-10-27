import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict)
            players.append(player)

    sorted_players = sorted(players, reverse = True, key= lambda player: player.goals + player.assists)

    print("Players from FIN\n")
    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
