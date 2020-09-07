def binarysearch(arr,start,end,key):
    if not start < end:
        return -1
        
    mid = (start + end)//2
    if arr[mid] < key:
        return binarysearch(arr,mid+1,end,key)
    elif arr[mid] > key:
        return binarysearch(arr,start,mid,key)
    else:
        return mid

print("Enter the elements in array/list in spaces")
arr = list(map(int,input().split()))
key = int(input("Enter the element to be found"))
index = binarysearch(arr,0,len(arr),key)
if index < 0:
    print("Element not found:")
else:
    print('{} found at index {}'.format(key,index))
