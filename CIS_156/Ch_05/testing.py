
stop = int(input())
result = 0

for a in range(4):
    print(a + 1, end=': ')
    
    for b in range(3):
        result += a + 1
        
        if result > stop:
            print('_', end=' ')
            continue
        
        print(result, end=' ')
    
    print()
    
    