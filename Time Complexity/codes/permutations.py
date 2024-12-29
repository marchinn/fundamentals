def Permutations(arr):
    result = []
    
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return

        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    backtrack(0)
    return result

print(Permutations([1, 2]) ) # output is [[1, 2], [2, 1]]
print(Permutations([1, 2, 3]) ) # output is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]