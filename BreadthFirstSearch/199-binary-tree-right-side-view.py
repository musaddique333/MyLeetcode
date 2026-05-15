"""
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=problem-list-v2&envId=breadth-first-search

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

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
    def rightSideView(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:
        """
        Breadth First Search (BFS)

        Problem:
        - Return the nodes visible when looking
          at the tree from the right side.

        Idea:
        - Traverse tree level by level.
        - Process right child before left child.
        - First node seen at each level
          becomes the rightmost visible node.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Empty tree
        if not root:
            return []

        # Queue used for BFS traversal
        nodeQueue = deque([root])

        # Stores right-side visible nodes
        rightSideView = []

        # Process tree level by level
        while nodeQueue:

            # Number of nodes in current level
            levelWidth = len(nodeQueue)

            # Stores first node encountered in level
            # (which will be the rightmost node
            # because right child is processed first)
            rightMostNode = None

            # Traverse all nodes in current level
            for _ in range(levelWidth):

                # Remove node from front of queue
                currNode = nodeQueue.popleft()

                # First node encountered is rightmost node
                if not rightMostNode:
                    rightMostNode = currNode

                # Add right child first
                if currNode.right:
                    nodeQueue.append(currNode.right)

                # Add left child after right child
                if currNode.left:
                    nodeQueue.append(currNode.left)

            # Store visible node for this level
            rightSideView.append(rightMostNode.val)

        return rightSideView