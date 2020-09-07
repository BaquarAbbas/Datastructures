def Binarysearch(arr,item):
    beg_index = 0
    end_index = len(arr)-1
    while(beg_index <= end_index):
        mid_index = int((beg_index+end_index)/2)
        if item == arr[mid_index]:
            return mid_index
        elif item > arr[mid_index]:
            beg_index = mid_index +1
        else:
            end_index = mid_index -1

    return False

arr1 = [-4,5,6,8,9,11,12,14]    
print(Binarysearch(arr1,14))

n = int(input("Enter the size of array or list:"))
arr2 = []
for i in range(n):
    i = int(input("Enter the element in list: ["+str(i)+"]"))
    arr2.append(i)
item= int(input("Enter search item"))
index = Binarysearch(arr2,item)
if index:
    print("Element Found in ",index)
else:
    print("Not found")
