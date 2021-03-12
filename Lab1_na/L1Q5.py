a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]

c=set(a).intersection(b)
#c=set(a) & set(b) (can also use this)
print("The common elements in both lists are:")
print(c)