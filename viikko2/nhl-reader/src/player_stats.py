import player_reader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def nationalities(self):
        nationalities = {player.nationality for player in self.players}
        return "/".join(nationalities)


    def top_scorers_by_nationality(self, nationality):
        player_list = filter(lambda player: player.nationality == nationality, self.players)
        sorted_players = sorted(player_list, reverse = True, key= lambda player: player.goals + player.assists)
        return sorted_players
