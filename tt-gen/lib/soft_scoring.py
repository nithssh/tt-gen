import statistics
from data_models import *

# MOST OF THESE FUNCTIONS ARE NOT TESTED LOL
# TODO: TEST AFTER INITIAL GENERATION IS IMPLEMENTED
def total_weighted_score():
    pass


def ind_coalescing_max(tt: ClassTimetable, day: int):
    max = 0
    for i in range(1, len(tt.timetable[day])):
        if (tt.timetable[day][i] == tt.timetable[day][i-1]):
            max += 1
    return max


def ind_diff_pacing(tt: ClassTimetable, day: int, target_factor: float):
    deviation = 0
    for i in range(1, len(tt.timetable[day])):
        deviation += target_factor - abs(tt.timetable[day][i-1].difficulty_rating -
                                         tt.timetable[day][i].difficulty_rating)
    return deviation


def itd_diff_uniformity(tt: ClassTimetable):
    norm_tot_diffs = []
    for day in range(len(tt.timetable)):
        day_diff = 0
        periods = len(tt.timetable[day])
        for period in range(periods):
            day_diff += tt.timetable[day][period]
        # Might need to tweak this divison / normalization factor
        norm_tot_diffs.append(day_diff / periods)
    # might have to be variance instead
    return statistics.stdev(norm_tot_diffs)


def itd_quality_weighting(tt: ClassTimetable, tt_layout: list[list[int]]):
    last_periods = len(tt.timetable[0])
    weights = _generate_quality_weights(tt_layout, 0)
    sub_weighted_sum = {}
    for day in range(len(tt.timetable)):
        periods = len(tt.timetable[day])
        if (last_periods != periods):
            weights = _generate_quality_weights(tt_layout, day)
        for period in range(periods):
            if (tt.timetable[day][period].quality_weighted):
                sub_id = tt.timetable[day][period].sub_id
                sub_weighted_sum[sub_id] += weights[period]
        last_periods = periods
    return statistics.stdev([v for k, v in sub_weighted_sum])


# def stf_ind_coalescing_max(staff_ref: Staff, day: int):
#     max = 0
#     if (staff_ref.timetable[day][0][0] != 0):
#         max = 1
#     for i in range(1, len(staff_ref.timetable[day])):
#         if (staff_ref.timetable[day][i][0] != 0 and staff_ref.timetable[day][i-1][0] != 0):
#             max += 1
#     return max


def stf_ind_coalescing_max(staff_ref: Staff, day: int):
    max_len = 0
    temp = 0
    for i in range(len(staff_ref.timetable[day])):
        if (staff_ref.timetable[day][i] != None):
            temp += 1
        else:
            max_len = max(temp, max_len)
            temp = 0
    return max(max_len, temp)  # for when the last block doesnt terminate


def stf_itd_load_uniformity(staff_ref: Staff):
    day_loads = []
    for day in range(len(staff_ref.timetable)):
        periods = len(staff_ref.timetable[day])
        load = periods - staff_ref.timetable[day].count(None)
        day_loads.append(load)
    return statistics.stdev(day_loads)


def _generate_quality_weights(tt_layout: list[list[int]], day: int):
    weights = []
    max_day_len = max(map(lambda x: sum(x), tt_layout))
    seg_start = 0
    for segment in range(len(tt_layout[day])):
        for _ in range(tt_layout[day][segment]):
            weights.append(max_day_len - (segment * 1.15))
        # penalize the periods after breaks
        weights[seg_start] -= 1
        seg_start += tt_layout[day][segment]
    weights[-1] -= 1  # penalize the last period
    return weights
