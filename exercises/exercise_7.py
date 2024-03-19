# Exercise 7
# Your solution comes here
num = int(input("Enter a 4 digit number: "))
thou = num // 1000
hund = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10
sum = thou + hund + tens + ones
print(sum)