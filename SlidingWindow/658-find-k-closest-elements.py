"""
https://leetcode.com/problems/find-k-closest-elements/?envType=problem-list-v2&envId=sliding-window

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Two Pointers / Shrinking Window

        Idea:
        - The answer must be a continuous subarray of size k,
          because arr is already sorted.
        - Start with the whole array as the window.
        - Remove the element that is farther from x.
        - Keep shrinking until window size becomes k.

        Tie rule:
        - If both sides have same distance from x,
          remove the right side.
        - This keeps smaller elements, as required by the problem.

        Time Complexity: O(n - k)
        Space Complexity: O(1)
        """

        n = len(arr)

        # Start with full array window
        leftPtr = 0
        rightPtr = n - 1

        # Shrink window until exactly k elements remain
        while rightPtr - leftPtr + 1 > k:

            # Distance of leftmost element from x
            leftDiff = abs(arr[leftPtr] - x)

            # Distance of rightmost element from x
            rightDiff = abs(arr[rightPtr] - x)

            # If left side is farther, remove it
            if leftDiff > rightDiff:
                leftPtr += 1

            else:
                # If right side is farther OR equal distance,
                # remove right side.
                #
                # Equal distance rule:
                # smaller element should be preferred,
                # so we remove the bigger right element.
                rightPtr -= 1

        # Return final k-sized sorted window
        return arr[leftPtr:rightPtr + 1]