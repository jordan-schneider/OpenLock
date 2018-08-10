import numpy as np

from openlock.common import TwoDConfig, LeverConfig, LeverRole

NUM_LEVERS = 7

UPPER = TwoDConfig(0, 15, 0)
LEFT = TwoDConfig(-15, 0, np.pi / 2)
LOWER = TwoDConfig(0, -15, -np.pi)
UPPERLEFT = TwoDConfig(-11, 11, np.pi/4)
UPPERRIGHT = TwoDConfig(11, 11, -np.pi/4)
LOWERLEFT = TwoDConfig(-11, -11, 3*np.pi / 4)
LOWERRIGHT = TwoDConfig(11, -11, 5*np.pi/4)

ATTEMPT_LIMIT = 30
ACTION_LIMIT = 3

THREE_LEVER_TRIALS = ['trial1', 'trial2', 'trial3', 'trial4', 'trial5', 'trial6']
FOUR_LEVER_TRIALS = ['trial7', 'trial8', 'trial9', 'trial10', 'trial11']

PARAMS = {
    'CE3-CE4': {
        'train_num_trials': 6,
        'train_scenario_name': 'CE3',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_num_trials': 1,
        'test_scenario_name': 'CE4',
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    },
    'CE3-CC4': {
        'train_num_trials': 6,
        'train_scenario_name': 'CE3',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_num_trials': 1,
        'test_scenario_name': 'CC4',
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    },
    'CC3-CE4': {
        'train_num_trials': 6,
        'train_scenario_name': 'CC3',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_num_trials': 1,
        'test_scenario_name': 'CE4',
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    },
    'CC3-CC4': {
        'train_num_trials': 6,
        'train_scenario_name': 'CC3',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_num_trials': 1,
        'test_scenario_name': 'CC4',
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    },
    'CC4': {
        'train_num_trials': 5,
        'train_scenario_name': 'CC4',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_num_trials': 0,
        'test_scenario_name': None,
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    },
    'CE4': {
        'train_num_trials': 5,
        'train_scenario_name': 'CE4',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_num_trials': 0,
        'test_scenario_name': None,
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    },
    'testing': {
        'train_num_trials': 1,
        'train_scenario_name': 'CC3',
        'train_attempt_limit': ATTEMPT_LIMIT,
        'train_action_limit': ACTION_LIMIT,
        'test_scenario_name': None,
        'test_attempt_limit': ATTEMPT_LIMIT,
        'test_action_limit': ACTION_LIMIT
    }
}

# maps arbitrary indices to parameter settings strings
IDX_TO_PARAMS = [
    'CE3-CE4',
    'CE3-CC4',
    'CC3-CE4',
    'CC3-CC4',
    'CE4',
    'CC4'
]

# mapping from 2dconfigs to position indices
CONFIG_TO_IDX = {
    UPPERRIGHT: 0,
    UPPER:      1,
    UPPERLEFT:  2,
    LEFT:       3,
    LOWERLEFT:  4,
    LOWER:      5,
    LOWERRIGHT: 6
}

# mapping from position indices to position names
IDX_TO_POSITION = {
    0: 'UPPERRIGHT',
    1: 'UPPER',
    2: 'UPPERLEFT',
    3: 'LEFT',
    4: 'LOWERLEFT',
    5: 'LOWER',
    6: 'LOWERRIGHT',
}

# mapping from position names to position indices
POSITION_TO_IDX = {
    'UPPERRIGHT':   0,
    'UPPER':        1,
    'UPPERLEFT':    2,
    'LEFT':         3,
    'LOWERLEFT':    4,
    'LOWER':        5,
    'LOWERRIGHT':   6,
}

