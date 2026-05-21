"""
http://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=problem-list-v2&envId=binary-search

Given an array of integers nums sorted in non-decreasing order, find the startPtring and endPtring position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Binary Search + Expansion

        Problem:
        - Find first and last position of target
          in sorted array.

        Idea:
        - First use binary search to find any occurrence
          of target.
        - Once found:
              expand left to find first occurrence
              expand right to find last occurrence

        Note:
        - This solution is simple, but worst-case can be O(n)
          if many elements are equal to target.

        Time Complexity: O(log n + count of target)
        Worst Case: O(n)
        Space Complexity: O(1)
        """

        # Left boundary of search space
        leftPtr = 0

        # Right boundary of search space
        rightPtr = len(nums) - 1

        # Standard binary search
        while leftPtr <= rightPtr:

            # Middle index
            midPtr = (leftPtr + rightPtr) // 2

            # Target found
            if nums[midPtr] == target:

                # Start and end both begin at found index
                startPtr = midPtr
                endPtr = midPtr

                # Move left while previous element is also target
                while (
                    startPtr > 0
                    and nums[startPtr] == nums[startPtr - 1]
                ):
                    startPtr -= 1

                # Move right while next element is also target
                while (
                    endPtr < len(nums) - 1
                    and nums[endPtr] == nums[endPtr + 1]
                ):
                    endPtr += 1

                # Return first and last position
                return [startPtr, endPtr]

            # Target is larger, search right side
            elif nums[midPtr] < target:
                leftPtr = midPtr + 1

            # Target is smaller, search left side
            else:
                rightPtr = midPtr - 1

        # Target not found
        return [-1, -1]
