# Easy21

## Description 
This repository contains the code to solve the assignment of the [course](https://www.davidsilver.uk/teaching/) on **Reinforcement
Learning** given by [*David Silver*](https://www.davidsilver.uk/) at [UCL](https://www.ucl.ac.uk/) (University College London).

## Usage
The text of the assignment is reported in the *Easy21_assignment.pdf* file.
The code to solve the 4 questions is available in the *code* folder.

The script `easy21_utils.py` contains useful routines to simulate the Easy21 environment.
In particular, the *step()* fucntion allows evolving the game of one step 
starting from the current state and the action of the player.

The script `easy21_episode.py` provides a wrapper to the step() routine to run a full episode of Easy21.
Furthermore, it keeps track of the evolution of the game, returning a pandas DataFrame containing the history from initialization to terminal state.

The folder `Code/extra` stores additional implementation not specifically required for the assignment, 
namely *first/every-visit Monte Carlo policy evaluation*, both with final and incremental updates, and 
*Temporal Difference for 1-step look-ahead*, i.e., TD(0).

### Simulate games
In order to simulate multiple games it is possible to run *easy21_episode.py* from command line as follows:

```commandline
# python code/easy21_episode.py <n_episodes> <save_path: default="./episodes">
python code/easy21_episode.py 100 
```

The output will be stored into the specified *save_path* folder, with one *.csv* file per episode.

## Installation

In order to reproduce the same environment used to test the code simply run:

```
# clone the repository
git clone https://github.com/clissa/Easy21.git

# reproduce the same environment using Anaconda
cd Easy21
conda env create -f environment.yml

# activate the new environment
conda activate Easy21
```