"""
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=sliding-window

    Given a string s, find the length of the longest substring without duplicate characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window + HashSet

        Idea:
        - Maintain a window that always contains unique characters.
        - Use a set to quickly check whether a character already exists
          inside the current window.
        
        Window movement:
        - rightPtr expands the window by adding new characters.
        - If a duplicate character is found:
            move leftPtr forward
            remove characters from the set
            until the duplicate is removed.

        Time Complexity: O(n)
        Space Complexity: O(min(n, charset))
        """

        # Stores characters currently inside the sliding window
        seen = set()

        n = len(s)

        # Left boundary of sliding window
        leftPtr = 0

        # Stores maximum valid window size found so far
        maxSize = 0

        # Expand window using right pointer
        for rightPtr in range(n):

            # Current character entering the window
            currChar = s[rightPtr]

            # If duplicate found inside current window
            if currChar in seen:

                # Shrink window from left side
                # until duplicate character is removed
                while leftPtr < rightPtr and currChar in seen:

                    # Character leaving the window
                    currTemp = s[leftPtr]

                    # Remove it from set
                    seen.remove(currTemp)

                    # Move left boundary forward
                    leftPtr += 1

            # Add current character into valid window
            seen.add(currChar)

            # Update maximum window size
            maxSize = max(maxSize, len(seen))

        return maxSize
