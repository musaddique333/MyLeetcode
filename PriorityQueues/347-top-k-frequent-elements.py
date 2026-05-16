"""
https://leetcode.com/problems/top-k-frequent-elements/?envType=problem-list-v2&envId=heap-priority-queue

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Frequency Map + Min Heap

        Problem:
        - Return k most frequent elements.

        Idea:
        1. Count frequency of every number.
        2. Maintain a min heap of size k.
        3. Heap stores:
               (frequency, number)
        4. If heap size exceeds k:
               remove smallest frequency element.

        Why min heap:
        - Heap always keeps the k most frequent elements.
        - Smallest frequency among them stays at top.

        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """

        # Count frequency of each number
        counterDict = collections.Counter(nums)

        # Min heap storing:
        # (frequency, number)
        heap = []

        # Process every unique number
        for num, freq in counterDict.items():

            # Add current number with frequency
            heapq.heappush(heap, (freq, num))

            # If heap size exceeds k,
            # remove smallest frequency element
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract numbers from heap
        topKFrequentNums = [
            num
            for _, num in heap
        ]

        return topKFrequentNums