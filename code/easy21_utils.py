class State:
    """ Class for representing any state of the Easy21 environment """

    def __init__(self):
        import random
        self.dealer_score = random.randint(1, 10)
        self.player_score = random.randint(1, 10)


def sample_card(n):
    """
    Sample n cards according to the rules of Easy21
    :param n: number of cards to draw
    :return: tuple with card and color
    """
    import random
    import pandas as pd

    p_red = 1 / 3  # p_black = 1 - p_red = 2/3

    # sample card
    values = [random.randint(1, 10) for i in range(n)]

    # sample color
    colors = [(i, "red") if random.random() < p_red else (i, "black") for i in range(n)]

    sampled_cards = pd.DataFrame(data={"value": values, "color": colors})
    return sampled_cards


def step(s, a):
    """
    Simulate one step of the environment given the initial state and the Player's action.
    :param s: State object containing Dealers first card and Player's sum (1 to 21)
    :param a: Player's action (either hit or stick)
    :return: tuple with next state and reward
    """
    # input checks
    if s.dealer_score < 1 or s.dealer_score > 10:
        raise ValueError("Invalid input argument for Dealer's initial score: must be an integer between 1 and 10.")
    if s.player_score < 1 or s.player_score > 21:
        raise ValueError("Invalid input argument for Player's initial score: must be an integer between 1 and 21.")
    if a not in ["hit", "stick"]:
        raise ValueError("Invalid input argument for Player's action: specify one between \"hit\" or \"stick\".")

    if a == "hit":
        # sample the next card
        card = sample_card(1)

        # update the sum
        if card.loc[0, "color"] == "black":
            s.player_score += card.loc[0, "value"]
        else:
            s.player_score -= card.loc[0, "value"]

        # compute the reward
        if s.player_score < 1 or s.player_score > 21:
            reward = -1
            print("Game finished with scores:\nDealer: {};\tPlayer: {}\n"
                  "The Player went bust.\n".format(s.dealer_score, s.player_score))
            state = "terminal"
        else:
            reward = 0
            state = s
    else:
        # roll Dealer's trajectory
        while 1 <= s.dealer_score < 17:
            card = sample_card(1)
            if card.loc[0, "color"] == 'black':
                s.dealer_score += card.loc[0, "value"]
            else:
                s.dealer_score -= card.loc[0, "value"]

        # compute the reward
        if s.dealer_score < 1 or s.dealer_score > 21:
            reward = 1
            print("Game finished with scores:\nDealer: {};\tPlayer: {}\n"
                  "The Dealer went bust.\n".format(s.dealer_score, s.player_score))
            state = "terminal"
        else:
            if s.player_score > s.dealer_score:
                reward = 1
                print("Game finished with scores:\nDealer: {};\tPlayer: {}\n"
                      "The Player won.\n".format(s.dealer_score, s.player_score))
                state = "terminal"
            elif s.player_score == s.dealer_score:
                reward = 0
                print("Game finished with scores:\nDealer: {};\tPlayer: {}\n"
                      "Draw.\n".format(s.dealer_score, s.player_score))
                state = "terminal"
            else:
                reward = -1
                print("Game finished with scores:\nDealer: {};\tPlayer: {}\n"
                      "The Dealer won.\n".format(s.dealer_score, s.player_score))
                state = "terminal"
    return state, reward


def policy(s, threshold=18):
    """
    Return the Player's action given the current state of the environment.
    :param s: current state
    :return: action (\"hit\" or \"stick\")
    """
    if s.player_score < threshold:
        action = "hit"
    else:
        action = "stick"
    return action
