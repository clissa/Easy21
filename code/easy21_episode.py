def main():
    """
    Simulate one entire episode of Easy21 game.
    :return: Final reward
    """
    import os
    import sys
    sys.path.append(os.getcwd() + "/code")

    import random
    from easy21_utils import step, State, policy

    # initialize the state
    state = State()
    print("Dealer started with {} and Player started with {}.".format(state.dealer_score, state.player_score))
    print("--"*30)

    # loop until the next_state is terminal
    while state != "terminal":
        # sample the action
        action = policy(s=state)

        state, reward = step(s=state, a=action)

    print("The final reward is {}".format(reward))
    print("--"*30)



if __name__ == "__main__":
    import sys
    n_episodes = int(sys.argv[1])
    for i in range(n_episodes):
        print("\nEPISODE {}:".format(i+1))
        main()

