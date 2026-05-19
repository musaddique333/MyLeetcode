"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/?envType=problem-list-v2&envId=heap-priority-queue

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Greedy + HashMaps

        Problem:
        - Split array into consecutive subsequences.
        - Every subsequence must have length >= 3.

        Greedy Strategy:
        1. First try extending an existing subsequence.
        2. If not possible:
              try creating a new subsequence
              of length 3.
        3. If neither is possible:
              answer is False.

        Why extending first is important:
        - Smaller unfinished subsequences are harder to complete later.
        - So always prioritize extending them.

        freqCounter:
        - Stores remaining unused numbers.

        endWithKDict:
        - endWithKDict[x] =
              number of subsequences ending at x

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Frequency of all numbers
        freqCounter = collections.Counter(nums)

        # Stores how many subsequences end with a number
        endWithKDict = collections.defaultdict(int)

        # Process numbers in sorted order
        for num in nums:

            # Number already used completely
            if freqCounter[num] == 0:
                continue

            # Use current number
            freqCounter[num] -= 1

            # Previous consecutive number
            prevNum = num - 1

            # Next consecutive numbers
            nextNum = num + 1
            secondNextNum = num + 2

            # Case 1:
            # Extend an existing subsequence
            #
            # Example:
            # [1,2,3] + 4
            if endWithKDict[prevNum] > 0:

                # One subsequence ending at prevNum
                # is now extended to end at num
                endWithKDict[prevNum] -= 1
                endWithKDict[num] += 1

            # Case 2:
            # Create a new subsequence:
            # num, num+1, num+2
            elif (
                freqCounter[nextNum] > 0
                and freqCounter[secondNextNum] > 0
            ):

                # Use next two numbers
                freqCounter[nextNum] -= 1
                freqCounter[secondNextNum] -= 1

                # New subsequence now ends at secondNextNum
                endWithKDict[secondNextNum] += 1

            # Case 3:
            # Neither extending nor creating possible
            else:
                return False

        return True