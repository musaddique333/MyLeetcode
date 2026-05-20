"""
https://leetcode.com/problems/distant-barcodes/?envType=problem-list-v2&envId=heap-priority-queue

n a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.


Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]


Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
"""

class Solution:
    def rearrangeBarcodes(
        self,
        barcodes: List[int]
    ) -> List[int]:
        """
        Greedy + Max Heap

        Problem:
        - Rearrange barcodes so that
          no two adjacent barcodes are equal.

        Idea:
        - Always place the two most frequent barcodes.
        - This prevents the same barcode from
          becoming adjacent.

        Heap:
        - Python heap is min heap.
        - Use negative frequencies to simulate max heap.

        Greedy Strategy:
        1. Pick two most frequent barcodes.
        2. Place them alternately.
        3. Reduce their frequencies.
        4. Reinsert if still remaining.

        Time Complexity: O(n log k)
        Space Complexity: O(k)

        where:
            n = number of barcodes
            k = unique barcode types
        """

        # Count frequency of each barcode
        barcodeFrequency = Counter(barcodes)

        # Max heap storing:
        # (-frequency, barcode)
        maxFrequencyHeap = [
            (-frequency, barcode)
            for barcode, frequency in barcodeFrequency.items()
        ]

        # Convert list into heap
        heapq.heapify(maxFrequencyHeap)

        # Stores final rearranged answer
        rearrangedBarcodes = []

        # Process two most frequent barcodes together
        while len(maxFrequencyHeap) >= 2:

            # Most frequent barcode
            firstFrequency, firstBarcode = heapq.heappop(
                maxFrequencyHeap
            )

            # Second most frequent barcode
            secondFrequency, secondBarcode = heapq.heappop(
                maxFrequencyHeap
            )

            # Add both barcodes alternately
            rearrangedBarcodes.append(firstBarcode)
            rearrangedBarcodes.append(secondBarcode)

            # One occurrence used,
            # so move negative frequency toward 0
            if firstFrequency + 1 < 0:

                heapq.heappush(
                    maxFrequencyHeap,
                    (
                        firstFrequency + 1,
                        firstBarcode
                    )
                )

            # Reinsert second barcode if still remaining
            if secondFrequency + 1 < 0:

                heapq.heappush(
                    maxFrequencyHeap,
                    (
                        secondFrequency + 1,
                        secondBarcode
                    )
                )

        # One barcode type may remain
        if maxFrequencyHeap:

            rearrangedBarcodes.append(
                heapq.heappop(maxFrequencyHeap)[1]
            )

        return rearrangedBarcodes