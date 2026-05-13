"""
https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=two-pointers

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sorting + Two Pointers

        Idea:
        - Sort the array first.
        - Fix one number using start.
        - Then use two pointers to find two other numbers
          whose sum with nums[start] becomes 0.

        Duplicate handling:
        - Skip duplicate start values.
        - After moving leftPtr or rightPtr,
          skip duplicate values to avoid repeated triplets.

        Time Complexity: O(n^2)
        Space Complexity: O(1), ignoring output
        """

        n = len(nums)

        # Sort nums so we can use two pointers
        nums.sort()

        # Stores all unique triplets
        resultArr = []

        # Fix first number of triplet
        for start in range(n):

            # Skip duplicate fixed numbers
            if start > 0 and nums[start] == nums[start - 1]:
                continue

            # Left pointer starts after fixed number
            leftPtr = start + 1

            # Right pointer starts at end
            rightPtr = n - 1

            # Find pairs while pointers do not cross
            while leftPtr < rightPtr:

                # Current sum of three numbers
                threeSum = nums[start] + nums[leftPtr] + nums[rightPtr]

                if threeSum == 0:
                    # Found valid triplet
                    resultArr.append([
                        nums[start],
                        nums[leftPtr],
                        nums[rightPtr]
                    ])

                    # Move both pointers after finding valid triplet
                    leftPtr += 1
                    rightPtr -= 1

                    # Skip duplicate left values
                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr - 1]:
                        leftPtr += 1

                    # Skip duplicate right values
                    while leftPtr < rightPtr and nums[rightPtr] == nums[rightPtr + 1]:
                        rightPtr -= 1

                elif threeSum > 0:
                    # Sum too large, need smaller value
                    rightPtr -= 1

                else:
                    # Sum too small, need larger value
                    leftPtr += 1

        return resultArr