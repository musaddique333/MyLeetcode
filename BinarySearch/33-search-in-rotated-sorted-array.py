"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=binary-search

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


Example 3:

Input: nums = [1], target = 0
Output: -1
"""

class Solution:
    def search(
        self,
        nums: List[int],
        target: int
    ) -> int:
        """
        Binary Search on Rotated Sorted Array

        Problem:
        - Array was originally sorted,
          then rotated at some pivot.
        - Search target in O(log n) time.

        Key Observation:
        - At least one half of the array
          is always sorted.

        Strategy:
        1. Find middle element.
        2. Determine which half is sorted.
        3. Check whether target belongs
           inside the sorted half.
        4. Discard the other half.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        # Left boundary of search space
        leftPointer = 0

        # Right boundary of search space
        rightPointer = len(nums) - 1

        # Continue while search space exists
        while leftPointer <= rightPointer:

            # Middle index
            midPointer = (
                leftPointer + rightPointer
            ) // 2

            # Target found
            if nums[midPointer] == target:
                return midPointer

            # Case 1:
            # Left half is sorted
            #
            # Example:
            # [4,5,6,7,0,1,2]
            #  ^-----sorted---^
            if nums[leftPointer] <= nums[midPointer]:

                # Check if target lies inside
                # sorted left half
                if (
                    nums[leftPointer]
                    <= target
                    < nums[midPointer]
                ):

                    # Search left half
                    rightPointer = midPointer - 1

                else:
                    # Search right half
                    leftPointer = midPointer + 1

            # Case 2:
            # Right half is sorted
            #
            # Example:
            # [6,7,0,1,2,4,5]
            #          ^---sorted---^
            else:

                # Check if target lies inside
                # sorted right half
                if (
                    nums[midPointer]
                    < target
                    <= nums[rightPointer]
                ):

                    # Search right half
                    leftPointer = midPointer + 1

                else:
                    # Search left half
                    rightPointer = midPointer - 1

        # Target not found
        return -1