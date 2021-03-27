import random

list = []
for i in range(10):
    r = random.randint(1,30)
    list.append(r)
print("Unsorted")
print(list)

def bubble_sort(list):
    swap = True
    for i in range(len(list)):
        for j in range(0,len(list)-i-1):
            if(list[j] > list[j+1]):
                (list[j],list[j+1]) = (list[j+1],list[j])
                swap = False
        if swap == True:
            break

bubble_sort(list)
print("\nAfter sorted")
print(list)
