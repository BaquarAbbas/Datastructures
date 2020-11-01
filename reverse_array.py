#The problem is that we want to reverse a array in O(n) linear time complexity and also we want the algorithm to be in-place as well?

def reverseArray(array):
    start_idx  = 0
    end_idx = len(array) - 1
    while end_idx > start_idx:
        array[start_idx],array[end_idx] = array[end_idx],array[start_idx]
        start_idx += 1
        end_idx -= 1
    return array
array = [1,3,5,6,8,7]
print("Original array is :",array)
print("Reverse of an array is :",reverseArray(array))
