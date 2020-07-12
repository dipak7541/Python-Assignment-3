def insertionSort(list):
    for i in range(0,len(list)):
        key=list[i]
        j=i-1
        while(j>=0 and key<list[j]):
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
my_list=[11,23,43,12,45,32,54,23]
insertionSort(my_list)
for i in range(len(my_list)):
    print("% d" % my_list[i])
