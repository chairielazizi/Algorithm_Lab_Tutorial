a = [5,10,15,20,25]

def newList(a):
    new = []

    new.append(a[0])
    new.append(a[-1])

    return new

print(newList(a))