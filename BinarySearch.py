def binarySearch(my_list,key,low,high):
    mid=int(low+high/2)
    if low>high:
        if key==my_list[mid]:
            return mid;
        elif key<mid:
            return binarySearch(my_list,key,low,mid-1)
        else:
            return binarySearch(my_list,key,mid+1,high)
    else:
        return -1

my_list=[1,2,4,5,7,8,9]
low=0
high=len(my_list)
key=6
result=binarySearch(my_list,key,low,high)
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
        
