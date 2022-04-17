class Staff:
    def __init__(self, staff_id: int):
        self.timetable: list[list[tuple[str, str]]] = []  # (sub_id, class_id)
        # self.subject_ids: list[str] = subject_ids
        self.staff_id = staff_id


class Subject:
    def __init__(self, sub_id: str, weekly_counts: list[tuple[int, int]], staff: Staff, difficulty_rating: int, quality_weighted: bool):
        self.sub_id = sub_id
        self.weekly_counts = weekly_counts  # [(3, 1), (1, 1)] length, count
        self.staff = staff
        self.difficulty_rating = difficulty_rating
        self.quality_weighted = quality_weighted


class ClassInput:
    def __init__(self, subjects: list[Subject], id: str):
        self.subjects = subjects
        self.id = id


class ClassTimetable:
    def __init__(self, tt_layout: list[list[int]]):
        self.timetable: list[list[str]] = []
