'''
Implementation
bucketSort()
  create N buckets each of which can hold a range of values
  for all the buckets
    initialize each bucket with 0 values
  for all the buckets
    put elements into buckets matching the range
  for all the buckets
    sort elements in each bucket
  gather elements from each bucket
end bucketSort
'''
import random
import decimal

list = []
for i in range(10):
    # r = random.randint(1,2)
    # r = decimal.Decimal(random.randrange(1,2))/100
    r = round(random.uniform(1, 1.99), 2)
    list.append(r)

print("Unsorted")
print(list)

def bucket_sort(list):
    length = len(list)
    bucket = []

    # initialize each bucket with 0 values
    for i in range(length):
        bucket.append([])

    for j in list:
        bucket_index = int(10*j%10)
        bucket[bucket_index].append(j)

    for k in range(length):
        bucket[k] = sorted(bucket[k])

    n = 0
    for i in range(length):
        for j in range(len(bucket[i])):
            list[n] = bucket[i][j]
            n += 1

    return list

bucket_sort(list)
print("Sorted list:")
print(list)
