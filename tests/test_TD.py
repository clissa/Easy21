from Code.easy21_utils import State
from Code.extra.TemporalDifference_prediction import td_policy_evaluation

s = State(8, 11, 0)
td_policy_evaluation(s, gamma=1, alpha=0.3, episodes_path="episodes/policy_ge18")
s.value_function