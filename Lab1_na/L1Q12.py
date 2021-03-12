def Fibonacci(num):
    n1,n2,count=0,1,0
    if num<=0:
        print("Please enter a positive integer")
    elif num==1:
        print("Fibonacci sequence: %d"%n1)
    else:
        print("Fibonacci sequence:")
        while count<num:
            print(n1)
            n=n1+n2
            #update value
            n1=n2
            n2=n
            count+=1

num=input("Choose a number:")
Fibonacci(num)