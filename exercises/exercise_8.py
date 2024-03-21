# Exercise 8
# Your solution comes here
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a last number: "))

first = num1 * (num1 <= num2 and num1 <= num3) + num2 * (num2 < num1 or num2 < num3) + num3 * (num3 < num1 and num3 < num2)
last = num1 * (num1 >= num1 and num1 >= num3) + num2 * (num2 > num1 or num2 > num3) + num3 * (num3 > num1 and num3 > num2)
second = num1 + num2 + num3 - first - last

print(first)
print(second)
print(last)