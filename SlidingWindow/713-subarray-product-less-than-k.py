"""
https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=sliding-window

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Sliding Window

        Idea:
        - Maintain a window where product of all elements is less than k.
        - Expand window using rightPtr.
        - If product becomes >= k, shrink from left side.
        - For every valid window ending at rightPtr:
              number of new valid subarrays =
              rightPtr - leftPtr + 1

        Why this works:
        - nums contains positive integers.
        - So removing elements from left decreases the product.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # If k <= 1, no positive product can be less than k
        if k <= 1:
            return 0

        n = len(nums)

        # Stores total number of valid subarrays
        result = 0

        # Left boundary of sliding window
        leftPtr = 0

        # Product of current window
        currProd = 1

        # Expand window using right pointer
        for rightPtr in range(n):

            # Add current element into product
            currProd *= nums[rightPtr]

            # If product is too large,
            # shrink window from left side
            while currProd >= k:
                currProd //= nums[leftPtr]
                leftPtr += 1

            # All subarrays ending at rightPtr and starting from
            # leftPtr, leftPtr+1, ..., rightPtr are valid
            result += rightPtr - leftPtr + 1

        return result