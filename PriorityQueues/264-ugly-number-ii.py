"""
https://leetcode.com/problems/ugly-number-ii/description/?envType=problem-list-v2&envId=heap-priority-queue

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Min Heap + HashSet

        Ugly Number:
        - Positive number whose prime factors
          are only 2, 3, and 5.

        Idea:
        - Start from 1.
        - Repeatedly generate next ugly numbers by:
              current * 2
              current * 3
              current * 5
        - Use min heap to always get smallest unseen ugly number.
        - Use hashset to avoid duplicates.

        Example:
        Start:
            1

        Generate:
            2, 3, 5

        Then from 2:
            4, 6, 10

        Continue in increasing order.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        # Min heap storing ugly numbers
        uglyNumHeap = [1]

        # Stores already generated ugly numbers
        # to avoid duplicates
        seenUglyNum = {1}

        # Generate ugly numbers n times
        for _ in range(n):

            # Smallest ugly number available
            nxtUglyNum = heapq.heappop(uglyNumHeap)

            # Generate next possible ugly numbers
            for multiplier in [2, 3, 5]:

                # New ugly number candidate
                uglyNum = nxtUglyNum * multiplier

                # Add only if not already generated
                if uglyNum not in seenUglyNum:

                    # Push into heap
                    heapq.heappush(
                        uglyNumHeap,
                        uglyNum
                    )

                    # Mark as seen
                    seenUglyNum.add(uglyNum)

        # nth popped ugly number
        return nxtUglyNum