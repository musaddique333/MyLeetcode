"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=heap-priority-queue

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Min Heap

        Idea:
        - Maintain a min heap of size k.
        - Heap always stores the k largest elements seen so far.
        - Smallest element inside heap becomes:
              kth largest element overall.

        Why min heap:
        - If heap size exceeds k:
              remove smallest element.
        - This keeps only the k largest numbers.

        Example:
        nums = [3,2,1,5,6,4], k = 2

        Heap process:
            [3]
            [2,3]
            remove 1
            [3,5]
            [5,6]
            remove 4

        Final heap:
            [5,6]

        Smallest in heap = 5
        => 2nd largest element

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """

        # Min heap storing k largest elements
        minHeap = []

        # Process every number
        for number in nums:

            # Add current number into heap
            heapq.heappush(minHeap, number)

            # If heap size exceeds k,
            # remove smallest element
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # Root of heap is kth largest element
        return heapq.heappop(minHeap)