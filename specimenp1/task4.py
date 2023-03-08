while True:
  n = input("input a number between 1 to 100: ")
  try: 
    n = int(n)
    if n < 1 or n > 100: 
      print('u have input an invalid number!')
      continue
    else:
      print("u have entered a valid value", ",", n)
      break
  except ValueError:
    print('please enter a number')
    continue
if n > 50: 
  print('yes dream big')
else:
  print('on the small side')
