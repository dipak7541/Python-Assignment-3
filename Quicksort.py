def partition(my_list,low,high): 
    i = ( low-1 )
    pivot = my_list[high]     
    for j in range(low , high): 
        if   my_list[j] <= pivot: 
            i = i+1 
            my_list[i],my_list[j] = my_list[j],my_list[i] 
  
    my_list[i+1],my_list[high] = my_list[high],my_list[i+1] 
    return ( i+1 )

def quickSort(my_list,low,high): 
    if low < high: 
        pi = partition(my_list,low,high) 
        quickSort(my_list, low, pi-1) 
        quickSort(my_list, pi+1, high) 
  
# Driver code to test above 
my_list = [10, 7, 8, 9, 1, 5] 
n = len(my_list) 
quickSort(my_list,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %my_list[i]),
