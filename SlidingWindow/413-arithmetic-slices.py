"""
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Dynamic Programming / Running Count

        Arithmetic Slice:
        - A subarray with at least 3 elements
        - Difference between consecutive elements is constant

        Idea:
        - If current 3 numbers form arithmetic sequence:
              nums[i] - nums[i-1] == nums[i-1] - nums[i-2]

          then:
          - previous arithmetic sequences can be extended
          - plus one new sequence of length 3 is formed

        currEleSeq:
        - Number of arithmetic slices ending at current index

        totalEleSeq:
        - Total arithmetic slices in entire array

        Example:
        nums = [1,2,3,4]

        At index 2:
            [1,2,3]
            currEleSeq = 1

        At index 3:
            [2,3,4]
            [1,2,3,4]
            currEleSeq = 2

        Total = 1 + 2 = 3

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)

        # Need at least 3 elements
        if n < 3:
            return 0

        # Number of arithmetic slices ending at current index
        currEleSeq = 0

        # Stores total arithmetic slices
        totalEleSeq = 0

        # Start checking from index 2
        for i in range(2, n):

            # Check if current 3 elements maintain same difference
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:

                # Extend previous sequences
                # + form one new length-3 sequence
                currEleSeq += 1

                # Add all sequences ending at current index
                totalEleSeq += currEleSeq

            else:
                # Sequence broken
                currEleSeq = 0

        return totalEleSeq