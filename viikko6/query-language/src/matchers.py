class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class All:
    def __init__(self):
        pass

    def test(self, player):
        return True
    
class Not:
    def __init__(self, condition):
        self._condition = condition

    def test(self, player):
        return not self._condition.test(player)
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._atrr = attr

    def test(self, player):
        player_value = getattr(player, self._atrr)
        return player_value < self._value
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False
    





    
class AllStack():
    def __init__(self):
        pass

    def test(self, player):
        return True
    
    def push(self, stack):
        stack.push(AllStack())
    

class PlaysInStack:
    def __init__(self, stack, team):
        self._stack = stack
        self._team = team

    def test(self, player):
        if player.team != self._team:
            return False
        return self._stack.test(player)


class HasAtLeastStack:
    def __init__(self, stack, value, attr):
        self._stack = stack
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        if player_value < self._value:
            return False
        return self._stack.test(player)


class HasFewerThanStack:
    def __init__(self, stack, value, attr):
        self._stack = stack
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        if player_value >= self._value:
            return False
        
        return self._stack.test(player)

