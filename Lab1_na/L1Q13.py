def check(a):
    print("Original list:")
    print(a)
    new_list=[]
    for i in a:
        if i not in new_list:
            new_list.append(i)
    print("Non-duplicate list:")
    print(new_list)

a=[2,4,4,6,7,9,9,12,23,34,34]
check(a)