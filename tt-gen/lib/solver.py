from data_models import *

# GLOBAL STATE -----------------------------------------------------------------
# These inits need to be moved out of the solver file
# and into the front
# TODO: Remove test values

tt_layout: list[list[int]] = [
    [2, 3, 3], [2, 3, 3], [2, 3, 3], [2, 3, 3], [2, 3, 3]
]

staffs: dict[int, Staff] = {
    1: Staff(1, tt_layout),
    2: Staff(2, tt_layout),
    3: Staff(3, tt_layout),
    4: Staff(4, tt_layout),
    5: Staff(5, tt_layout),
    6: Staff(6, tt_layout),
    7: Staff(7, tt_layout),
    8: Staff(8, tt_layout),
    9: Staff(9, tt_layout)
}

classes: dict[str, ClassTimetable] = {}

soft_constr: dict[str, int] = {
    # close to zero coalesced periods | target difficulty difference of 2 b/w periods
    'ind_coalescing': 0, 'ind_diff_pacing': 2,
    # uniform quality weighting for enrolled subs | close to no interday difficulty difference
    'itd_quality_weighting': 0, 'itd_diff_uniformity': 0,
    # max 3 period blocks for staff | close to no interday variance for staff load
    'stf_ind_coalescing': 3, 'stf_itd_load_uniformity': 0
}

# every soft_constr enabled
soft_constr_toggle: dict[str, bool] = {
    'ind_coalescing': True, 'ind_diff_pacing': True,
    'itd_quality_weighting': True, 'itd_diff_uniformity': True,
    'stf_ind_coalescing': True, 'stf_itd_load_uniformity': True
}

# INPUTS -----------------------------------------------------------------------
class_ins: dict[str, ClassInput] = {
    '2CSEB': ClassInput([
        SubjectInstance('191MAB403T', [(1, 6)], staffs[1], 4, True),
        SubjectInstance('191CSC401T', [(1, 5)], staffs[2], 3, True),
        SubjectInstance('191CSC402T', [(1, 4)], staffs[3], 2, True),
        SubjectInstance('191CSC403T', [(1, 5)], staffs[4], 3, True),
        SubjectInstance('191CSC404T', [(1, 3)], staffs[5], 2, True),
        SubjectInstance('191CSC411L', [(3, 1), (1, 1)], staffs[6], 1, False),
        SubjectInstance('191CSC412L', [(3, 1), (1, 1)], staffs[7], 1, False),
        SubjectInstance('191CSC413L', [(3, 1), (1, 1)], staffs[8], 1, False),
        SubjectInstance('CDC', [(2, 1)], staffs[9], 1, False),
    ], '2CSEB')
}

# Solver -----------------------------------------------------------------------

