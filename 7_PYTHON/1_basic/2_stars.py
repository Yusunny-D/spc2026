print('*')
print('**')
print('***')
print('****')
print('*****')

print('\n - 1 - ')
for i in range(1, 6):
    print('*'*i)

print('\n - 2 - ')
for i in range(1, 6):
    print(' '*(5-i), end='')
    print('*'*i)
    # print(' '*(5-i) +'*'*i)

print('\n - 3 - ')
for i in range(1, 6):
    print(' '*(5-i) +'*'*(2*i-1), ' '*(5-i))


