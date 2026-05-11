"""
https://leetcode.com/problems/fruit-into-baskets/editorial/?envType=problem-list-v2&envId=sliding-window

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Sliding Window + HashMap

        Idea:
        - We need the longest subarray containing at most 2 types of fruits.
        - Each basket can hold only one fruit type.
        - So the window is valid only when it has <= 2 unique fruit types.

        Approach:
        - Expand window using rightPtr.
        - Count fruit frequencies in basket.
        - If basket has more than 2 fruit types:
            shrink from left until valid again.
        - Track the maximum valid window size.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Stores fruit type -> frequency inside current window
        basket = defaultdict(int)

        noOfFruits = len(fruits)

        # Left boundary of sliding window
        leftPtr = 0

        # Maximum number of fruits collected
        maxFruits = 0

        # Expand window using right pointer
        for rightPtr in range(noOfFruits):

            # Current fruit entering the window
            fruit = fruits[rightPtr]

            # Add fruit to basket
            basket[fruit] += 1

            # If more than 2 fruit types exist,
            # shrink window from left side
            while len(basket) > 2:

                # Fruit leaving the window
                fruit = fruits[leftPtr]

                # Reduce its count
                basket[fruit] -= 1

                # If count becomes 0,
                # remove this fruit type completely
                if basket[fruit] == 0:
                    del basket[fruit]

                # Move left boundary forward
                leftPtr += 1

            # Window is valid here: at most 2 fruit types
            maxFruits = max(maxFruits, rightPtr - leftPtr + 1)

        return maxFruits