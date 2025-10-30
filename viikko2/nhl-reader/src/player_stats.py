class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda x: x.nationality == nationality, self.players)
        sorted_players = sorted(filtered_players, key=lambda x: x.goals + x.assists, reverse=True)
        return list(sorted_players)
