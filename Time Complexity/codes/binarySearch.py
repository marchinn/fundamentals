def binarySearch(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            print ("position of your number is ", mid)
            return
        
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

binarySearch([1, 2, 3, 4, 5, 6], 5) # output is 4
binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5) # output is also 4