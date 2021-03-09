# list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#using for loop
def for_(list):
    for i in a:
        if(i < 5):
            print(i)

#using for loop and range
def for_range(a):
    for i in range(len(a)):
        if(a[i] < 5):
            print(a[i])

# for_(a)
for_range(a)