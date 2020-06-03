def MC_policy_evaluation(policy, MC_type):
    pass


def mc_state_policy_evaluation(state, mc_type, episodes_path):
    """
    Evaluate a policy using final-update Monte Carlo for the specified state reading episodes from .csv files.
    :param state: the state for which the value function is computed
    :param mc_type: Monte Carlo type (either \"first\" or \"every\")
    :param episodes_path: path where the episode for the fixed policy are stored
    :return: value function estimate for the input state
    """
    from pathlib import Path
    import pandas as pd

    # initialize state counter
    n_state = 0

    # initialize value function
    v_state = -1

    # initialize episode return
    g_t = 0

    for path in Path(episodes_path).iterdir():

        # read episode history
        episode_history = pd.read_csv(path, index_col="time")

        # replace literals with numerical values
        episode_history = episode_history.replace(["terminal", "draw"], [22, -1]).astype(
            {"dealer_score": int, "player_score": int})

        state_occurences = episode_history[
            (episode_history.dealer_score == state.dealer_score) & (episode_history.player_score == state.player_score)]

        if state_occurences.shape[0] == 0:
           continue
        elif mc_type == "first":  # first-visit MC
            # update state frequency counter
            n_state += 1

            # compute return
            first_occurence_time = state_occurences.index[0]
            g_t += episode_history[first_occurence_time:].reward.sum()
        elif mc_type == "every":
            # update state frequency counter
            n_state += state_occurences.shape[0]

            # compute return
            for first_occurence_time in state_occurences.index:
                g_t += episode_history[first_occurence_time:].reward.sum()

    # update value function
    # TODO implement non-stationary version with alpha weight
    v_state += 1/n_state * (g_t - v_state)

    return v_state
