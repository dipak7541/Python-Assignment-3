def linearSearch(my_list,key):
    
    for i in range (0, len(my_list)):
        if key==my_list[i]:
            return i
    return -1

my_list=[2,4,6,8,12,9,10]
key=9
result=linearSearch(my_list,key)
if result==-1:
    print("{} Not Found in given Array".format(key))
else:
    print("{} is in {} index of given array".format(key,result))
