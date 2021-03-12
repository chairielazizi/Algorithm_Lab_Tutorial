from datetime import datetime

name=raw_input("Enter your name:")
age=raw_input("Enter your age:")

num= int(datetime.now().year)+100-int(age)

print("The year that you will turn 100 years old is: %d" %num)