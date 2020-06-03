def run_episode():
    """
    Simulate one entire episode of Easy21 game.
    :return: Final reward
    """
    import os
    import sys
    sys.path.append(os.getcwd() + "/code")

    import pandas as pd
    from easy21_utils import step, State, policy

    # initialize the state
    state = State()

    # initialize history DataFrame for tracking the episode evolution
    history = pd.DataFrame(
        data={"dealer_score": [state.dealer_score], "player_score": [state.player_score], "reward": [0]})

    print("Dealer started with {} and Player started with {}.".format(state.dealer_score, state.player_score))
    print("--" * 30)

    # loop until the next_state is terminal
    while state != "terminal":
        # sample the action
        action = policy(s=state)

        # simulate the environment
        new_state, reward = step(s=state, a=action)

        # update history
        state_df = pd.DataFrame(
            data={"dealer_score": [state.dealer_score], "player_score": [state.player_score], "reward": [reward]})
        history = history.append(state_df, ignore_index=True)

        # override old state
        state = new_state

    print("The final reward is {}".format(reward))
    print("--" * 30)

    return history


if __name__ == "__main__":
    import sys
    from pathlib import Path

    n_episodes = int(sys.argv[1])

    if len(sys.argv) > 2:
        save_path = Path(sys.argv[2])
    else:
        save_path = Path("./episodes")
    save_path.mkdir(parents=True, exist_ok=True)

    for i in range(n_episodes):
        print("\nEPISODE {}:".format(i + 1))
        history = run_episode()
        outpath = save_path / "episode{}.csv".format(i + 1)
        history.to_csv(outpath, index_label="time")
