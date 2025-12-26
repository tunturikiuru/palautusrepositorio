class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player):
        if player == self.player1:
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            return self.draw()
        if max(self.score1, self.score2) >= 4:
            return self.victory()
        return self.ongoing()

    def draw(self):
        l = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        if self.score1 < 3:
            return l[self.score1]
        return l[3]

    def victory(self):
        if self.score1 > self.score2:
            return "Advantage player1" if self.score1 == self.score2 +1 else "Win for player1"
        return "Advantage player2" if self.score2 == self.score1 +1 else "Win for player2"

    def ongoing(self):
        l = ["Love", "Fifteen", "Thirty", "Forty"]
        return f'{l[self.score1]}-{l[self.score2]}'

