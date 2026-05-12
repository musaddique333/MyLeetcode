"""
https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=two-pointers

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two Pointers

        Idea:
        - Water area is determined by:
              width * minimum height

        Formula:
              area = (rightPtr - leftPtr) *
                     min(height[leftPtr], height[rightPtr])

        Greedy Observation:
        - Area is limited by the shorter line.
        - Moving the taller line inward can never help,
          because width decreases and minimum height
          still remains limited by the shorter line.
        - So always move the shorter line.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(height)

        # Stores maximum water area found
        maxArea = 0

        # Left boundary
        leftPtr = 0

        # Right boundary
        rightPtr = n - 1

        # Continue until pointers meet
        while leftPtr < rightPtr:

            # Height of water is limited by shorter wall
            minHeight = min(
                height[leftPtr],
                height[rightPtr]
            )

            # Width between two walls
            width = rightPtr - leftPtr

            # Current container area
            currArea = width * minHeight

            # Update maximum area
            maxArea = max(maxArea, currArea)

            # Move the shorter wall inward
            #
            # Reason:
            # Only increasing the smaller height
            # can potentially produce larger area.
            if height[leftPtr] < height[rightPtr]:
                leftPtr += 1

            else:
                rightPtr -= 1

        return maxArea