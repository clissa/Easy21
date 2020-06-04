import sys
sys.path.append("code")
sys.path.append("code/extra")

from easy21_utils import step, State, policy
from MonteCarlo_prediction import mc_state_policy_evaluation_incremental

s1 = State(8, 11, 0)
mc_state_policy_evaluation_incremental(s1, "every", "episodes/policy_ge18")