a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

# method 1
# for i in a:
#     for j in b:
#         if(i==j):
#             c.append(i)

# method 2
if(len(a) < len(b)):
    for i in a:
        if i in b and i not in result:
            result.append(i)
if(len(a) > len(b)):
    for i in b:
        if i in a and i not in result:
            result.append(i)

print(result)

