from Exercises.inheritance.need_for_speed import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)