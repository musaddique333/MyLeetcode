"""
https://leetcode.com/problems/top-k-frequent-words/description/?envType=problem-list-v2&envId=heap-priority-queue

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""

class Solution:
    def topKFrequent(
        self,
        words: List[str],
        k: int
    ) -> List[str]:
        """
        Frequency Map + Max Heap

        Problem:
        - Return k most frequent words.
        - If frequencies are same:
              smaller lexicographical word comes first.

        Idea:
        1. Count frequency of every word.
        2. Push into heap as:
               (-frequency, word)

        Why negative frequency:
        - Python heap is a min heap.
        - Using negative frequency simulates max heap.

        Lexicographical ordering:
        - If frequencies are equal,
          heap automatically compares words.
        - Smaller word comes first alphabetically.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        # Count frequency of each word
        freqCounter = Counter(words)

        # Max heap simulated using negative frequency
        maxHeap = []

        # Add all words into heap
        for word, freq in freqCounter.items():

            heapq.heappush(
                maxHeap,
                (-freq, word)
            )

        # Stores final top k frequent words
        result = []

        # Extract top k words
        while maxHeap and len(result) < k:

            # heap element format:
            # (-frequency, word)
            result.append(
                heapq.heappop(maxHeap)[-1]
            )

        return result