# an iterative binary search function

def binSearch(arr: list, target: int) -> int:

    # define the highest and lowest indices of the array
    # which will always be 0 and the length of the array -1 at the start of the algorithm
    high, low = len(arr) - 1, 0
    
    # looping until the subset of the array becomes too small
    while high >= low:

        # define the middle value as the lower value plus half the difference between the high and low (rounded down)
        mid = low + ((high - low) // 2)

        # if the value is greater than the target, we need to discard the right half of the array
        if arr[mid] > target:
            high = mid-1
        
        # if the value is less than the target, we discard the left half
        elif arr[mid] < target:
            low = mid+1

        # if the value is the same as the target return mid
        elif arr[mid] == target:
            return mid
    
    # if we traverse the full loop without finding the target, the target cannot be in the array
    return -1
        
print(binSearch([1,2,3,4,6,9,10,11], 11))