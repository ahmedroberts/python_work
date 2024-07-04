# Ahmed O. Roberts
# Module 08 Programming Assignment
# Part B

# This program looks up the artists of songs of the 1990's
# https://www.rollingstone.com/music/music-lists/50-best-songs-of-the-nineties-252530/nirvana-smells-like-teen-spirit-1991-252544/

import random

# Define Variables
greeting = '\nWelcome to the 90\'s artist finder\n'
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
# random_song = random.choice(songs)
found_song = False
msg_get_song_inp ='Enter title of the song name: '
msg_artist_not_found = 'Sorry, Artist Not found'
# msg_random_song = f'Sample song title: {random_song}\n'

# Define Functions
# get the proper song title
def get_90s_song_title(inp_song='exit'):
  if inp_song == 'exit':
    return 'exit'
  for song in songs:
    if str(inp_song) in song:
      full_title = song
      return full_title
  return 'Unfortunately, Song Not Found'

# return artist associated with the song
def get_90s_artist_name(song_title='none'):
  if song_title == 'none':
    return 'none'
  if song_title in songs:
    artist_name = nineties_songs[song_title]
    return artist_name
  else:
    return msg_artist_not_found

# Start Program ---------------------------------------------------------
print('list of songs:', songs) # proof of all keys
print(greeting)

inp_song = input(f'Enter song title like, `{random.choice(songs)}` or `exit` to end: ')

while inp_song != 'exit':
  # print('test ==================> ', get_90s_song_title(inp_song))
  # inp_song = input(msg_get_song_inp)
  full_song_title = get_90s_song_title(inp_song)
  artist_name = get_90s_artist_name(full_song_title)
  print(f'Song Title: {full_song_title}\nArtist Name: {artist_name}\n')
  inp_song = input(f'\nEnter song title like, `{random.choice(songs)}`: ')
