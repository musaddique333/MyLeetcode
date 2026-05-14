"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=problem-list-v2&envId=two-pointers

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two Pointers

        Problem:
        - Sorted array is given.
        - Each element can appear at most 2 times.
        - Modify array in-place and return new length.

        Idea:
        - First 2 elements are always valid.
        - Start writing from index 2.
        - For every new number:
              compare with element at repeatedIdx - 2

        Why repeatedIdx - 2:
        - If current number equals nums[repeatedIdx - 2],
          then adding it would create more than 2 duplicates.
        - Otherwise it is safe to keep.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)

        # Arrays with size <= 2 are already valid
        if n <= 2:
            return n

        # Position where next valid element should be placed
        repeatedIdx = 2

        # Start checking from third element
        for currIdx in range(2, n):

            # If current number is different from
            # element two places behind,
            # it means current number has appeared
            # less than 2 times so far
            if nums[currIdx] != nums[repeatedIdx - 2]:

                # Place valid element
                nums[repeatedIdx] = nums[currIdx]

                # Move insertion pointer
                repeatedIdx += 1

        # repeatedIdx becomes new valid length
        return repeatedIdx


        """
        Alternative HashMap Solution
        Time Complexity: O(n)
        Space Complexity: O(n)

        # count = {}
        # k = 0
        #
        # for num in nums:
        #
        #     # Count occurrences
        #     count[num] = count.get(num, 0) + 1
        #
        #     # Keep number only if frequency <= 2
        #     if count[num] <= 2:
        #         nums[k] = num
        #         k += 1
        #
        # return k
        """