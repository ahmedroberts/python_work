'''
num_input = int(input())

input_list = []

for x in range(num_input):
    input_list.append(int(input()))

print(input_list)
'''
'''
not_on_board = input().split()
on_board_bus = input().split()

print(f'Passengers waiting at a bus stop: {not_on_board}')
print(f'Passengers on board: {on_board_bus}')

first_passenger = on_board_bus[0]
on_board_bus.pop(0)
on_board_bus.extend(not_on_board)
print(f'Passenger alighted: {first_passenger}')

print(f'Updated passengers on board: {on_board_bus}')
'''

''' 
tokens = input().split()
video_lengths = []
for token in tokens:
    video_lengths.append(int(token))

video_lengths.sort()
shortest_video = video_lengths[0]
longest_video  = video_lengths[-1]
length_variation = longest_video - shortest_video

print(f'Sorted videos: {video_lengths}')
print(f'The shortest: {shortest_video}')
print(f'The longest: {longest_video}')
print(f'The difference: {length_variation}')
'''
