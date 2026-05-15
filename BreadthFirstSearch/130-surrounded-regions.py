"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Breadth First Search (BFS)

        Problem:
        - Capture surrounded regions.
        - Any "O" fully surrounded by "X" should become "X".
        - Any "O" connected to border should stay "O".

        Idea:
        - Border-connected "O" cannot be captured.
        - Start BFS from every border "O".
        - Mark all safe border-connected "O" as "S".
        - After that:
              remaining "O"  -> captured, change to "X"
              safe "S"       -> restore back to "O"

        Time Complexity: O(ROWS * COLS)
        Space Complexity: O(ROWS * COLS)
        """

        # Number of rows in board
        self.ROWS = len(board)

        # Number of columns in board
        self.COLS = len(board[0])

        # 4 possible movement directions:
        # right, left, down, up
        self.directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # Step 1:
        # Start BFS from every border "O"
        for row in range(self.ROWS):
            for col in range(self.COLS):

                # Check if current cell is on border
                isBorderCell = (
                    row == 0
                    or row == self.ROWS - 1
                    or col == 0
                    or col == self.COLS - 1
                )

                # Border "O" and all connected "O"s are safe
                if board[row][col] == "O" and isBorderCell:
                    self.breadthFirstSearch(row, col, board)

        # Step 2:
        # Capture surrounded regions and restore safe regions
        for row in range(self.ROWS):
            for col in range(self.COLS):

                # This "O" was not connected to border,
                # so it is captured
                if board[row][col] == "O":
                    board[row][col] = "X"

                # This "S" was marked safe,
                # restore it back to "O"
                elif board[row][col] == "S":
                    board[row][col] = "O"

    def breadthFirstSearch(
        self,
        row: int,
        col: int,
        board: List[List[str]]
    ) -> None:
        # Queue for BFS traversal
        nodeQueue = deque()

        # Add starting border "O"
        nodeQueue.append((row, col))

        # Mark starting cell as safe
        board[row][col] = "S"

        # Process all connected safe "O"s
        while nodeQueue:

            # Current cell
            row, col = nodeQueue.popleft()

            # Explore all 4 neighbouring cells
            for deltaR, deltaC in self.directions:

                # Calculate neighbour position
                newRow = row + deltaR
                newCol = col + deltaC

                # Check if neighbour is inside board
                isInsideBoard = (
                    0 <= newRow < self.ROWS
                    and 0 <= newCol < self.COLS
                )

                # If neighbour is valid "O",
                # mark it safe and add to queue
                if isInsideBoard and board[newRow][newCol] == "O":
                    board[newRow][newCol] = "S"
                    nodeQueue.append((newRow, newCol))