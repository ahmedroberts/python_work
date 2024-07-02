# Get It together

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 1) and (nth_person <= 5):
    print(f'The {nth_person}th oldest person lived {oldest_people[nth_person-1]} years')

animals = ['cat', 'dog', 'bird', 'raptor']
print(animals[0])

# Print Values

user_values = [1, 4, 9]

print(user_values)

# Copy List
uv_copy = user_values[:]


user_values = [1, 5, 7]
user_values[0] = user_values[0] + 1
user_values[2] = user_values[2] + 1
user_values[1] = user_values[1] + 2

print(user_values)

print()
my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[ i ] += 5
    
user_values = [3, 5, 8]

for n in range(len(user_values)):
   print(user_values[n])