a=[1,4,9,16,25,36,49,64,81,100]
even=[]

for i in range(0,len(a),1):
    if a[i]%2==0:
        even.append(a[i])
        print(a[i])
