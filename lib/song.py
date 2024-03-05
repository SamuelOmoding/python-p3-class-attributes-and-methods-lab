
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance variable to storing songs, artists names and genre
        self.name = name
        self.artist = artist
        self.genre = genre
        #Instance methods
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        Song.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            # Increment artist count
            Song.artist_count[self.artist] += 1
        else:
            # Initialize artist count if it doesn't exist
            Song.artist_count[self.artist] = 1
            
    def genre_histogram():
        for genre, count in Song.genre_count.items():
           return(f"{genre}: {count}")

    def artist_histogram():
        for artist, count in Song.artist_count.items():
            return(f"{artist}: {count}")
            
pass
# Instance creating and Printing attributes of the instance
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  
print(ninety_nine_problems.artist)  
print(ninety_nine_problems.genre) 
#class variables printing 
print(Song.count)  
print(Song.genres)  
print(Song.artists)  
print(Song.genre_count)  
print(Song.artist_count)  