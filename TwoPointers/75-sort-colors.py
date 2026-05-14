"""
https://leetcode.com/problems/sort-colors/submissions/2003097752/?envType=problem-list-v2&envId=two-pointers

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag Algorithm

        Problem:
        - Sort array containing only:
              0, 1, 2
        - In-place without using extra space.

        Idea:
        Maintain 3 regions:

            [0 ... leftPtr-1]      -> all 0s
            [leftPtr ... midPtr-1] -> all 1s
            [midPtr ... rightPtr]  -> unknown
            [rightPtr+1 ... end]   -> all 2s

        Pointer meanings:
        - leftPtr:
              position where next 0 should go
        - midPtr:
              current element being processed
        - rightPtr:
              position where next 2 should go

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)

        # midPtr traverses array
        midPtr = 0

        # Boundary for placing 0s
        leftPtr = 0

        # Boundary for placing 2s
        rightPtr = n - 1

        # Process until unknown region becomes empty
        while midPtr <= rightPtr:

            # Current element is 0
            if nums[midPtr] == 0:

                # Place 0 in left region
                nums[midPtr], nums[leftPtr] = (
                    nums[leftPtr],
                    nums[midPtr]
                )

                # Expand 0 region
                leftPtr += 1

                # Move to next element
                #
                # Safe because swapped value before leftPtr
                # is already processed
                midPtr += 1

            # Current element is 1
            elif nums[midPtr] == 1:

                # 1 already belongs in middle region
                midPtr += 1

            # Current element is 2
            else:

                # Place 2 in right region
                nums[midPtr], nums[rightPtr] = (
                    nums[rightPtr],
                    nums[midPtr]
                )

                # Expand 2 region
                rightPtr -= 1

                # DO NOT increment midPtr here
                #
                # Reason:
                # swapped element from right side
                # is unprocessed and must be checked again