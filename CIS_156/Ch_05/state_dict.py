# state_dict = {
#     'New Jersey': 'NJ',
#     'California': 'CA',
#     'Florida': 'FL',
#     'Arkansas': 'AR',
#     'Wyoming': 'WY'
# }

# state_name = input()
# state_abbrev = input()
# state_dict[state_name] = state_abbrev

# print(state_dict)

# for state in state_dict:
#     print(f"{state}'s code: {state_dict[state]}")
    
num_successes = 0

curr_depth = int(input())

while num_successes < 4:

    print(curr_depth)
    if curr_depth > 0:
        num_successes += 1
    curr_depth = int(input())
