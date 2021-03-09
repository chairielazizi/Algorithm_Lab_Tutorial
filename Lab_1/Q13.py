listA = [1,2,3,1,2,5,6,7]
# listB = ["chameleon","dog","bonk","beaver","pig"]

def delete_duplicate(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

print(delete_duplicate(listA))