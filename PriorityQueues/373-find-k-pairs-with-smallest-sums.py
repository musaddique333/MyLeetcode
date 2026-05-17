"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=problem-list-v2&envId=heap-priority-queue

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
"""

class Solution:
    def kSmallestPairs(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int
    ) -> List[List[int]]:
        """
        Min Heap

        Problem:
        - Return k pairs with smallest sums.
        - Pair format:
              (nums1[i], nums2[j])

        Idea:
        - Arrays are already sorted.
        - For every nums1[i]:
              smallest possible pair starts with nums2[0]

        Heap stores:
            [pairSum, nums1Idx, nums2Idx]

        Process:
        1. Insert first pair from each nums1 row:
               (nums1[i], nums2[0])
        2. Always pop smallest pair.
        3. Then push next pair from same row:
               (nums1[i], nums2[j + 1])

        This works similar to merging sorted lists.

        Time Complexity: O(k log k)
        Space Complexity: O(k)
        """

        # Min heap storing:
        # [pairSum, nums1Idx, nums2Idx]
        heap = []

        # Stores final k smallest pairs
        resArr = []

        nums1Len = len(nums1)
        nums2Len = len(nums2)

        # Add first pair from each row
        #
        # Pair:
        # nums1[i] + nums2[0]
        #
        # Only first min(k, nums1Len) rows are needed
        for idx in range(min(k, nums1Len)):

            heapq.heappush(
                heap,
                [
                    nums1[idx] + nums2[0],
                    idx,
                    0
                ]
            )

        # Continue until heap becomes empty
        # or we collect k pairs
        while heap and len(resArr) < k:

            # Smallest sum pair
            _, nums1Idx, nums2Idx = heapq.heappop(heap)

            # Add actual pair into result
            resArr.append([
                nums1[nums1Idx],
                nums2[nums2Idx]
            ])

            # Move to next column in same row
            #
            # Example:
            # (nums1[i], nums2[j+1])
            if nums2Idx + 1 < nums2Len:

                heapq.heappush(
                    heap,
                    [
                        nums1[nums1Idx] + nums2[nums2Idx + 1],
                        nums1Idx,
                        nums2Idx + 1
                    ]
                )

        return resArr