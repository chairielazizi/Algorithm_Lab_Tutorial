'''
Implementation
shellSort(array, size)
  for interval i <- size/2n down to 1
    for each interval "i" in array
        sort all the elements at interval "i"
end shellSort
'''

import random

list = []
for i in range(10):
    r = random.randint(1, 10)
    list.append(r)

print("Unsorted")
print(list)

def shell_sort(list, size):
    # for n/2,n/4,n/8,...
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            # make a temporary var to store the current number
            temp = list[i]
            j = i
            while j >= gap and list[j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap

            list[j] = temp
        gap = gap // 2

shell_sort(list,len(list))
print("Sorted list")
print(list)
