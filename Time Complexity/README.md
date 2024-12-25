# Time complexity _Big O_

Time complexity is a measure that indicates the amount of time required to execute an algorithm, typically expressed in terms of worst-case time complexity. The notation used is _O(n)_, where _n_ represents the size of the input data processed by the algorithm. So, the worst-case time complexity refers to the maximum size of data that the algorithm can process.

## How it works?
As it was noticed above, the time complexity's argument _n_ is the volume of data that can be processed. In most instances, _n_ is the largest data size that may be observed in algorithm and in practically using this is achieved by discarding the lesser parts of expression and less significant components of the time complexity equation.

> For example: If the time required to complete the algorithm  is expressed as _n^3 + 5n^2 + 9n + 100_, the worst-case-time-complexity will be represented as _O(n^3)_ as it reflects the higher power and the coefficients aren't important. Even if the expression is _30000n_, the time complexity would still be classified as _O(n)_

## Why is it important?
ML is interrupted refers to processing large datasets. In instances involving huge number of operitions the use of algorithms with time complexities of O(n^2) and higher is ineffective as they operate more slowly than necessary and may lead to different errors and crashes during runtime an algorithm.
Also it is important to make useful and rapid operational processes, particularly in contexts involving client interactions, such as searching for a specific item in a shopping catalog or transmitting data to numerous services. A Wrong choice of the time complexity can result in company looses, server failures and decreasing conversion.

## Commonly in ML are used following types of time complexity:

### _O(1)_
The best time complexity is considered an _O(1)_, where the required time remains constant. It means that the operation runtime doesn't increase with growing volume of data.

Example:
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