def multiplyPairs(arr):
    pairs = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
           pairs.append(arr[i] * arr[j])

    return pairs

print(multiplyPairs([1, 2])) # output is [1, 2, 2, 4]
print(multiplyPairs([1, 2, 3, 4])) # output is [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]