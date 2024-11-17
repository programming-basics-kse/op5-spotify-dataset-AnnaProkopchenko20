with open("convert.tsv") as file :
    HEADER = next(file).split("\t")

    #wierd symbols in [0] element
    HEADER[0] = HEADER[0][3:]

    DANCE = HEADER.index("danceability")
    ENERGY = HEADER.index("energy")
    LIVE = HEADER.index("liveness")
    ARTIST = HEADER.index("artist_name")
    EXPLICIT = HEADER.index("is_explicit")
    DATE = HEADER.index("album_release_date")
    GENRES = HEADER.index("genres")

    num_of_explicit_songs = 0
    danceability = []
    liveliness = []
    artist_appearance = {}
    songs_per_year = {}
    genres_frequency = {}

    for line in file:
        line = line.split("\t")#has commas inside can't be split usually how to make it tab using exel

        danceability.append(float(line[DANCE]))

        if float(line[ENERGY]) >= 0.5:
            liveliness.append(float(line[LIVE]))

        if line[ARTIST] not in artist_appearance:
            artist_appearance[line[ARTIST]] = 1
        else :
            artist_appearance[line[ARTIST]] += 1

        if line[EXPLICIT] :
            num_of_explicit_songs += 1

        if line[DATE][:4] not in songs_per_year:
            songs_per_year[line[DATE][:4]] = 1
        else :
            songs_per_year[line[DATE][:4]] += 1

        for genre in line[GENRES]:
            if genre not in genres_frequency :
                genres_frequency[genre] = 1
            else :
                genres_frequency[genre] += 1



print(round(sum(danceability)/len(danceability),3))

print(round(sum(liveliness)/len(liveliness),3))

M = max(artist_appearance.values())
for artist in artist_appearance:
    if artist_appearance[artist] == M:
        print(artist, M)

max_releases = max(songs_per_year.values())
for year in songs_per_year:
    if songs_per_year[year] == max_releases:
        print(year, max_releases)

revers_genres_frequency = {}
for genre in genres_frequency:
    if genres_frequency[genre] not in revers_genres_frequency:
        revers_genres_frequency[genres_frequency[genre]] = []
    revers_genres_frequency[genres_frequency[genre]].append(genre)
#need to finish but to lazy to think on sunday evening






