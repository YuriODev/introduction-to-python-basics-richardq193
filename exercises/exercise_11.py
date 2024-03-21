# Exercise 11
# Your solution comes here
s = float(input("Enter the total: "))
b500 = s // 500
s %= 500

b100 = s // 100
s %= 100

b10 = s // 10
s %= 10

b5 = s // 5
s %= 5

b1 = s
print(f"{b500} (500), {b100} (100), {b10} (10), {b5} (5), {b1} (1)")