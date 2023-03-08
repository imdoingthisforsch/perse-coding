while True: 
  n = input('please input a number between -100 and 100: ')
  try:
    n = int(n)
    if n < -100 or n > 100:
      print("please input a value that is between -100 and 100")
      continue
    else: 
      print('u have input a valid number: ', n)
      break
  except ValueError: 
    print ('please input a number!')
allowed_operators = ['-', '+', '*']
while True:
  sign = input("please input a '-', '+', '*': ")
  if sign not in allowed_operators:
    print('please enter a ', allowed_operators)
    continue
  else: 
    print("u have input a correct operator, ", sign)
    break
while True: 
  n2 = input('please input another number between -100 and 100: ')
  try:
    n2 = int(n2)
    if n2 < -100 or n > 100:
      print("please input a value that is between -100 and 100")
      continue
    else: 
      print('u have input a valid number: ', n2)
      break
  except ValueError: 
    print ('please input a number!')
print(n, sign, n2)
if sign == '+':
  result = n + n2
  print(result)
elif sign == '*':
  result = n * n2
  print(result)
else:
  result = n - n2
  print(result)
