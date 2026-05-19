"""
https://leetcode.com/problems/network-delay-time/description/?envType=problem-list-v2&envId=heap-priority-queue

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""
class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:
        """
        Dijkstra's Algorithm (Shortest Path)

        Problem:
        - Find minimum time needed for all nodes
          to receive signal from node k.
        - Directed weighted graph is given.

        Idea:
        - Use Dijkstra's algorithm.
        - Always process node with smallest current travel time.
        - Once a node is visited:
              shortest path to it is finalized.

        If all nodes are visited:
        - answer is maximum shortest-path time.

        Otherwise:
        - some nodes are unreachable
        - return -1

        Time Complexity: O(E log V)
        Space Complexity: O(V + E)
        """

        # Adjacency list:
        # src -> [(travelTime, destination)]
        directedGraph = defaultdict(list)

        # Build graph
        for src, dst, tt in times:
            directedGraph[src].append((tt, dst))

        # Min heap storing:
        # (currentTotalTime, currentNode)
        heap = [(0, k)]

        # Stores finalized shortest-path nodes
        visited = set()

        # Maximum shortest-path time seen so far
        totalTime = 0

        # Process nodes in increasing travel time
        while heap:

            # Node with smallest current travel time
            ctt, src = heapq.heappop(heap)

            # Skip already processed node
            if src in visited:
                continue

            # Mark node as finalized
            visited.add(src)

            # Update total network delay time
            totalTime = max(totalTime, ctt)

            # Explore neighbours
            for tt, dst in directedGraph[src]:

                # Only process unvisited nodes
                if dst not in visited:

                    # Push new cumulative travel time
                    heapq.heappush(
                        heap,
                        (ctt + tt, dst)
                    )

        # If all nodes reached,
        # return maximum shortest-path time
        return totalTime if len(visited) == n else -1