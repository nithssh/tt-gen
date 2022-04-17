from data_models import *

# GLOBAL STATE -----------------------------------------------------------------
# These inits need to be moved out of the solver file
# and into the front

staffs: dict[Staff] = {}
classes: dict[ClassTimetable] = {}
# [ [2, 3, 3], [2, 3, 3], ... , [2, 3, 3], [2, 3] ]
tt_layout: list[list[int]] = []
soft_constr: dict = {
    # close to zero coalesced periods | target difficulty difference of 2 b/w periods
    'ind_coalescing': 0, 'ind_diff_pacing': 2,
    # uniform quality weighting for enrolled subs | close to no interday difficulty difference
    'itd_quality_weighting': 0, 'itd_diff_uniformity': 0,
    # max 3 period blocks for staff | close to no interday variance for staff load
    'stf_ind_coalscing': 3, 'stf_itd_load_uniformity': 0
}

# every soft_constr enabled
soft_constr_toggle: dict = {
    'ind_coalescing': True, 'ind_diff_pacing': True,
    'itd_quality_weighting': True, 'itd_diff_uniformity': True,
    'stf_ind_coalscing': True, 'stf_itd_load_uniformity': True
}

# INPUTS -----------------------------------------------------------------------
class_ins: dict[ClassInput] = {}
