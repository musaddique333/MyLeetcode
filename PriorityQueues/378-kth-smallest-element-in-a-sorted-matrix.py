"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/?envType=problem-list-v2&envId=heap-priority-queue

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Max Heap of Size k

        Problem:
        - Find kth smallest element in a sorted matrix.

        Idea:
        - Maintain a max heap of size k.
        - Since Python only provides min heap,
          store negative values to simulate max heap.

        Process:
        - Traverse every element in matrix.
        - Push negative value into heap.
        - If heap size exceeds k:
              remove largest element
              (smallest negative value).

        Result:
        - Heap finally stores k smallest elements.
        - Top of heap becomes kth smallest element.

        Time Complexity: O(n^2 log k)
        Space Complexity: O(k)
        """

        # Max heap simulated using negative values
        heap = []

        # Matrix dimension
        n = len(matrix)

        # Traverse all matrix elements
        for i in range(n):
            for j in range(n):

                # Push negative value
                # to simulate max heap
                heapq.heappush(
                    heap,
                    -matrix[i][j]
                )

                # If heap size exceeds k,
                # remove current largest element
                if len(heap) > k:
                    heapq.heappop(heap)

        # Top element of max heap
        # is kth smallest value
        return -heap[0]