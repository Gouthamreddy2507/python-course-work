class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs  # list of song names

    # + : Merge two playlists
    def __add__(self, other):
        return Playlist(f"{self.name} + {other.name}", self.songs + other.songs)

    # - : Remove songs from one playlist that are in another
    def __sub__(self, other):
        new_songs = [song for song in self.songs if song not in other.songs]
        return Playlist(f"{self.name} - {other.name}", new_songs)

    # * : Repeat the playlist songs
    def __mul__(self, times):
        return Playlist(f"{self.name} * {times}", self.songs * times)

    # / : Split playlist into parts (true division simulation)
    def __truediv__(self, parts):
        part_size = len(self.songs) // parts
        split_playlists = []
        for i in range(parts):
            split_playlists.append(self.songs[i * part_size : (i + 1) * part_size])
        return split_playlists

    # == : Compare playlists by number of songs
    def __eq__(self, other):
        return len(self.songs) == len(other.songs)

    # < : Compare by number of songs
    def __lt__(self, other):
        return len(self.songs) < len(other.songs)

    # > : Compare by number of songs
    def __gt__(self, other):
        return len(self.songs) > len(other.songs)

    # [] : Get song by index
    def __getitem__(self, index):
        return self.songs[index]

    # in : Check if a song is in playlist
    def __contains__(self, song):
        return song in self.songs

    # str() : Print playlist nicely
    def __str__(self):
        return f"Playlist '{self.name}': {', '.join(self.songs)}"


# Create two playlists
p1 = Playlist("Bollywood Hits", ["Kal Ho Na Ho", "Tum Hi Ho", "Senorita"])
p2 = Playlist("Workout Mix", ["Eye of the Tiger", "Senorita", "Believer"])

# + Merge playlists
print(p1 + p2)

# - Remove common songs
print(p1 - p2)

# * Repeat playlist
print(p1 * 2)

# / Split playlist into 2 parts
print(p1 / 2)

# == Equal length?
print(p1 == p2)

# < and >
print(p1 < p2)
print(p1 > p2)

# [] Access song by index
print(p1[1])

# in Check if song exists
print("Senorita" in p1)

# str() - Automatically called in print
print(p2)