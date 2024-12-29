def generateSubsets(symbols):
    result = []
    
    def backtrack(start, path):
        result.append(path)

        for i in range(start, len(symbols)):
            backtrack(i + 1, path + [symbols[i]])
    
    backtrack(0, [])
    return result

print( generateSubsets([1, 2]) ) # output is [[], [1], [1, 2], [2]]
print( generateSubsets(["a", "b", "c"]) ) # output is [[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'c'], ['b'], ['b', 'c'], ['c']]
