"""
https://leetcode.com/problems/4sum/description/?envType=problem-list-v2&envId=two-pointers

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Sorting + Two Pointers

        Idea:
        - Sort the array.
        - Fix first number using firstPtr.
        - Fix second number using secondPtr.
        - Then use two pointers to find remaining two numbers.

        Duplicate handling:
        - Skip duplicate firstPtr values.
        - Skip duplicate secondPtr values.
        - After finding one valid quadruplet,
          skip duplicate leftPtr and rightPtr values.

        Time Complexity: O(n^3)
        Space Complexity: O(1), ignoring output
        """

        n = len(nums)

        # Need at least 4 numbers to form quadruplet
        if n < 4:
            return []

        # Sort array so two-pointer movement works
        nums.sort()

        # Stores all unique quadruplets
        result = []

        # Fix first number
        for firstPtr in range(n):

            # Skip duplicate first numbers
            if firstPtr > 0 and nums[firstPtr] == nums[firstPtr - 1]:
                continue

            # Fix second number
            for secondPtr in range(firstPtr + 1, n):

                # Skip duplicate second numbers
                if (
                    secondPtr > firstPtr + 1
                    and nums[secondPtr] == nums[secondPtr - 1]
                ):
                    continue

                # Left pointer starts after secondPtr
                leftPtr = secondPtr + 1

                # Right pointer starts at end
                rightPtr = n - 1

                # Find remaining two numbers
                while leftPtr < rightPtr:

                    # Current sum of four numbers
                    fSum = (
                        nums[firstPtr]
                        + nums[secondPtr]
                        + nums[leftPtr]
                        + nums[rightPtr]
                    )

                    if fSum == target:
                        # Found valid quadruplet
                        result.append([
                            nums[firstPtr],
                            nums[secondPtr],
                            nums[leftPtr],
                            nums[rightPtr]
                        ])

                        # Move both pointers after finding answer
                        leftPtr += 1
                        rightPtr -= 1

                        # Skip duplicate left values
                        while (
                            leftPtr < rightPtr
                            and nums[leftPtr] == nums[leftPtr - 1]
                        ):
                            leftPtr += 1

                        # Skip duplicate right values
                        while (
                            leftPtr < rightPtr
                            and nums[rightPtr] == nums[rightPtr + 1]
                        ):
                            rightPtr -= 1

                    elif fSum > target:
                        # Sum too large, need smaller value
                        rightPtr -= 1

                    else:
                        # Sum too small, need larger value
                        leftPtr += 1

        return result