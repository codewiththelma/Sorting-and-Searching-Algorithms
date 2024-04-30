# Binary Search
def binary_search(arr, target):
    """
    Author: Thelma Ofoegbu
    Purpose:Perform binary search on a sorted list to find the target value.
    index: The index of the target value in the list if found, otherwise -1.
    """
    left = 0             # Initialize left pointer
    right = len(arr) - 1 # Initialize right pointer
    
    while left <= right:
        mid = (left + right) // 2  # Calculate mid index
        
        if arr[mid] == target:
            return mid             # Target found, return index
        
        elif arr[mid] < target:
            left = mid + 1         # Target may be in the right half
            
        else:
            right = mid - 1        # Target may be in the left half
    
    return -1                      # Target not found

#Binary Search needs your list to be sorted but linear search doesnt care
#Binary Search is faster than a linear search if you have a very large list
#Time complexity of Binary Search= O(log)n
#Time complexity of Linear Search= O(n)