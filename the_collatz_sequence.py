def collatz(number):
  if number%2 == 0:
    return (number // 2)
  else:
    return (3 * number + 1)
    
try:
  number = int(input())
except ValueError:
  print('Please enter an integer')

print(collatz(number))
