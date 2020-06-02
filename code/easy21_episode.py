def main():
    """
    Simulate one entire episode of Easy21 game.
    :return: Final reward
    """
    import os
    import sys
    sys.path.append(os.getcwd() + "/code")

    import random
    from easy21_utils import step

    # sample inital cards
    dealer_card = random.sample(range(1, 11), 1)[0]
    player_card = random.sample(range(1, 11), 1)[0]

    # initialize the state
    initial_state = (dealer_card, player_card)
    print("Dealer started with {},\nwhile player started with {}.".format(dealer_card, player_card))

    # loop until the next_state is terminal
    next_state = initial_state
    while next_state != "terminal":
        # sample the action
        # TODO implement policy function that returns directly the action
        if next_state[1] < 17:
            action = "hit"
        else:
            action = "stick"

        next_state, reward = step(s=next_state, a=action)
        if next_state != "terminal":
        print("Dealer score  = {}; Player score = {}".format(next_state[0], next_state[1]))

    print("The final reward is {}\n\n".format(reward))



if __name__ == "__main__":
    main()