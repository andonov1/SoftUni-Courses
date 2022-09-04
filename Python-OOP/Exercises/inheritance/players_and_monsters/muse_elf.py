from Exercises.inheritance.need_for_speed import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)