from exams.concert.band import Band
from exams.concert.band_members.drummer import Drummer
from exams.concert.band_members.guitarist import Guitarist
from exams.concert.band_members.singer import Singer
from exams.concert.common import Helper
from exams.concert.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        valid_musician_types = {"Guitarist": Guitarist,
                                "Drummer": Drummer,
                                "Singer": Singer}
        if musician_type not in valid_musician_types:
            raise ValueError("Invalid musician type!")

        elif any(name == x.name for x in self.musicians):
            raise Exception(f"{name} is already a musician!")

        else:
            musician = valid_musician_types[musician_type](name, age)
            self.musicians.append(musician)
            return f"{name} is now a {musician_type}."

    def create_band(self, name):
        if any(name == x.name for x in self.bands):
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for concert in self.concerts:
            if place == concert.place:
                current_genre = concert.genre
                raise Exception(f"{place} is already registered for {current_genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        if not any(musician_name == x.name for x in self.musicians):
            raise Exception(f"{musician_name} isn't a musician!")

        elif not any(band_name == x.name for x in self.bands):
            raise Exception(f"{band_name} isn't a band!")

        else:
            band = ''
            musician = ''
            for x in self.bands:
                if band_name == x.name:
                    band = x

            for x in self.musicians:
                if musician_name == x.name:
                    musician = x

            band.members.append(musician)
            return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        if not Helper.check_if_valid(band_name, self.bands):
            raise Exception(f"{band_name} isn't a band!")

        current_band = ''
        for band in self.bands:
            if band_name == band.name:
                current_band = band

        if not Helper.check_if_valid(musician_name, current_band.members):
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        for musician in current_band.members:
            if musician_name == musician.name:
                current_band.members.remove(musician)

                return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        singer = False
        drummer = False
        guitarist = False
        band = Helper.get_band(band_name, self.bands)
        for member in band.members:
            if member.__class__.__name__ == 'Singer':
                singer = True
            elif member.__class__.__name__ == 'Drummer':
                drummer = True
            elif member.__class__.__name__ == 'Guitarist':
                guitarist = True

        if not singer and not drummer and not guitarist:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = ''
        for x in self.concerts:
            if concert_place == x.place:
                concert = x

        result = False
        if concert.genre == 'Rock':
            result = Helper.check_if_band_can_play(band, Drummer='play the drums with drumsticks',
                                                   Singer='sing high pitch notes',
                                                   Guitarist='play rock')

        elif concert.genre == 'Metal':
            result = Helper.check_if_band_can_play(band, Drummer='play the drums with drumsticks',
                                                   Singer='sing low pitch notes',
                                                   Guitarist='play metal')

        elif concert.genre == 'Jazz':
            result = Helper.check_if_band_can_play(band, Drummer='play the drums with drum brushes',
                                                   Singer='sing high pitch notes and sing low pitch notes',
                                                   Guitarist='play jazz')

        if not result:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        else:
            profit = (concert.audience * concert.ticket_price) - concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
