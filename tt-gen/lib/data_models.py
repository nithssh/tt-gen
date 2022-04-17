class Staff:
    def __init__(self, id: int, tt_layout: list[list[int]]):
        self.id = id
        # (sub_id, class_id)
        self.timetable: list[list[tuple[str, str]]] = _generate_tt(tt_layout, None)


class SubjectInstance:
    def __init__(self, sub_id: str, weekly_counts: list[tuple[int, int]], staff_ref: Staff, difficulty_rating: int, quality_weighted: bool):
        self.sub_id = sub_id
        self.weekly_counts = weekly_counts  # [(3, 1), (1, 1)] length, count
        self.staff_ref = staff_ref
        self.difficulty_rating = difficulty_rating
        self.quality_weighted = quality_weighted


class ClassInput:
    def __init__(self, subjects: list[SubjectInstance], id: str):
        self.id = id
        self.subjects = subjects


class ClassTimetable:
    def __init__(self, tt_layout: list[list[int]]):
        self.timetable: list[list[SubjectInstance]] = _generate_tt(tt_layout, None)


def _generate_tt(ttl, val):
    timetable = []
    for i in range(len(ttl)):
        ttd = []
        for j in range(len(ttl[i])):
            for _ in range(ttl[i][j]):
                ttd.append(val)
        timetable.append(ttd)
    return timetable

