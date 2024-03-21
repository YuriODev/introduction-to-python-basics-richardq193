# Exercise 4
# Your solution comes here
n = int(input("Enter a 4 digit integer: "))
thousands = n // 1000
hundreds = (n//100) %10
tens = (n//10) %10
ones = n%10
if thousands + 1 == hundreds and hundreds + 1 == tens and tens + 1 == ones:
  print("1")
else:
  print(0)