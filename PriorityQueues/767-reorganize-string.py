"""
https://leetcode.com/problems/reorganize-string/?envType=problem-list-v2&envId=heap-priority-queue

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Greedy + Max Heap

        Problem:
        - Rearrange string so that
          no two adjacent characters are same.

        Greedy Idea:
        - Always pick the two most frequent characters.
        - Place them alternately.
        - This prevents same characters from becoming adjacent.

        Why impossible condition works:
        - If one character frequency >
              (len(s) + 1) // 2
          then even after separating characters,
          at least two same characters must remain adjacent.

        Heap:
        - Python heap is min heap.
        - Use negative frequencies to simulate max heap.

        Time Complexity: O(n log k)
        Space Complexity: O(k)

        where:
            n = length of string
            k = unique characters
        """

        # Count frequency of each character
        charCounter = Counter(s)

        # Impossible case:
        # one character appears too many times
        if max(charCounter.values()) > (len(s) + 1) // 2:
            return ""

        # Max heap storing:
        # (-frequency, character)
        maxHeap = [
            (-freq, char)
            for char, freq in charCounter.items()
        ]

        # Convert list into heap
        heapq.heapify(maxHeap)

        # Stores final rearranged characters
        rtnArr = []

        # Always process two most frequent characters
        while len(maxHeap) > 1:

            # Most frequent character
            freq1, char1 = heapq.heappop(maxHeap)

            # Second most frequent character
            freq2, char2 = heapq.heappop(maxHeap)

            # Add both characters alternately
            rtnArr.extend([char1, char2])

            # One occurrence used,
            # so increase negative frequency toward 0
            if freq1 + 1 < 0:
                heapq.heappush(
                    maxHeap,
                    (freq1 + 1, char1)
                )

            # Reinsert second character if still remaining
            if freq2 + 1 < 0:
                heapq.heappush(
                    maxHeap,
                    (freq2 + 1, char2)
                )

        # One character may remain at end
        if maxHeap:
            rtnArr.append(maxHeap[0][1])

        # Convert character list into string
        return "".join(rtnArr)