"""
https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=binary-search

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary Search on Matrix

        Problem:
        - Each row is sorted.
        - First element of each row is greater than
          last element of previous row.
        - Search target in matrix.

        Idea:
        1. Binary search to find the possible row.
        2. Binary search inside that row.

        Time Complexity: O(log ROWS + log COLS)
        Space Complexity: O(1)
        """

        # Matrix dimensions
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Search space for rows
        topPtr = 0
        bottomPtr = ROWS - 1

        # Stores candidate row index
        rowPtr = -1

        # First binary search:
        # find row where target can exist
        while topPtr <= bottomPtr:

            # Middle row
            rowPtr = (topPtr + bottomPtr) // 2

            # If target lies between first and last
            # element of this row, this is target row
            if matrix[rowPtr][0] <= target <= matrix[rowPtr][-1]:
                break

            # Target is smaller than first element
            # of current row, search upper rows
            elif target < matrix[rowPtr][0]:
                bottomPtr = rowPtr - 1

            # Target is larger than last element
            # of current row, search lower rows
            else:
                topPtr = rowPtr + 1

        # If no valid row found
        if not (0 <= rowPtr < ROWS and matrix[rowPtr][0] <= target <= matrix[rowPtr][-1]):
            return False

        # Search space for columns
        leftPtr = 0
        rightPtr = COLS - 1

        # Second binary search:
        # search target inside selected row
        while leftPtr <= rightPtr:

            # Middle column
            colPtr = (leftPtr + rightPtr) // 2

            # Target found
            if matrix[rowPtr][colPtr] == target:
                return True

            # Target is larger, search right side
            elif target > matrix[rowPtr][colPtr]:
                leftPtr = colPtr + 1

            # Target is smaller, search left side
            else:
                rightPtr = colPtr - 1

        # Target not found
        return False