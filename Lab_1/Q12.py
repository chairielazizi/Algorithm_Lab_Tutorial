def fibonacci(n):
    if(n < 0):
        print("Invalid value")
    elif(n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = input("Enter a number: ")
# fibo = fibonacci(int(num))
for i in range(int(num)):
    print(fibonacci(i))