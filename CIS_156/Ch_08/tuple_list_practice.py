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