x = input('input a single word here: ')
x = x.replace(' ', '')
output = ""
repeat = 1
while len(output) < 30:
  output = x * repeat 
  repeat += 1
print(output)
