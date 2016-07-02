from numpy.random import randint, choice, seed
seed(1234)


class player(object):
    def __init__(self, name=None):
        self.name = name
        self.hand = [self.deal(True)]

    def get_sum(self):
        hand_sum = 0
        for num, col in self.hand:
            if col == 'black':
                hand_sum += num
            else:
                hand_sum -= num
        return hand_sum

    def hit(self):
        self.hand.append(self.deal())

    def deal(self, fisrtHand=None):
        if fisrtHand:
            return randint(1, 11), 'black'
        else:
            color = choice(['black', 'red'], p=[1/3, 2/3])
            return randint(1, 11), color


def step(dealer, player, action):
    if action == 'hit':
        player.hit()
        if player.get_sum() > 21 or player.get_sum() < 1:
            return 'terminal', -1
        return (dealer, player), None
    else:
        while dealer.get_sum() < 17:
            dealer.hit()
            if dealer.get_sum() > 21 or dealer.get_sum() < 1:
                return 'terminal', 1
        if dealer.get_sum() == player.get_sum():
            return 'terminal', 0
        elif dealer.get_sum() > player.get_sum():
            return 'terminal', -1
        else:
            return 'terminal', 1


if __name__ == '__main__':

    for i in range(10):
        me = player(name='me')
        dealer = player(name='dealer')

        action = 'hit'
        state, reward = step(dealer, me, action)
        if state is not 'terminal':
            print('round:', i, '\n',
                  state[0].hand, '\n',
                  state[1].hand, '\n', reward)
        while state is not 'terminal':
            action = choice(['hit', 'stick'])
            state, reward = step(state[0], state[1], action)
        if state is not 'terminal':
            print('round:', i, '\n',
                  state[0].hand, '\n',
                  state[1].hand, '\n', reward)
        else:
            print('round:', i, action, '\n',
                  dealer.hand, '\n',
                  me.hand, '\n', reward)
