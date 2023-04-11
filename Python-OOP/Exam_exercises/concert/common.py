class Helper:

    @staticmethod
    def check_if_valid(name, place):
        if any(name == x.name for x in place):
            return name

    @staticmethod
    def get_band(band_name, place):
        for x in place:
            if band_name == x.name:
                return x

    @staticmethod
    def check_if_band_can_play(band, **requirements):
        for member in band.members:
            required_skill = requirements[member.__class__.__name__]
            if required_skill not in member.skills:
                return False
        return True

