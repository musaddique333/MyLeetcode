"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=problem-list-v2&envId=sliding-window

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Sliding Window + Frequency Counter

        Idea:
        - An anagram of p must have the same length as p.
        - Maintain a fixed-size window of length len(p) over s.
        - Compare character frequencies between current window and p.

        Optimization:
        - Instead of comparing full counters every time,
          track how many required characters currently have exact frequency.

        Time Complexity: O(n)
        Space Complexity: O(26) = O(1)
        """

        n = len(s)
        m = len(p)

        # If p is longer than s, no anagram is possible
        if m > n:
            return []

        # Frequency count of characters required from p
        pCharCounter = collections.Counter(p)

        # Frequency count of current window in s
        currWindow = collections.Counter()

        # Number of unique characters required to fully match
        reqUniques = len(pCharCounter)

        # Number of unique characters currently matching exact required frequency
        currUniques = 0

        # Left boundary of sliding window
        leftPtr = 0

        # Stores starting indexes of anagrams
        result = []

        # Expand window using right pointer
        for rightPtr in range(n):

            # Character entering window
            currChar = s[rightPtr]

            # Add current character to window frequency
            currWindow[currChar] += 1

            # If current character is needed and its frequency now matches p,
            # then one required character is fully satisfied
            if (
                currChar in pCharCounter
                and currWindow[currChar] == pCharCounter[currChar]
            ):
                currUniques += 1

            # Keep window size exactly m
            if rightPtr - leftPtr + 1 > m:

                # Character leaving window
                removeChar = s[leftPtr]

                # If this character was perfectly matched before removing,
                # removing it will break that match
                if (
                    removeChar in pCharCounter
                    and currWindow[removeChar] == pCharCounter[removeChar]
                ):
                    currUniques -= 1

                # Remove character from window frequency
                currWindow[removeChar] -= 1

                # Move left boundary forward
                leftPtr += 1

            # If all required unique characters match,
            # current window is an anagram of p
            if currUniques == reqUniques:
                result.append(leftPtr)

        return result