class Player:
    def __init__(self, player):
        self.name = player['name']
        self.nationality = player['nationality']
        self.assists = player['assists']
        self.goals = player['goals']
        self.team = player['team']
        self.games = player['games']

    def __str__(self):
        return f'{self.name:20} team {self.team:15} {self.goals:3} + {self.assists:3} = {self.goals+self.assists}'
