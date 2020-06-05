from Code.easy21_utils import State
from Code.extra.TemporalDifference_prediction import td_policy_evaluation

initial_value_function = {(8, 11): 0,
                          (2, 22): -1,
                          (2, 18): -1,
                          (7, 15): 1,
                          (3, 21): 1}

s = State(8, 11, 0)
td_policy_evaluation(s, gamma=1, alpha=0.3, episodes_path="episodes/policy_ge18", V_s = initial_value_function)
s.value_function