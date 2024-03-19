# Exercise 3
# Your solution comes here
n = int(input("Enter a value: "))
hrs = (n // 3600) % 24
mins = (n // 60) % 60
secs = n % 60
print(f"{hrs}:{mins:02d}:{secs:02d}")