from Code.easy21_utils import State
from Code.extra.MonteCarlo_prediction import mc_state_policy_evaluation_incremental

s = State(8, 11, 0)
mc_state_policy_evaluation_incremental(s, "every", "episodes/policy_ge18")
s.value_function

s = State(8, 11, 0)
mc_state_policy_evaluation_incremental(s, "first", "episodes/policy_ge18")
s.value_function