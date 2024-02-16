import random

# greeting = "Press 'enter' or 'q' to quit.  "
# print(greeting)
# u_input = input()
spin_random = 0
spin_count = 0

while spin_random != 9:
    spin_random = random.randint(-1, 36)
    spin_count += 1
    print(spin_random)
    continue
'''
while u_input != "q":
    spin_random = random.randint(-1, 36)
    u_input = input()
    print(spin_random)
'''
print(f"\t\tAll Done in {spin_count} spins.")
quit
