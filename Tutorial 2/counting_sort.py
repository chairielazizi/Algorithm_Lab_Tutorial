'''
Implementation
countingSort(array, size)
  max <- find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
'''
import random

list=[]
for i in range(10):
    r = random.randint(1,10)
    list.append(r)

print("Unsorted")
print(list)

def counting_sort_without_negative(list):
    sorted = [0] * len(list)

    count_arr = [0] * (len(list) + 1) # to store the count of each number

    # count occurence of each number
    for j in range(0,len(list)):
        # count = 0
        # if(list[j]):
        # count += 1
        count_arr[list[j]] += 1

    # do the running sum
    for k in range(1,len(list)+1):
        count_arr[k] += count_arr[k-1]

    i = len(list) - 1
    while i >= 0:
        sorted[count_arr[list[i]] - 1] = list[i]
        count_arr[list[i]] -= 1
        i -= 1

    for n in range(0,len(list)):
        list[n] = sorted[n]

counting_sort_without_negative(list)
print("Sorted list without negative")
print(list)



list_negative=[]
for i in range(10):
    s = random.randint(-10,8)
    list_negative.append(s)

print("\nUnsorted with negative")
print(list_negative)

def counting_sort_universal(list):
    sorted = [0] * len(list)
    bigg = int(max(list))
    smol = int(min(list))
    ranged = bigg - smol + 1
    count_arr = [0] * ranged
    # count_arr = [0 for _ in range(ranged)]

    # store in count array
    for j in range(0,len(list)):
        count_arr[list[j] - smol] += 1

    # do running sum
    for k in range(1,len(count_arr)):
        count_arr[k] += count_arr[k-1]

    # store the numbers in count array and decrease it
    for i in range(len(list)-1,-1,-1):
        sorted[count_arr[list[i] - smol]-1] = list[i]
        count_arr[list[i]-smol] -= 1

    for n in range(0,len(list)):
        list[n] = sorted[n]


counting_sort_universal(list_negative)
print("Sorted with negative numbers")
print(list_negative)