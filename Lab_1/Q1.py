name = input("Enter your name: ")
age = input("Enter your age: ")

year = 2021

hundred = 100 - int(age)

year_hundred = year + hundred - 1

print("Hi %s, you will be a 100 years old in %d " % (name, year_hundred))
