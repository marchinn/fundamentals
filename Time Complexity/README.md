# Time complexity _Big O_

Time complexity is a measure that indicates the amount of time required to execute an algorithm, typically expressed in terms of worst-case time complexity. The notation used is _O(n)_, where _n_ represents the size of the input data processed by the algorithm. So, the worst-case time complexity refers to the maximum size of data that the algorithm can process.

## How it works?
As it was noticed above, the time complexity's argument _n_ is the volume of data that can be processed. In most instances, _n_ is the largest data size that may be observed in algorithm and in practically using this is achieved by discarding the lesser parts of expression and less significant components of the time complexity equation.

> For example: If the time required to complete the algorithm  is expressed as _n^3 + 5n^2 + 9n + 100_, the worst-case-time-complexity will be represented as _O(n^3)_ as it reflects the higher power and the coefficients aren't important. Even if the expression is _30000n_, the time complexity would still be classified as _O(n)_

## Why is it important?
ML is interrupted refers to processing large datasets. In instances involving huge number of operations the use of algorithms with time complexities of O(n^2) and higher is ineffective as they operate more slowly than necessary and may lead to different errors and crashes during runtime an algorithm.
Also it is important to make useful and rapid operational processes, particularly in contexts involving client interactions, such as searching for a specific item in a shopping catalog or transmitting data to numerous services. A Wrong choice of the time complexity can result in company looses, server failures and decreasing conversion.

## Commonly in ML are used following types of time complexity:

### _O(1)_
The best time complexity is considered an _O(1)_, where the required time remains constant. It means that the operation runtime doesn't increase with growing volume of data.

For example, taking the last element in array:
####
```python
def getLastElement (arr):
    print (arr[-1])

getLastElement([1,2,3,4,5,6,7,8,9]) # output is 9
getLastElement(['try','to','find','the','last']) # output is last

a='first'
b='second'
c='third'
getLastElement([a,b,c]) # output is third
```
In that case we need to complete only one operation, so it doesn't matter how many elements the array contains.
In practice, achieving constant time complexity is challenging, as it typically needs handling a larger scale of operations.

### _O(n)_
_O(n)_ means that time of processing is growing proportional volume of data.

For example, finding the minimum value in an unsorted array:
####
```python
def findMinimum (arr):
    min = arr[0]

    for num in arr:
        if num < min:
            min = num
    
    return min

print (findMinimum([5, 7, 2, 0, -3, 1, 1, 7])) # output is -3
print (findMinimum([5, 7])) # output is 5
```
As the size of an array increases, so does the time required to process an operation. With an growing volume of data, the time complexity also proportionally grow. In the first case we must check eight elements, whereas in the second we only need to check two. Thus, the time complexity in the second case is four times lower than in the first.

### _O(n log n)_
In time complexity _O(n)_ required time is growing more than equal proportion between volume of data and time, but not so fast.

The example below shows how binary search works:
####
```python
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
```
As we can see, the volume of data doubled, but it appended only one step to complete an operation, yet it only added one additional step to complete the operation. Time complexity has increased, but it has not doubled in proportion to the array's growth. This phenomenon is referred to as _logarithmic time complexity_.

### _O(n^2)_
_O(n)_ means that the processing time increases in direct proportion to a doubled volume of data.

The code below is designed to generate an array containing all possible multiplied pairs of the elements from the original array:
####
```python
def multiplyPairs(arr):
    pairs = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
           pairs.append(arr[i] * arr[j])

    return pairs

print(multiplyPairs([1, 2])) # output is [1, 2, 2, 4]
print(multiplyPairs([1, 2, 3, 4])) # output is [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]
```
When the array consists of only two elements, we must evaluate 4 operations. In the case of an array with four elements, the total number of operations required to compute all possible multiplied pairs is 16. The quadratic dependence on the volume of data in the algorithm is evident.