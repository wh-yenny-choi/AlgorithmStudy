'''
별찍기
'''
# 1
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print('')

# 2
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# 3
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for j in range(5-i):
        print('*', end='')
    print('')

# 4
for i in range(1, 6):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')

# 5
for i in range(1, 6):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(1, i*2, 1):
        print('*',end='')
    print('')

# 6
for i in range(1, 6):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(1, i *2, 1):
        print('*', end='')
    print()
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for j in range(10, 1 + i*2, -1):
        print('*', end='')
    print()

# 7
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for j in range(10, 1 + i*2, -1):
        print('*', end='')
    print('')
for i in range(2, 6):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(1, i*2, 1):
        print('*', end='')
    print('')