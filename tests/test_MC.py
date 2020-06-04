from Code.easy21_utils import easy21_utils import step, State, policy
from Code.extra.MonteCarlo_prediction import mc_state_policy_evaluation_incremental

s1 = State(8, 11, 0)
mc_state_policy_evaluation_incremental(s1, "every", "episodes/policy_ge18")