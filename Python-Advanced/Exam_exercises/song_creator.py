def add_songs(*args):
    songs = {}
    result = ''
    for el in args:
        song, lines = el[0], el[1]
        if song not in songs:
            songs[song] = []
        if lines:
            for line in lines:
                if song not in songs:
                    songs[song] = []
                songs[song].append(line)

    for song, lyrics in songs.items():
        result += f'- {song}\n'
        for lyric in lyrics:
            result += f'{lyric}\n'
    return result

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
