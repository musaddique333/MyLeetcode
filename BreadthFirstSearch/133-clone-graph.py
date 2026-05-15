"""
https://leetcode.com/problems/clone-graph/?envType=problem-list-v2&envId=breadth-first-search

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(
        self,
        node: Optional['Node']
    ) -> Optional['Node']:
        """
        Breadth First Search (BFS) + HashMap

        Problem:
        - Create a deep copy of an undirected graph.
        - Every node and its neighbour connections
          must be cloned.

        Idea:
        - Use BFS traversal to visit graph nodes.
        - Maintain a hashmap:
              original node value -> cloned node
        - While traversing:
              create clone nodes if not already created
              connect cloned neighbours accordingly.

        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """

        # Empty graph
        if not node:
            return None

        # Stores:
        # original node value -> cloned node
        #
        # Create clone for starting node
        visitedNodes = {
            node.val: Node(node.val, [])
        }

        # Queue used for BFS traversal
        nodeQueue = deque()

        # Start traversal from input node
        nodeQueue.append(node)

        # Traverse graph level by level
        while nodeQueue:

            # Current original graph node
            currNode = nodeQueue.popleft()

            # Corresponding cloned node
            currClone = visitedNodes[currNode.val]

            # Traverse all neighbours
            for neighbor in currNode.neighbors:

                # If neighbour clone not created yet
                if neighbor.val not in visitedNodes:

                    # Create cloned neighbour node
                    visitedNodes[neighbor.val] = Node(
                        neighbor.val,
                        []
                    )

                    # Add original neighbour for future traversal
                    nodeQueue.append(neighbor)

                # Connect cloned neighbour
                currClone.neighbors.append(
                    visitedNodes[neighbor.val]
                )

        # Return cloned starting node
        return visitedNodes[node.val]