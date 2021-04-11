# def merge(arr=[], p=0, q=0, r=0):
#     n1 = q - p + 1
#     n2 = r - q
#
#     half1 = [n1]
#     half2 = [n2]
#
#     for i in range(n1):
#         half1[i] = arr[p + i]
#
#     for j in range(n2):
#         half2[j] = arr[q + 1 + j]
#
#     i, j = 0, 0
#     k = p
#
#     # compare the value between 2 half
#     while(i < n1 and j < n2):
#         if(half1[i] < half2[j]):
#             arr[k] = half1[i]
#             i += 1
#         else:
#             arr[k] = half2[j]
#             j += 1
#         k += 1
#
#         while(i < n1):
#             arr[k] = half1[i]
#             i += 1
#             j += 1
#
#         while(j < n2):
#             arr[k] = half2[j]
#             j += 1
#             k += 1
#
#
# def merge_sort(arr = [], left=0, right=0):
#     if(left < right):
#         middle = (left + right) / 2
#
#         merge_sort(arr, 1, int(middle))
#         merge_sort(arr, int(middle + 1), right)
#
#         # merge the sorted array
#         merge(arr, left, int(middle), right)

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        # divide the array into half
        left = arr[:middle]
        right = arr[middle:]
        # print(left)

        merge_sort(left)
        merge_sort(right)

        # i for track first half,j for second half, and k for sorted array
        i,j,k = 0,0,0


        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def print_list(array):
    for a in range(len(array)):
        print(array[a])

import random
list = []
for i in range(10):
    r = random.randint(1,10)
    list.append(r)

print("Unsorted list")
print(list)

# merge_sort(list, 0, len(list) - 1)
merge_sort(list)
print("\nSorted list:")
# print_list(list)
print(list)