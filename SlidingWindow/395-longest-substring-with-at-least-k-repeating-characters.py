"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/?envType=problem-list-v2&envId=sliding-window

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Sliding Window over possible unique character counts.

        Idea:
        - Try every possible number of unique characters in the answer.
        - For each reqUniqueChars, maintain a window with at most that many
          unique characters.
        - Track:
            uniqueChars -> number of unique characters in current window
            charCountK  -> number of characters appearing at least k times

        Valid window:
        - uniqueChars == reqUniqueChars
        - charCountK == uniqueChars

        Time Complexity: O(26 * n) = O(n)
        Space Complexity: O(26) = O(1)
        """

        n = len(s)

        # Stores the longest valid substring length found so far
        maxLen = 0

        # Try all possible unique character counts from 1 to 26
        for reqUniqueChars in range(1, 27):

            # Number of unique characters in current window
            uniqueChars = 0

            # Number of characters whose frequency is at least k
            charCountK = 0

            # Left boundary of sliding window
            leftPtr = 0

            # Frequency map for current window
            freq = {}

            # Expand window using right pointer
            for rightPtr in range(n):

                # Character entering the window
                rightChar = s[rightPtr]

                # Increase frequency of current character
                freq[rightChar] = freq.get(rightChar, 0) + 1

                # If character appeared first time, unique count increases
                if freq[rightChar] == 1:
                    uniqueChars += 1

                # If character frequency just became k,
                # this character now satisfies the condition
                if freq[rightChar] == k:
                    charCountK += 1

                # If window has more unique characters than allowed,
                # shrink it from the left side
                while uniqueChars > reqUniqueChars:
                    leftChar = s[leftPtr]

                    # If this character was satisfying frequency k,
                    # removing it will make it invalid
                    if freq[leftChar] == k:
                        charCountK -= 1

                    # Remove left character from window
                    freq[leftChar] -= 1

                    # If frequency becomes 0,
                    # one unique character is completely removed
                    if freq[leftChar] == 0:
                        uniqueChars -= 1

                    # Move left boundary forward
                    leftPtr += 1

                # Valid window:
                # exactly reqUniqueChars unique chars,
                # and all of them appear at least k times
                if uniqueChars == reqUniqueChars and uniqueChars == charCountK:
                    maxLen = max(maxLen, rightPtr - leftPtr + 1)

        return maxLen