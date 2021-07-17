num = int(input('Please input the distance in kilometers:'))

if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

status = 'The number is odd' if num % 2 else 'The number is even'
print(status)
