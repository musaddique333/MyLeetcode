"""
https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=sliding-window

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Sliding Window + HashSet

        Idea:
        - Every valid DNA sequence must have exactly 10 characters.
        - Use a sliding window of size 10 across the string.
        - Store sequences already seen in a hashset.
        - If a sequence appears again:
            add it into result set.

        Why result is also a set:
        - Prevents duplicate entries in final answer.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        n = len(s)

        # If string length is less than 10,
        # no valid DNA sequence can exist
        if n < 10:
            return []

        # Stores all unique 10-letter sequences seen so far
        uniqueSequences = set()

        # Stores repeated sequences
        result = set()

        # Slide window of size 10
        for i in range(n - 9):

            # Extract current 10-letter DNA sequence
            currSeq = s[i:i + 10]

            # If sequence already exists,
            # it means we found a repetition
            if currSeq in uniqueSequences:
                result.add(currSeq)

            # Store current sequence as seen
            uniqueSequences.add(currSeq)

        # Convert set to list because problem expects List[str]
        return list(result)