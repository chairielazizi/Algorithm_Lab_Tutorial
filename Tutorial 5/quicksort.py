import random

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1
    j = low
    while j <= high - 1:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    # for j in range(low, high):
    #     if arr[j] < pivot:
    #         i += 1
    #         arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)

        quick_sort(arr, low, partition_index - 1) #before par index
        quick_sort(arr, partition_index + 1, high) #after par index

list = []
for i in range(10):
    r = random.randint(1,20)
    list.append(r)

print("Unsorted list")
print(list)

quick_sort(list, 0, len(list) - 1)
print("\nSorted list:")
print(list)