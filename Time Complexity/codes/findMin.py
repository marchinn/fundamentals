def findMinimum (arr):
    min = arr[0]

    for num in arr:
        if num < min:
            min = num
    
    return min

print (findMinimum([5, 7, 2, 0, -3, 1, 1, 7])) # output is -3
print (findMinimum([5, 7])) # output is 5