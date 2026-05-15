"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=problem-list-v2&envId=breadth-first-search

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
"""

"""
# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: 'Node' = None,
        right: 'Node' = None,
        next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(
        self,
        root: 'Optional[Node]'
    ) -> 'Optional[Node]':
        """
        Breadth First Search (BFS)

        Problem:
        - Connect all nodes at the same level
          using the `next` pointer.
        - Last node of each level should point to None.

        Idea:
        - Traverse tree level by level using BFS.
        - Maintain previous node of current level.
        - Connect:
              prevNode.next = currNode

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Empty tree
        if not root:
            return root

        # Queue used for BFS traversal
        nodeQueue = deque()

        # Start traversal from root
        nodeQueue.append(root)

        # Process tree level by level
        while nodeQueue:

            # Number of nodes in current level
            totalNodes = len(nodeQueue)

            # Stores previous node in current level
            prevNode = None

            # Traverse all nodes of current level
            for idx in range(totalNodes):

                # Remove node from front of queue
                currNode = nodeQueue.popleft()

                # Connect previous node to current node
                if prevNode:
                    prevNode.next = currNode

                # Update previous node
                prevNode = currNode

                # Add left child for next level
                if currNode.left:
                    nodeQueue.append(currNode.left)

                # Add right child for next level
                if currNode.right:
                    nodeQueue.append(currNode.right)

            # Last node of current level
            # should point to None
            prevNode.next = None

        return root