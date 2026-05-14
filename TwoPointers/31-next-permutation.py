"""
https://leetcode.com/problems/next-permutation/description/?envType=problem-list-v2&envId=two-pointers

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory
"""

class Solution:
    def _swap(self, leftPtr, rightPtr, nums):
        # Reverse elements between leftPtr and rightPtr
        while leftPtr < rightPtr:
            nums[leftPtr], nums[rightPtr] = nums[rightPtr], nums[leftPtr]
            rightPtr -= 1
            leftPtr += 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Next Permutation

        Idea:
        - Find the first decreasing point from the right.
        - That index is called pivot.
        - Reverse the right side of pivot to make it sorted ascending.
        - Find the first number greater than pivot.
        - Swap it with pivot.

        If no pivot exists:
        - nums is in descending order.
        - So it is the largest permutation.
        - Reverse entire array to get smallest permutation.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)

        # Stores index where nums[idx] < nums[idx + 1]
        # from right side
        pivot = -1

        # Find pivot from right side
        for idx in range(n - 2, -1, -1):
            if nums[idx] < nums[idx + 1]:
                pivot = idx
                break

        # If no pivot found, array is in descending order
        # Example: [3, 2, 1]
        # Next permutation is [1, 2, 3]
        if pivot == -1:
            self._swap(0, n - 1, nums)
            return

        # Reverse suffix after pivot
        #
        # Before reversing, suffix is in descending order.
        # After reversing, suffix becomes ascending order.
        self._swap(pivot + 1, n - 1, nums)

        # Find first number greater than pivot value
        # in the sorted suffix
        swapIdx = -1

        for idx in range(pivot + 1, n):
            if nums[idx] > nums[pivot]:
                swapIdx = idx
                break

        # Swap pivot with next greater number
        nums[pivot], nums[swapIdx] = nums[swapIdx], nums[pivot]