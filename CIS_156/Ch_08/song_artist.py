# Ahmed O. Roberts
# Module 08 Programming Assignment
# Part B

# This program looks up the artists of songs of the 1990's
# https://www.rollingstone.com/music/music-lists/50-best-songs-of-the-nineties-252530/nirvana-smells-like-teen-spirit-1991-252544/

import random

greeting = '\nWelcome to the 90\'s artist finder\l'
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
print('list of songs:', songs) # proof of all keys

random_song = random.choice(songs)
print(f'\nSong name example: {random_song}\n') # randomly select a song


inp_song = input('Enter title (hopefully, any part) of the song name: ')
print(inp_song)

'''
create a function to 
- get input string value
- check if that string is in the title of any song in the list
- return the full song title
'''

found_song = False

if inp_song in songs:
  found_song = True
  song_name = inp_song # assign song <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  print(f'\nSong found: [{found_song}] => Song: `{song_name}` artist is: `{nineties_songs[song_name]}`\n')
else:
  print(f'Sorry that song, `{inp_song}` was not found.')

def get_90s_song_title():
  pass

'''
return artis in dictionary or artist not found
'''
def get_90s_artist_name(song_title):
  pass