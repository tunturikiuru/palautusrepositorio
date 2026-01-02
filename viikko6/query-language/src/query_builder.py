from matchers import PlaysInStack, HasAtLeastStack, HasFewerThanStack, AllStack, Or

class QueryBuilder:
    def __init__(self, stack = None):
        if stack is None:
            stack = AllStack()
        self._next = stack

    def build(self):
        return self._next

    def plays_in(self, team):
        return QueryBuilder(PlaysInStack(self._next, team))

    def has_at_least(self, value, attr):
        return QueryBuilder(HasAtLeastStack(self._next, value, attr))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(HasFewerThanStack(self._next, value, attr))
    
    def one_of(self, *queries):
        matchers = [query.build() for query in queries]
        return QueryBuilder(Or(*matchers))