import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.players = self.get_players(url)

    def get_players(self, url):
        response = requests.get(url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return list(players)