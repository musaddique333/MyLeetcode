
"""
https://leetcode.com/problems/number-of-islands/?envType=problem-list-v2&envId=breadth-first-search

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Breadth First Search (BFS)

        Problem:
        - Count number of islands in a grid.
        - "1" means land.
        - "0" means water.
        - Connected land horizontally/vertically forms one island.

        Idea:
        - Traverse every cell.
        - When we find land "1":
              count one island
              run BFS to visit and sink all connected land
        - Sinking means changing visited "1" to "0".

        Time Complexity: O(ROWS * COLS)
        Space Complexity: O(ROWS * COLS)
        """

        # 4 possible movement directions:
        # up, left, down, right
        self.directions = (
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        )

        # Grid dimensions
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        # Store grid reference for helper method
        self.grid = grid

        # Total island count
        noOfIslands = 0

        # Visit every cell in grid
        for row in range(self.ROWS):
            for col in range(self.COLS):

                # Found new unvisited island
                if grid[row][col] == "1":

                    # Count this island
                    noOfIslands += 1

                    # Visit and sink entire connected island
                    self.breadthFirstSearch(row, col)

        return noOfIslands

    def breadthFirstSearch(self, row: int, col: int) -> None:
        # Queue for BFS traversal
        searchQueue = deque([(row, col)])

        # Mark starting land as visited immediately
        self.grid[row][col] = "0"

        # Process all connected land cells
        while searchQueue:

            # Current land cell
            row, col = searchQueue.popleft()

            # Explore all 4 neighbouring cells
            for deltaR, deltaC in self.directions:

                # Calculate neighbour position
                newRow = row + deltaR
                newCol = col + deltaC

                # Check if neighbour is inside grid
                isInsideGrid = (
                    0 <= newRow < self.ROWS
                    and 0 <= newCol < self.COLS
                )

                # If neighbour is unvisited land,
                # mark visited and add to queue
                if isInsideGrid and self.grid[newRow][newCol] == "1":
                    self.grid[newRow][newCol] = "0"
                    searchQueue.append((newRow, newCol))