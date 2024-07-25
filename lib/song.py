class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the count of songs
        Song.add_song_to_count()
        
        # Add artist and genre
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        
        # Update counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  # "99 Problems"
print(ninety_nine_problems.artist)  # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"

# Checking the class attributes
print(Song.count)  # 1
print(Song.artists)  # ["Jay-Z"]
print(Song.genres)  # ["Rap"]
print(Song.genre_count)  # {"Rap": 1}
print(Song.artist_count)  # {"Jay-Z": 1}
