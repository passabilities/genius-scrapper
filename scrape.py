import json
import time

import lyricsgenius

genius = lyricsgenius.Genius("ohNweOJX3bmczHyKIkbRzEur1HNUCiTMpSv1-dDeUtbTmV9HTOC8-7Yg0EMemXNC")

artist_names = ['Drake', 'Post Malone', 'XXXTENTACION', 'J Balvin', 'Ed Sheeran', 'Big Sean', 'Future', 'Nipsey Hussle', 'Jay Z', 'T.I.', 'Chris Brown', '50 Cent', 'Jacquees', 'Dej Loaf', 'Arianna Grande', 'Dua Lipa', 'Cardi B', 'Taylor Swift', 'Nicki Minaj', 'Camilia Cabello', 'Coldplay', 'Maroon 5', 'Justin Bieber', 'Migos', 'Imagine Dragons', 'Travis Scott', 'Lil Wayne', 'Birdman', 'Kayne West', 'Khalid', '6ix9ine', 'Ella Mai', 'Kendrick Lamar', 'Florida Georgia Line', 'Bebe Rexha', 'Bazzi', 'Marshmello', 'Eminem', 'Lil Pump', '21 Savage', 'NF', 'Demi Lovato', 'Selena Gomez', 'G-Easy', 'The Weekend', 'Lil Baby', 'BlueFace', 'Kane Brown', 'Trey Songs', 'J. Cole', 'Rich The Kid', 'Bad Bunny', '5 Seconds of Summer', 'SZA', 'Portugal. The Man', 'Luke Combs', 'Lauv', 'Thomas Rhett', 'Childish Gambino', 'BlocBoy JB', 'Sam Smith', 'Maren Morris', 'Jason Aldean', 'Offset', 'Luke Bryan', 'Kodak Black', 'Young Thug', 'Ty Dolla $ign', 'Logic', 'Tyga', 'Brett Young', 'Zedd', 'Normani', 'Old Dominion', 'Grey', 'Famous Dex', 'Kenny Chesney', 'Lil Uzi Vert', 'Metro Boomin', 'Justin Timberlake', 'Daddy Yankee', 'Russell Dickerson', 'Anne-Marie', 'Lil Dicky', 'YG', 'Beyonce', 'DJ Khaled']

saved_artists_file_name = '0_saved_artists.json'
def get_saved_artist_names():
    try:
        with open(saved_artists_file_name, 'r') as file:
            artists_data = json.load(file)
    except FileNotFoundError:
        artists_data = []
    except json.decoder.JSONDecodeError:
        artists_data = []

    return artists_data

def get_artists_to_get():
    saved_artists = get_saved_artist_names()

    return [name for name in artist_names if name not in saved_artists]

def get_artist(name):
    try:
        artist = genius.search_artist(name)
    except (Exception, TypeError):
        time.sleep(5)
        artist = get_artist(name)

    return artist

for name in get_artists_to_get():
    artist = get_artist(name)
    artist.save_lyrics()

    saved_artists = get_saved_artist_names()
    saved_artists.append(name)
    with open(saved_artists_file_name, 'w') as file:
        json.dump(saved_artists, file)

