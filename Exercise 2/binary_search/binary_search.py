"""
Binary Search in Python
Time Complexity: O(log n) | Space Complexity: O(1)
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(nums, target)
    print(f"Python: Target {target} found at index: {result}")