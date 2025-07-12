class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def __str__(self):
        return f"'{self.title}' by {self.artist}"
    
    def find_by_artist(library, artist_name):
        for song in library:
            if song.artist.lower() == artist_name.lower():
                print(f"{song.title.title()} by {song.artist.title()}")
            
music1 = Music("Homecoming", "kanye West")
music2 = Music("Numb", "linkin Park")
music3 = Music("Bohemian Rhapsody", "queen")
music4 = Music("Stronger", "kanye West")

library = [music1, music2, music3, music4]
            
while True:
    artist_name = input("What artist are you searching for? (or type 'q' to quit): ")
    if artist_name.lower() == "q":
        print("Goodbye!")
        break
    print("You have these songs in your library:")
    Music.find_by_artist(library, artist_name)
    input("Press Enter to continue...")
