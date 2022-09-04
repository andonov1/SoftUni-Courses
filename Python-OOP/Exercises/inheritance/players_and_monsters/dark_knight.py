from Exercises.inheritance.need_for_speed import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)