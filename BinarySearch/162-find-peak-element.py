"""
https://leetcode.com/problems/find-peak-element/?envType=problem-list-v2&envId=binary-search

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.


Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Binary Search

        Peak Element:
        - Element strictly greater than neighbours.

        Key Observation:
        - If nums[mid] < nums[mid + 1]:
              peak must exist on right side.
        - Otherwise:
              peak exists on left side (including mid).

        Why:
        - Moving toward increasing slope always leads
          to a peak eventually.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        # Search boundaries
        leftPtr = 0
        rightPtr = len(nums) - 1

        # Continue until both pointers meet
        while leftPtr < rightPtr:

            # Middle index
            midPtr = leftPtr + (
                (rightPtr - leftPtr) // 2
            )

            # Increasing slope
            #
            # Example:
            # [1,2,3,4]
            #          ^
            #
            # Peak must exist on right side
            if nums[midPtr] < nums[midPtr + 1]:
                leftPtr = midPtr + 1

            # Decreasing slope
            #
            # Example:
            # [4,3,2,1]
            #  ^
            #
            # Peak exists on left side including mid
            else:
                rightPtr = midPtr

        # leftPtr == rightPtr
        # This index is peak element
        return leftPtr