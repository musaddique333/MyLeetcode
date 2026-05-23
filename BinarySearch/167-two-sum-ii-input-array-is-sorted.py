"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=binary-search

iven a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].



Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import List

class Solution:
    def twoSum(
        self,
        numbers: List[int],
        target: int
    ) -> List[int]:
        """
        Binary Search

        Problem:
        - Array is sorted in ascending order.
        - Find two numbers whose sum equals target.
        - Return 1-based indexes.

        Idea:
        - Fix first number using index i.
        - Search for:
              target - numbers[i]
          using binary search on remaining right side.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """

        def binarySearch(
            leftPtr: int,
            rightPtr: int,
            targetValue: int
        ) -> int:
            """
            Standard binary search

            Returns:
            - index of targetValue if found
            - -1 otherwise
            """

            while leftPtr <= rightPtr:

                # Middle index
                midPtr = leftPtr + (
                    (rightPtr - leftPtr) // 2
                )

                # Target found
                if numbers[midPtr] == targetValue:
                    return midPtr

                # Search right half
                if targetValue > numbers[midPtr]:
                    leftPtr = midPtr + 1

                # Search left half
                else:
                    rightPtr = midPtr - 1

            return -1

        # Fix first number
        for i in range(len(numbers) - 1):

            # Find complement using binary search
            #
            # complement =
            # target - current number
            j = binarySearch(
                i + 1,
                len(numbers) - 1,
                target - numbers[i]
            )

            # Pair found
            if j != -1:

                # Problem requires 1-based indexing
                return [i + 1, j + 1]

        # No valid pair found
        return [-1, -1]

        """
        Two Pointers (Optimal Solution)

        Problem:
        - Array is sorted in ascending order.
        - Find two numbers whose sum equals target.
        - Return 1-based indexes.

        Key Observation:
        - Since array is sorted:
              increasing left pointer increases sum
              decreasing right pointer decreases sum

        Strategy:
        - Start with:
              left pointer at beginning
              right pointer at end
        - Compare current sum with target.
        - Move pointers accordingly.

        Time Complexity: O(n)
        """
        # Left boundary
        leftPtr = 0

        # Right boundary
        rightPtr = len(nums) - 1

        # Continue until pointers meet
        while leftPtr < rightPtr:

            # Current pair sum
            total = nums[leftPtr] + nums[rightPtr]

            # Pair found
            if total == target:

                # Problem requires 1-based indexing
                return [leftPtr + 1, rightPtr + 1]

            # Sum too small,
            # need larger value
            if total < target:
                leftPtr += 1

            # Sum too large,
            # need smaller value
            else:
                rightPtr -= 1

        # No valid pair found
        return [-1, -1]
