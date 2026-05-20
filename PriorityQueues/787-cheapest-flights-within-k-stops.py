"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=problem-list-v2&envId=heap-priority-queue

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 
Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.


Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
"""

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        """
        Modified Dijkstra + Stops Tracking

        Problem:
        - Find cheapest price from src to dst.
        - You can use at most k stops.
        - k stops means at most k + 1 flights/edges.

        Idea:
        - Use min heap to always explore cheapest current route first.
        - Heap stores:
              (currentCost, currentCity, flightsTaken)

        Why track flightsTaken:
        - Same city can be reached with different number of flights.
        - A slightly more expensive route with fewer flights
          may still be useful later.

        Time Complexity: O(E log E)
        Space Complexity: O(E)
        """

        # Build adjacency list:
        # originCity -> [(destinationCity, ticketCost)]
        adjacencyList = defaultdict(list)

        for originCity, destinationCity, ticketCost in flights:
            adjacencyList[originCity].append(
                (destinationCity, ticketCost)
            )

        # Min heap storing:
        # (totalCostSoFar, currentCity, flightsTaken)
        minCostHeap = [(0, src, 0)]

        # Stores best cost for each:
        # (city, flightsTaken)
        bestCostAtCityAndStops = {}

        # Process cheapest route first
        while minCostHeap:

            # Current cheapest route state
            currentCost, currentCity, flightsTaken = heapq.heappop(
                minCostHeap
            )

            # Destination reached with cheapest valid cost
            if currentCity == dst:
                return currentCost

            # If already used more than k + 1 flights,
            # we cannot continue this route
            if flightsTaken > k:
                continue

            # If we already found a cheaper way to reach
            # same city with same number of flights, skip
            if (
                (currentCity, flightsTaken) in bestCostAtCityAndStops
                and bestCostAtCityAndStops[
                    (currentCity, flightsTaken)
                ] < currentCost
            ):
                continue

            # Explore outgoing flights
            for neighborCity, flightCost in adjacencyList[currentCity]:

                # New total cost after taking this flight
                updatedCost = currentCost + flightCost

                # One more flight used
                updatedFlights = flightsTaken + 1

                # Only push if this is cheaper for
                # same city and same flight count
                if (
                    bestCostAtCityAndStops.get(
                        (neighborCity, updatedFlights),
                        float("inf")
                    )
                    > updatedCost
                ):
                    bestCostAtCityAndStops[
                        (neighborCity, updatedFlights)
                    ] = updatedCost

                    heapq.heappush(
                        minCostHeap,
                        (
                            updatedCost,
                            neighborCity,
                            updatedFlights
                        )
                    )

        return -1