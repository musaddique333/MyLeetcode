"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=problem-list-v2&envId=breadth-first-search

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(
        self,
        root: Optional[TreeNode]
    ) -> List[List[int]]:
        """
        Breadth First Search (BFS)

        Idea:
        - Traverse tree level by level using a queue.
        - For each level:
              collect node values normally.
        - Alternate traversal direction:
              left -> right
              right -> left

        Zigzag pattern:
        Level 0 -> left to right
        Level 1 -> right to left
        Level 2 -> left to right
        ...

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Empty tree
        if not root:
            return []

        # Queue for BFS traversal
        nodeQueue = deque()

        # Start traversal from root
        nodeQueue.append(root)

        # Stores final zigzag traversal
        zigzagTraversal = []

        # Continue until queue becomes empty
        while nodeQueue:

            # Stores values of current level
            currLayer = []

            # Number of nodes in current level
            currLevelSize = len(nodeQueue)

            # Process all nodes of current level
            for _ in range(currLevelSize):

                # Remove node from front of queue
                currNode = nodeQueue.popleft()

                # Store node value
                currLayer.append(currNode.val)

                # Add left child for next level
                if currNode.left:
                    nodeQueue.append(currNode.left)

                # Add right child for next level
                if currNode.right:
                    nodeQueue.append(currNode.right)

            # Reverse every alternate level
            #
            # Even index levels:
            # left -> right
            #
            # Odd index levels:
            # right -> left
            if len(zigzagTraversal) % 2 != 0:
                currLayer.reverse()

            # Store processed level
            zigzagTraversal.append(currLayer)

        return zigzagTraversal