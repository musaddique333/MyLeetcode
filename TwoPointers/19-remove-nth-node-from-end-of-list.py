"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=problem-list-v2&envId=two-pointers

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:
        """
        Two Pointers + Dummy Node

        Idea:
        - Maintain a gap of n nodes between fastPtr and slowPtr.
        - Move fastPtr ahead by n + 1 steps.
        - Then move both pointers together.
        - When fastPtr reaches the end:
              slowPtr will be just before
              the node to remove.

        Why dummy node:
        - Handles edge case where head itself
          needs to be removed.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Dummy node before head
        # Helps handle head deletion easily
        dummyPtr = ListNode(0, head)

        # Both pointers start at dummy node
        slowPtr = dummyPtr
        fastPtr = dummyPtr

        # Move fastPtr ahead by n + 1 positions
        #
        # Gap between slowPtr and fastPtr becomes n nodes
        for _ in range(n + 1):
            fastPtr = fastPtr.next

        # Move both pointers together
        #
        # When fastPtr reaches end:
        # slowPtr will be just before target node
        while fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

        # Remove nth node from end
        #
        # Skip target node
        slowPtr.next = slowPtr.next.next

        # Return updated head
        return dummyPtr.next