LEVER_CONFIGS = {
    # Trial 1. l0=UPPERLEFT, l1=LOWERLEFT, l2=UPPERRIGHT,
    'trial1'   : [LeverConfig(UPPERRIGHT,   LeverRole.l0,       None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LEFT,         LeverRole.inactive, None),
                  LeverConfig(LOWERLEFT,    LeverRole.l1,       None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 2. l0=UPPER, l1=LOWER, l2=LEFT,
    'trial2'   : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.l2,       None),
                  LeverConfig(UPPERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LEFT,         LeverRole.l0,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LOWER,        LeverRole.l1,       None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 3. l0=UPPERLEFT , l1=LOWERLEFT, l2=LOWERRIGHT,
    'trial3'   : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.l1,       None),
                  LeverConfig(LEFT,         LeverRole.inactive, None),
                  LeverConfig(LOWERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.l0,       None)],
    # Trial 4. l0=UPPER, l1=UPPERLEFT, l2=UPPERRIGHT,
    'trial4'   : [LeverConfig(UPPERRIGHT,   LeverRole.l0,       None),
                  LeverConfig(UPPER,        LeverRole.l2,       None),
                  LeverConfig(UPPERLEFT,    LeverRole.l1,       None),
                  LeverConfig(LEFT,         LeverRole.inactive, None),
                  LeverConfig(LOWERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 5. l0=UPPERLEFT, l1=LOWERLEFT, l2=LEFT,
    'trial5'   : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LEFT,         LeverRole.l0,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.l1,       None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 6. l0=LOWERLEFT, l1=LOWER, l2=LOWERRIGHT,
    'trial6'   : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LEFT,         LeverRole.inactive, None),
                  LeverConfig(LOWERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LOWER,        LeverRole.l1,       None),
                  LeverConfig(LOWERRIGHT,   LeverRole.l0,       None)],
    # Trial 7. l0=LOWERLEFT, l1=UPPERRIGHT, l2=LOWERRIGHT, l3=UPPERLEFT
    'trial7'   : [LeverConfig(UPPERRIGHT,   LeverRole.l1,       None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.l3,       None),
                  LeverConfig(LEFT,         LeverRole.inactive, None),
                  LeverConfig(LOWERLEFT,    LeverRole.l0,       None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.l2,       None)],
    # Trial 8. l0=UPPERRIGHT, l1=UPPER, l2=UPPERLEFT, l3=LEFT
    'trial8'   : [LeverConfig(UPPERRIGHT,   LeverRole.l0,       None),
                  LeverConfig(UPPER,        LeverRole.l1,       None),
                  LeverConfig(UPPERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LEFT,         LeverRole.l3,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 9. l0=UPPERLEFT, l1=UPPER, l2=LEFT, l3=LOWERLEFT
    'trial9'   : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.l1,       None),
                  LeverConfig(UPPERLEFT,    LeverRole.l0,       None),
                  LeverConfig(LEFT,         LeverRole.l2,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.l3,       None),
                  LeverConfig(LOWER,        LeverRole.inactive, None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 10. l0=LOWERLEFT, l1=UPPERLEFT, l2=LEFT, l3=LOWER
    'trial10'  : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.l1,       None),
                  LeverConfig(LEFT,         LeverRole.l2,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.l0,       None),
                  LeverConfig(LOWER,        LeverRole.l3,       None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # Trial 11. l0=LOWERRIGHT, l1=LEFT, l2=LOWERLEFT, l3=LOWER
    'trial11'  : [LeverConfig(UPPERRIGHT,   LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.inactive, None),
                  LeverConfig(UPPERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LEFT,         LeverRole.l1,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LOWER,        LeverRole.l3,       None),
                  LeverConfig(LOWERRIGHT,   LeverRole.l0,       None)],

    # multi-lock. l0=UPPER, l1=LOWER, l2=LEFT,
    'multi-lock': [LeverConfig(UPPERRIGHT,  LeverRole.inactive, None),
                  LeverConfig(UPPER,        LeverRole.l2,       None),
                  LeverConfig(UPPERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LEFT,         LeverRole.l0,       {'lower_lim': 0.0, 'upper_lim': 2.0}),
                  LeverConfig(LOWERLEFT,    LeverRole.inactive, None),
                  LeverConfig(LOWER,        LeverRole.l1,       None),
                  LeverConfig(LOWERRIGHT,   LeverRole.inactive, None)],
    # full.
    'full'     : [LeverConfig(UPPERRIGHT,   LeverRole.l0,       None),
                  LeverConfig(UPPER,        LeverRole.l1,       None),
                  LeverConfig(UPPERLEFT,    LeverRole.l2,       None),
                  LeverConfig(LEFT,         LeverRole.l3,       None),
                  LeverConfig(LOWERLEFT,    LeverRole.l4,       None),
                  LeverConfig(LOWER,        LeverRole.l5,       None),
                  LeverConfig(LOWERRIGHT,   LeverRole.l6,       None)],
}


def select_trial(trial):
    return trial, LEVER_CONFIGS[trial]


def get_trial(name, completed_trials=None):
    """
    Apply specific rules for selecting random trials.
    Namely, For CE4 & CC4, only selects from trials 7-11, otherwise only selects from trials 1-6.

    :param name: Name of trial
    :param completed_trials:
    :return: trial and configs
    """
    # select a random trial and add it to the scenario
    if name != 'CE4' and name != 'CC4':
        # trials 1-6 have 3 levers for CC3/CE3
        trial, configs = select_random_trial(completed_trials, THREE_LEVER_TRIALS)
    else:
        # trials 7-11 have 4 levers for CC4/CE4
        trial, configs = select_random_trial(completed_trials, FOUR_LEVER_TRIALS)

    return trial, configs


def select_random_trial(completed_trials, possible_trials):
    '''
    sets a new random trial
    :param completed_trials: list of trials already selected
    :param possible_trials: list of all trials possible
    :return:
    '''
    if len(completed_trials) == len(possible_trials):
        return None, None

    incomplete_trials = np.setdiff1d(possible_trials, completed_trials)
    rand_trial_idx = np.random.randint(0, len(incomplete_trials))
    trial = incomplete_trials[rand_trial_idx]

    return select_trial(trial)

