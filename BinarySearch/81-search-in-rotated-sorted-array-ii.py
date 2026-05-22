"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/?envType=problem-list-v2&envId=binary-search

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true


Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Binary Search on Rotated Sorted Array with Duplicates

        Problem:
        - Array is sorted, then rotated.
        - Array may contain duplicate values.
        - Return True if target exists.

        Key Issue with duplicates:
        - When nums[leftPtr] == nums[midPtr],
          we cannot confidently know which side is sorted.
        - So we safely shrink the search space by moving leftPtr.

        Time Complexity:
        - Average: O(log n)
        - Worst: O(n), because duplicates may force one-by-one shrinking

        Space Complexity: O(1)
        """

        # Search boundaries
        leftPtr = 0
        rightPtr = len(nums) - 1

        # Standard binary search loop
        while leftPtr <= rightPtr:

            # Middle index
            midPtr = (leftPtr + rightPtr) // 2

            # Target found
            if nums[midPtr] == target:
                return True

            # Duplicate ambiguity case
            #
            # Example:
            # [1, 1, 1, 1, 3, 1]
            #
            # nums[leftPtr] == nums[midPtr]
            # We cannot know which half is sorted,
            # so shrink left side safely.
            if nums[midPtr] == nums[leftPtr]:
                leftPtr += 1
                continue

            # Case 1:
            # Left half is sorted
            if nums[leftPtr] <= nums[midPtr]:

                # Target lies inside sorted left half
                if nums[leftPtr] <= target < nums[midPtr]:
                    rightPtr = midPtr - 1

                else:
                    leftPtr = midPtr + 1

            # Case 2:
            # Right half is sorted
            else:

                # Target lies inside sorted right half
                if nums[midPtr] < target <= nums[rightPtr]:
                    leftPtr = midPtr + 1

                else:
                    rightPtr = midPtr - 1

        # Target not found
        return False