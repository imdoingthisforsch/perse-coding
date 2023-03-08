x = input('type anything here: ')
y = int(input('type a number here: '))

x_reverse = x[::-1]

result = x_reverse * y
result = result.replace(' ', '')
print(result)
