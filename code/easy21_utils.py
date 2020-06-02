def sample_card(n):
    """Sample n cards according to the rules of Easy21

    :param n: number of cards to draw
    :return: tuple with card and color
    """
    import random
    import pandas as pd

    p_red = 1/3  # p_black = 1 - p_red = 2/3

    # sample card
    values = random.sample(range(1, 11), n)

    # sample color
    colors = ["red" if random.random() < p_red else "black" for i in range(n)]

    sampled_cards = pd.DataFrame(data={"value": values, "color": colors})
    return sampled_cards


def step(s, a):
    """ Simulate one step of the environment given the initial state and the player's action.

    :param s: tuple with dealers first card and player's sum (1 to 21)
    :param a: player's action (either hit or stick)
    :return: tuple with next state and reward
    """
    dealer_score = s[0]
    player_score = s[1]

    # input checks
    if dealer_score < 1 or dealer_score > 10:
        print("Problem here0")
        raise ValueError("Invalid input argument for dealer's initial score: must be an integer between 1 and 10.")
    if player_score < 1 or player_score > 21:
        print("Problem here1")
        raise ValueError("Invalid input argument for player's initial score: must be an integer between 1 and 21.")
    if a not in ["hit", "stick"]:
        print("Problem here2")
        raise ValueError("Invalid input argument for player's action: specify one between \"hit\" or \"stick\".")

    if a == "hit":
        # sample the next card
        card = sample_card(1)

        # update the sum
        if card.loc[0, "color"] == "black":
            player_score += card.loc[0, "value"]
        else:
            player_score -= card.loc[0, "value"]

        # compute the reward
        if player_score < 1 or player_score > 21:
            reward = -1
        else:
            reward = 0

        # update the next state
        if reward > -1:
            next_state = (s[0], player_score)
        else:
            next_state = "terminal"
    else:
        # roll dealer's trajectory
        while 1 <= dealer_score < 17:
            card = sample_card(1)
            if card.loc[0, "color"] == 'black':
                dealer_score += card.loc[0, "value"]
            else:
                dealer_score -= card.loc[0, "value"]

        # compute the reward
        if dealer_score < 1 or dealer_score > 21:
            reward = 1
        else:
            if player_score > dealer_score:
                reward = 1
            elif player_score == dealer_score:
                reward = 0
            else:
                reward = -1

        # update the next state as terminal
        next_state = "terminal"

    return next_state, reward
