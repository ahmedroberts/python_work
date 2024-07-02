def code_breaker():
  print('\n################################################\n')

code_breaker()
################################################

'''
List video_lengths contains integers read from input. 
Each integer represents the length of a video recording in minutes. 
Write a loop to update each element in video_lengths with the element's value multipled by 60.
'''

video_lengths = []

# tokens = input().split()
# for token in tokens:
#     video_lengths.append(int(token))

video_lengths = [1, 4, 5, 2, 3, 1]
  
print('Duration in minutes:', end=' ')
for duration in video_lengths:
    print(duration, end=' ')
print()

''' Your code goes here '''
for pos, time in enumerate(video_lengths):
  video_lengths[pos] = time * 60
''' my code ends'''

print('Duration in seconds:', end=' ')
for duration in video_lengths:
    print(duration, end=' ')
print()

code_breaker() ################################################
'''
List data_samples contains integers read from input. 
Each integer represents a random data sample in an experiment. 
Write a loop to remove every element from data_samples that is less than 60.
'''

data_samples = []

# tokens = input().split()
# for token in tokens:
#     data_samples.append(int(token))

data_samples = [100, 50, 75, 66, 34, 99, 60, 69, 12]
  
print('Original samples:', end=' ')
for samples in data_samples:
    print(samples, end=' ')
print()

''' Your code goes here '''
for val in data_samples[:]:
  if val < 60:
    data_samples.remove(val)
''' end my code '''

print('Filtered samples:', end=' ')
for samples in data_samples:
    print(samples, end=' ')
print()

code_breaker() ################################################
'''
List colors_available contains words read from the first line of input. 
List already_picked contains words read from the second line of input. 
For each element in colors_available that is also in already_picked:

Output the element, followed by ' already taken'.
Remove the element from colors_available.
'''

# colors_available = input().split()
# already_picked = input().split()
colors_available = ['black', 'red', 'orange', 'yellow', 'silver', 'blue', 'indigo', 'violet', 'gold']
already_picked = ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']
  
print('Original colors:', end=' ')
for color in colors_available:
    print(color, end=' ')
print()

print('Colors already used:', end=' ')
for color in already_picked:
    print(color, end=' ')
print()

''' Your code goes here '''
for color in colors_available[:]:
  if color in already_picked:
    print(f'{color} already taken')
    colors_available.remove(color)
''' end of my code'''

print('Remaining colors:', end=' ')
for color in colors_available:
    print(color, end=' ')
print()

code_breaker() ################################################
code_breaker() ################################################