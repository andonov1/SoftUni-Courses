from Exercises.inheritance.need_for_speed import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)
