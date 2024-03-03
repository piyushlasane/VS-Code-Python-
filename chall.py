a=[3,4,5,6,7,8,9,2]
i=0
n=int((len(a))/2)
i=0
for i in range (n):
    temp=a[i]
    a[i]=a[n*2-i-1]
    a[n*2-i-1]=temp
print(a)