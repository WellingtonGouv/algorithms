# Linear Search

In __Linear Search__, we iterate over all the elements of the array and check if it the current element is equal to the target element. If we find any element to be equal to the target element, then return the index of the current element. Otherwise, if no element is equal to the target element, then return -1 as the element is not found. Linear search is also known as __sequential search__.

## Implementation

```python
def linear_search(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if (nums[i] == target):
            return i
    return -1
```
### Complexity Analysis
#### Time Complexity:
- __Best Case__: In the best case, the key might be present at the first index. So the best case complexity is O(1)
- __Worst Case__: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
- __Average Case__: O(N)
  
__Auxiliary Space__: O(1) as except for the variable to iterate through the list, no other variable is used. 

## Applications of Linear Search Algorithm:
- __Unsorted Lists__: When we have an unsorted array or list, linear search is most commonly used to find any element in the collection.
- __Small Data Sets__: Linear Search is preferred over binary search when we have small data sets with
- __Searching Linked Lists__: In linked list implementations, linear search is commonly used to find elements within the list. Each node is checked sequentially until the desired element is found.
- __Simple Implementation__: Linear Search is much easier to understand and implement as compared to Binary Search or Ternary Search.

### Advantages of Linear Search Algorithm:
- Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
- Does not require any additional memory.
- It is a well-suited algorithm for small datasets.
  
### Disadvantages of Linear Search Algorithm:
- Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
- Not suitable for large arrays.

### When to use Linear Search Algorithm?
- When we are dealing with a small dataset.
- When you are searching for a dataset stored in contiguous memory.

Source: https://www.geeksforgeeks.org/dsa/linear-search/