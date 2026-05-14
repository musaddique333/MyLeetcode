"""
https://leetcode.com/problems/rotate-list/?envType=problem-list-v2&envId=two-pointers

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:
        """
        Linked List Rotation

        Idea:
        - Rotating right by k means:
              last k nodes move to front.

        Steps:
        1. Find length of linked list and tail node.
        2. Reduce unnecessary rotations using:
               k %= n
        3. Find new tail:
               (n - k - 1)th node
        4. New head becomes newTail.next
        5. Break list at newTail
        6. Connect old tail to old head

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Edge cases:
        # empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Find linked list length and tail node
        tail = head
        n = 1

        while tail.next:
            tail = tail.next
            n += 1

        # Reduce extra full rotations
        #
        # Example:
        # n = 5, k = 12
        # rotating 12 times == rotating 2 times
        k %= n

        # If rotation becomes 0 after modulo,
        # list remains same
        if k == 0:
            return head

        # Find new tail
        #
        # new tail is:
        # (n - k - 1) steps from head
        #
        # Example:
        # 1 -> 2 -> 3 -> 4 -> 5
        # k = 2
        #
        # newTail = 3
        # newHead = 4
        newTail = head

        for _ in range(n - k - 1):
            newTail = newTail.next

        # Node after newTail becomes new head
        newHead = newTail.next

        # Break linked list at newTail
        newTail.next = None

        # Connect old tail to old head
        tail.next = head

        return newHead