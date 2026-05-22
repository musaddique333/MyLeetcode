"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=binary-search

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.


Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.


Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 



Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Binary Search on Rotated Sorted Array

        Problem:
        - Array was originally sorted in ascending order,
          then rotated.
        - Find minimum element in O(log n).

        Key Observation:
        - One half of the array is always sorted.
        - Minimum element exists in the unsorted portion.
        - If entire current range is sorted:
              leftmost element is minimum.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        # Search boundaries
        leftPtr = 0
        rightPtr = len(nums) - 1

        # Binary search
        while leftPtr <= rightPtr:

            # Middle index
            midPtr = (leftPtr + rightPtr) // 2

            # Case 1:
            # Left half is sorted
            if nums[leftPtr] <= nums[midPtr]:

                # Entire current range is sorted
                #
                # Example:
                # [1,2,3,4,5]
                #
                # Minimum is leftmost element
                if nums[leftPtr] <= nums[rightPtr]:
                    return nums[leftPtr]

                # Minimum must be in right half
                #
                # Example:
                # [4,5,6,7,0,1,2]
                leftPtr = midPtr + 1

            # Case 2:
            # Rotation point exists in left half
            else:

                # Check if mid itself is minimum
                #
                # Example:
                # [4,5,6,0,1,2]
                if nums[midPtr] < nums[midPtr - 1]:
                    return nums[midPtr]

                # Otherwise minimum lies further left
                rightPtr = midPtr - 1

        # Fallback return
        return nums[leftPtr]