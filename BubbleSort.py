def bubblesort(list):
    for i in range(0,len(list)):      
       for j in range(0,len(list)-i-1):  
           if (list[j] > list[j+1]): 
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
list=[14,46,43,27,57,41,45,21,70]
bubblesort(list)
print(list)
