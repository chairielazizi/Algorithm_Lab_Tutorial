'''
Implementation
radixSort(array)
  d <- maximum number of digits in the largest element
  create d buckets of size 0-9
  for i <- 0 to d
    sort the elements according to ith place digits using countingSort

countingSort(array, d)
  max <- find largest element among dth place elements
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique digit in dth place of elements and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
'''
import random

list = []
for i in range(10):
    r = random.randint(1,20)
    list.append(r)

print("Unsorted list")
print(list)

def counting_sort(list,digit):
    length = len(list)
    sorted = [0] * length
    # bigg = max(list)
    # smol = min(list)
    # ranged = bigg - smol + 1
    count_arr = [0] * (length + 1)

    # calculate num of occurence
    for k in range(0,length):
        index = list[k] // digit
        count_arr[index % 10] += 1

    # do running sum
    for j in range(1,len(count_arr)):
        count_arr[j] += count_arr[j-1]

    # put digit in sorted
    for i in range(length - 1,-1,-1):
        index = list[i] // digit
        sorted[count_arr[index % 10]-1] = list[i]
        count_arr[index % 10] -= 1

    for n in range(0,length):
        list[n] =  sorted[n]

def radix_sort(list):
    bigg = max(list)
    digit = 1

    while(bigg // digit > 0):
        counting_sort(list,digit)
        digit *= 10

# counting_sort(list)
radix_sort(list)
print("\nsorted list")
print(list)