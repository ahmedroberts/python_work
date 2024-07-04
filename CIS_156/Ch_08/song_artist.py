# Ahmed O. Roberts
# Module 08 Programming Assignment
# Part B

# This program looks up the artists of songs of the 1990's
# https://www.rollingstone.com/music/music-lists/50-best-songs-of-the-nineties-252530/nirvana-smells-like-teen-spirit-1991-252544/

import random

greeting = 'Welcome to the 90\'s artist finder'
print(greeting)

nineties_songs = {
  'Smells Like Teen Spirit': 'Nirvana',
  'No Diggity': 'Blackstreet',
  'Mo Money Mo Problems': 'Notorious B.I.G. with Mase and Puff Daddy',
  'Rebel Girl': 'Bikini Kill',
  "Nuthin' but a 'G' Thang": 'Dr. Dre and Snoop Dogg',
  'Gold Soundz': 'Pavement',
  'The Rain (Supa Dupa Fly)': 'Missy "Misdeameanor" Elliott'
}

songs = list(nineties_songs.keys())
random_song = random.choice(songs)
print(f'\nSong name example: {random_song}')
inp_song = input('Enter title (hopefully, any part) of the song name: ')
print(inp_song)

'''
create a function to 
- get input string value
- check if that string is in the title of any song in the list
- return the full song title
'''

def get_song_title():
  pass

'''
return artis in dictionary or artist not found
'''
def get_artist_name(song_title):
  pass