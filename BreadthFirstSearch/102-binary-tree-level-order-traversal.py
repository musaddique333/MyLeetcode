"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=problem-list-v2&envId=breadth-first-search

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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
    def levelOrder(
        self,
        root: Optional[TreeNode]
    ) -> List[List[int]]:
        """
        Breadth First Search (BFS)

        Idea:
        - Traverse tree level by level.
        - Use a queue to process nodes in FIFO order.
        - For each level:
              process all nodes currently in queue
              and add their children for next level.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Empty tree
        if not root:
            return []

        # Queue used for BFS traversal
        nodeQueue = deque()

        # Start with root node
        nodeQueue.append(root)

        # Stores final level-order traversal
        levelOrderTraversal = []

        # Continue until queue becomes empty
        while nodeQueue:

            # Stores values of current tree level
            currLayer = []

            # Number of nodes currently in this level
            totalNodes = len(nodeQueue)

            # Process all nodes of current level
            for _ in range(totalNodes):

                # Remove node from front of queue
                currNode = nodeQueue.popleft()

                # Store current node value
                currLayer.append(currNode.val)

                # Add left child for next level
                if currNode.left:
                    nodeQueue.append(currNode.left)

                # Add right child for next level
                if currNode.right:
                    nodeQueue.append(currNode.right)

            # Store completed current level
            levelOrderTraversal.append(currLayer)

        return levelOrderTraversal