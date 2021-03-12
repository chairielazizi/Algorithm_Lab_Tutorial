def insertionSort(a):
    for j in range(1, len(a), 1):
        key = a[j]
        i = j - 1
        while (i >= 0 and a[i] < key):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

arr = [41, 51, 69, 36, 51, 68]
data = insertionSort(arr)
print(data)

#tutorial git
