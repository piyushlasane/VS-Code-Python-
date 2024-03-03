def insertion(a, size, element, index):
    a.append(None)
    for i in range(size,index,-1):
        a[i]=a[i-1]
    a[index]=element
    return 1
a=[2,4,6,8,64,256,512,1024,2048,4096]
element=10
index=4
size=len(a)
print("old list",a)
insertion(a,size,element,index)
size+=1
print("new list",a)