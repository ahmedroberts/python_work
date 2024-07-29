
# Your code goes here
try:
    num_socks = int(input())
    pairs = int(num_socks / 2)
    print(f'{pairs} pairs of socks')

except:
    print('Error: Input for number of socks is bad')
    
valid_count = 0

while valid_count < 2:
    try:
        num_dancers = int(input())
        # num_dancers // 2 divides num_dancers by 2 using integer division
        print(f'{num_dancers // 2} pairs of dancers')
        valid_count = valid_count + 1

# Your code goes here
    except:
        print('Discarded the invalid number of dancers entered')
