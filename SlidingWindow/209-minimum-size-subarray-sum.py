"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding Window

        Idea:
        - Maintain a running sum of the current window.
        - Expand window using rightPtr by adding new elements.
        - Once window sum becomes >= target:
            try shrinking from the left side
            to find the smallest valid subarray.

        Since all numbers are positive:
        - Expanding increases sum
        - Shrinking decreases sum
        This makes sliding window possible.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Stores current window sum
        currSum = 0

        # Stores minimum valid window length found so far
        minLength = float("inf")

        # Left boundary of sliding window
        leftPtr = 0

        n = len(nums)

        # Expand window using right pointer
        for rightPtr in range(n):

            # Add current element into window
            currSum += nums[rightPtr]

            # While current window satisfies condition
            while currSum >= target:

                # Update minimum valid window length
                minLength = min(
                    minLength,
                    rightPtr - leftPtr + 1
                )

                # Remove left element from window
                currSum -= nums[leftPtr]

                # Shrink window from left side
                leftPtr += 1

        # If no valid subarray found, return 0
        return minLength if minLength != float("inf") else 0