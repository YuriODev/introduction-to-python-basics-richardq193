# Exercise 9
# Your solution comes here
hrs = int(input("Enter hours: "))
mins = int(input("Enter mins: "))
secs = int(input("Enter seconds: "))
angle = 0.5 * (60 * hrs + mins + secs / 60)
print(angle)