s = 'Hello, World'
print(s)
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())


s = '         Hello,         World        '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(s.split())

s='apple banana cherry'
print(s.split())
s='apple, banana, cherry'
print(s.split())
s='apple,banana,cherry'
print(s.split())
print(s.split(','))


s_list = s.split(',')
print(s_list)
print(','.join(s_list))
print('.'.join(s_list))
print(' '.join(s_list))

s = "Hello, World"
print(s)
print(s.startswith('Hello'))
print(s.endswith('Hello'))