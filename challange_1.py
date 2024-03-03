def b_search(a, size, ele):
    low=0 
    high=size-1
    while(low<=high):
        mid=int((high+low)/2)
        if(a[mid]==ele):
            return mid
        elif(a[mid]<ele):
            low=mid+1
        else:
            high=mid-1
    return -1
a=[2,4,6,8,64,256,512,1024,2048,4096]
element=512
size=len(a)
i=b_search(a,size,element)
if(i==-1):
    print("The element is not present in list.")
else:
    print("The element", element,"is present at index",i)