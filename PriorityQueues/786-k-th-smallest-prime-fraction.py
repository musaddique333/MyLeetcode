"""
https://leetcode.com/problems/k-th-smallest-prime-fraction/description/?envType=problem-list-v2&envId=heap-priority-queue

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].


Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]
"""

class Solution:
    def kthSmallestPrimeFraction(
        self,
        arr: List[int],
        k: int
    ) -> List[int]:
        """
        Max Heap of Size k

        Problem:
        - Find kth smallest fraction:
              arr[i] / arr[j]
          where:
              i < j

        Idea:
        - Generate all possible valid fractions.
        - Maintain a max heap of size k.
        - Heap stores:
              (-fractionValue, numeratorIdx, denominatorIdx)

        Why negative fraction:
        - Python only provides min heap.
        - Using negative values simulates max heap.

        Heap behavior:
        - Heap always keeps k smallest fractions.
        - Largest fraction among them stays on top.
        - If heap size exceeds k:
              remove largest fraction.

        Time Complexity: O(n^2 log k)
        Space Complexity: O(k)
        """

        # Length of input array
        arrayLength = len(arr)

        # Max heap simulated using negative fraction values
        #
        # Stores:
        # (-fractionValue, numeratorIdx, denominatorIdx)
        minFractionHeap = []

        # Generate all possible fractions
        for numeratorIdx in range(arrayLength):

            for denominatorIdx in range(
                numeratorIdx + 1,
                arrayLength
            ):

                # Current fraction value
                fractionValue = (
                    -arr[numeratorIdx]
                    / arr[denominatorIdx]
                )

                # Push fraction into heap
                heapq.heappush(
                    minFractionHeap,
                    (
                        fractionValue,
                        numeratorIdx,
                        denominatorIdx
                    )
                )

                # Keep only k smallest fractions
                if len(minFractionHeap) > k:
                    heapq.heappop(minFractionHeap)

        # Top element becomes kth smallest fraction
        _, smallestNumeratorIdx, smallestDenominatorIdx = heapq.heappop(
            minFractionHeap
        )

        # Return actual fraction values
        return [
            arr[smallestNumeratorIdx],
            arr[smallestDenominatorIdx]
        ]

