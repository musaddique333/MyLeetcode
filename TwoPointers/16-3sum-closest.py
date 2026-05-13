"""
https://leetcode.com/problems/3sum-closest/description/?envType=problem-list-v2&envId=two-pointers

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Sorting + Two Pointers

        Idea:
        - Sort the array first.
        - Fix one number using start.
        - Use two pointers to find the pair that makes
          the sum closest to target.

        Pointer movement:
        - If current sum is smaller than target:
            move leftPtr right to increase sum.
        - If current sum is larger than target:
            move rightPtr left to decrease sum.

        Time Complexity: O(n^2)
        Space Complexity: O(1), ignoring sorting space
        """

        n = len(nums)

        # Sort nums so two-pointer movement works
        nums.sort()

        # Stores closest sum found so far
        closestSum = float("inf")

        # Fix first number of triplet
        for start in range(n):

            # Skip duplicate fixed numbers
            # Not strictly required for correctness,
            # but avoids checking same fixed value again
            if start > 0 and nums[start] == nums[start - 1]:
                continue

            # Left pointer starts after fixed number
            leftPtr = start + 1

            # Right pointer starts at end
            rightPtr = n - 1

            # Search best pair for current fixed number
            while leftPtr < rightPtr:

                # Current sum of three numbers
                threeSum = nums[start] + nums[leftPtr] + nums[rightPtr]

                # If current sum is closer to target,
                # update closestSum
                if abs(threeSum - target) < abs(closestSum - target):
                    closestSum = threeSum

                # Perfect match found
                if threeSum == target:
                    return threeSum

                # Sum too small, need a larger value
                if threeSum < target:
                    leftPtr += 1

                else:
                    # Sum too large, need a smaller value
                    rightPtr -= 1

        return closestSum