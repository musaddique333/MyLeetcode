"""
https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=two-pointers

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Expand Around Center

        Idea:
        - Every palindrome expands from its center.
        - A palindrome can have:
            1. Odd length center:  one middle character
            2. Even length center: two middle characters

        For every index:
        - Check odd palindrome centered at index.
        - Check even palindrome centered between index and index + 1.
        - Keep track of the longest palindrome found.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        # Start index of longest palindrome found
        startIndex = 0

        # End index of longest palindrome found
        endIndex = 0

        # Length of longest palindrome found
        maxLen = 0

        # Try every index as a palindrome center
        for index in range(len(s)):

            # Odd length palindrome
            # Example: "aba", center is "b"
            oddLen = self._expandFromCenters(s, index, index)

            # If odd palindrome is longer, update answer boundaries
            if oddLen > maxLen:
                maxLen = oddLen

                # Calculate start index from center and length
                startIndex = index - (oddLen - 1) // 2

                # Calculate end index from center and length
                endIndex = index + oddLen // 2

            # Even length palindrome
            # Example: "abba", center is between two "b"s
            evenLen = self._expandFromCenters(s, index, index + 1)

            # If even palindrome is longer, update answer boundaries
            if evenLen > maxLen:
                maxLen = evenLen

                # Calculate start index for even length palindrome
                startIndex = index - (evenLen // 2) + 1

                # Calculate end index for even length palindrome
                endIndex = index + evenLen // 2

        # Return longest palindrome substring
        return s[startIndex:endIndex + 1]

    def _expandFromCenters(self, s: str, leftPtr: int, rightPtr: int) -> int:
        # Expand while both sides are inside string
        # and characters are equal
        while (
            leftPtr >= 0
            and rightPtr < len(s)
            and s[leftPtr] == s[rightPtr]
        ):
            # Move left pointer outward
            leftPtr -= 1

            # Move right pointer outward
            rightPtr += 1

        # After loop breaks, pointers are one step outside
        # the valid palindrome boundary.
        #
        # Palindrome length =
        # rightPtr - leftPtr - 1
        return rightPtr - leftPtr - 1