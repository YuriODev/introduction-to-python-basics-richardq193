# Exercise 5
# Your solution comes here
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number:"))
max = n1 * (n1 > n2) + n2 * (n2 >= n1)
print(max)
