def td_policy_evaluation(state, gamma, alpha, episodes_path, V_s=None):
    from pathlib import Path
    import pandas as pd
    from Code.easy21_utils import State

    # initialize value function for all the states if not specified
    if V_s is None:
        V_s = {(dealer_score, player_score): 3 for dealer_score in range(-1, 23) for player_score in range(-1, 23)}

    for path in Path(episodes_path).iterdir():
        # read episode history
        episode_history = pd.read_csv(path, index_col="time")

        # replace literals with numerical values
        episode_history = episode_history.replace(["terminal", "draw"], [22, -1]).astype(
            {"dealer_score": int, "player_score": int})

        state_occurrences = episode_history[
            (episode_history.dealer_score == state.dealer_score) & (episode_history.player_score == state.player_score)]

        if state_occurrences.shape[0] == 0:
            continue
        else:
            # compute expected return
            for first_occurrence_time in state_occurrences.index:

                # retrieve expected return for next state
                next_state = State(episode_history.loc[first_occurrence_time].dealer_score,
                                   episode_history.loc[first_occurrence_time].player_score)
                next_state.value_function = V_s.get((episode_history.loc[first_occurrence_time + 1].dealer_score,
                                                     episode_history.loc[first_occurrence_time + 1].player_score), 0)
                # expected return
                g_t = episode_history.loc[first_occurrence_time].reward + gamma * next_state.value_function

                # update value function of the state
                state.value_function += alpha * (g_t - state.value_function)

                # update value function dictionary
                V_s[(episode_history.loc[first_occurrence_time].dealer_score,
                                   episode_history.loc[first_occurrence_time].player_score)] = state.value_function

    return
