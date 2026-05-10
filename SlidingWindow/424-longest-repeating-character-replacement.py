class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=problem-list-v2&envId=sliding-window

        Sliding Window Solution

        Idea:
        - Maintain a sliding window.
        - Track frequency of characters inside the window.
        - Keep track of the highest repeating character frequency.

        Key Formula:
            replacements_needed =
                window_size - maxRepCharFreq

        If replacements_needed > k:
            shrink the window from the left.

        Why maxRepCharFreq is not decreased:
        - It may become stale, but never smaller than the true max frequency.
        - A stale value may temporarily allow an invalid window,
          but it never causes us to miss the correct answer.
        - This keeps the solution O(n).

        Time Complexity: O(n)
        Space Complexity: O(26) = O(1)
        """

        n = len(s)

        # Stores longest valid substring length
        maxLen = 0

        # Maximum repeating character frequency seen so far
        maxRepCharFreq = 0

        # Frequency map of current window
        charCounter = {}

        # Left boundary of sliding window
        leftPtr = 0

        # Expand window using right pointer
        for rightPtr in range(n):

            # Current character entering window
            currChar = s[rightPtr]

            # Increase frequency
            charCounter[currChar] = charCounter.get(currChar, 0) + 1

            # Update maximum repeating frequency
            maxRepCharFreq = max(
                maxRepCharFreq,
                charCounter[currChar]
            )

            # Current window size
            windowSize = rightPtr - leftPtr + 1

            # Invalid window:
            # replacements needed exceed k
            while windowSize - maxRepCharFreq > k:

                # Character leaving window
                removeChar = s[leftPtr]

                # Decrease frequency
                charCounter[removeChar] -= 1

                # Shrink window
                leftPtr += 1

                # Update window size after shrinking
                windowSize = rightPtr - leftPtr + 1

            # Update maximum valid window length
            maxLen = max(maxLen, windowSize)

        return maxLen


"""
Time Complexity: O(26 * n)

Idea:
- Try making the entire substring equal to each character A-Z.
- Use sliding window:
    if current character is not target character,
    consume one replacement.
- If replacements exceed k:
    shrink window from left side.

Still linear because alphabet size is fixed (26),
but optimal solution is cleaner and faster.
"""
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        # Stores longest valid substring length
        maxLen = 0

        # ASCII value of 'A'
        asciiA = ord('A')

        # Try every target character from A-Z
        for alpha in range(26):

            # Remaining replacements allowed
            remReplacements = k

            # Left boundary of window
            leftPtr = 0

            # Expand window
            for rightPtr in range(n):

                # Current character entering window
                currChar = s[rightPtr]

                # Convert character into index 0-25
                currAlpha = ord(currChar) - asciiA

                # If character is not target character,
                # one replacement is needed
                if currAlpha != alpha:
                    remReplacements -= 1

                # Too many replacements used,
                # shrink window from left side
                while remReplacements < 0:

                    # Character leaving window
                    removeChar = s[leftPtr]

                    # Convert to alphabet index
                    removeAlpha = ord(removeChar) - asciiA

                    # If removed character was consuming replacement,
                    # restore one replacement
                    if removeAlpha != alpha:
                        remReplacements += 1

                    # Shrink window
                    leftPtr += 1

                # Update maximum valid window size
                maxLen = max(
                    maxLen,
                    rightPtr - leftPtr + 1
                )

        return maxLen
"""