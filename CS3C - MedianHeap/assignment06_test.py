"""
CS3C, Assignment #6 Unittest - Min Heap
Matthew Heitman

The unittest code below tests scenarios related to assignment06.py
"""

import random
import unittest
from assignment06 import *
from minheap import *

class MoreMinHeapTestCase(unittest.TestCase):

    def assertIsMinHeap(self, minheap): # param minheap is MinHeap instance

        # Make sure len(object) is len(minheap._heap) - 1
        self.assertEqual(len(minheap), len(minheap._heap) - 1)

        # traverse minheap and verify heap order
        for i in range(1, len(minheap)+1): # range(start at 1, full length of minheap)
            if (i * 2) <= len(minheap): # check if index has a child / if it's last row
                # assert that parent is less than left child
                self.assertLessEqual(minheap._heap[i], minheap._heap[i * 2])
            if (i * 2 + 1) <= len(minheap):
                # assert that parent is less than right child
                self.assertLessEqual(minheap._heap[i], minheap._heap[i * 2 + 1])

    def testLargerParent(self):
        minheap = MinHeap()
        data = [5, 9, 3, 7, 1]
        for d in data:
            minheap.insert(d)
        expected = [None, 1, 3, 5, 9, 7]
        self.assertListEqual(expected, minheap._heap)

        minheap._heap[1] = 10 # insert "10" at index 1, violates heap
        with self.assertRaises(AssertionError):
            self.assertIsMinHeap(minheap)

    def testSmallerChild(self):
        minheap = MinHeap()
        data = [5, 9, 3, 7, 1]
        for d in data:
            minheap.insert(d)
        expected = [None, 1, 3, 5, 9, 7]
        self.assertListEqual(expected, minheap._heap)

        minheap._heap[5] = 1 # insert "1" at index 5, violates heap
        with self.assertRaises(AssertionError):
            self.assertIsMinHeap(minheap)

    def testInsertRemoveRandom(self):
        import random
        minheap = MinHeap()
        random.seed(80)
        data = random.sample(range(10000), 1001)  # data is 1001 random generated numbers

        # INSERT
        for d in data:
            minheap.insert(d)
            self.assertIsMinHeap(minheap) # if minheap violation, raise error
        print(f"Successful Min Heap Insertion.  Length = {len(minheap)}")
        self.assertEqual(1001, len(minheap))

        # REMOVE
        prev_value = minheap._heap[1] # captures min value
        while len(minheap) > 0:
            removed_val = minheap.remove() # capture returned removed value
            # assure previous value is less than removed_value
            self.assertGreaterEqual(removed_val, prev_value,"minimum value hasn't been removed")
            self.assertIsMinHeap(minheap) # if minheap violation, raise error
            prev_value = removed_val # reassigns prev_value to newly removed val
        print(f"Successful Min Heap Removal. Length = {len(minheap)}")
        self.assertEqual(0, len(minheap))

    def testFloydVsWilliam(self):
        """
        RESULTS

        I ran this first with a 1000 length heap. Here's the results:

            Duration of Floyd's (average): 0.0005484998691827059
            Number of data movements: 1205
            Duration of William's (average): 0.00046066707000136375
            Number of data movements: 2243
            Duration of Floyd (worst): 0.0006866669282317162
            Number of data movements: 1492
            Duration of William's (worst): 0.0010009999386966228
            Number of data movements: 8987

        Then I ran it with a larger sample (10,000).  The below "Findings" are based on the larger sample
        but the comparison is worthy of note.

            Duration of Floyd's (average): 0.005456749815493822
            Number of data movements: 12403
            Duration of William's (average): 0.004624540917575359
            Number of data movements: 22653
            Duration of Floyd (worst): 0.0064145829528570175
            Number of data movements: 14992
            Duration of William's (worst): 0.014790249988436699
            Number of data movements: 123631

        FINDINGS
        - For the average case, Floyd's does roughly half as many data movements, but is still fractionally slower
        than William's (~.0008 seconds)
        - For the worst case, Floyd's performs >2x as fast, with nearly 8x fewer data movements.
        - Floyd's worst is still close to average duration (0.0069 vs 0.0055)
        - While the movement comparisons stay somewhat consistent between a small n (1000) and large n (10000),
        the duration timing starts to show drastically more in William's worst, with a more than 100% increase in time
        versus the ~30% increase in time for the small n.
        - Using the differentiation between the small n and large n, I calculated the following:

            1000 -> 10000 element size = 10x increase

            Floyd's - O(n) expected - O(10)
            - Average case ratio: 12403/1205 ≈ 10.29
            - Worst case ration: 14992/1492 ≈ 10.05
            This is consistent with the O(n) expectations

            William's - O(n log(n)) expected - 10*(log2(10000)/log2(1000)) ≈ 10*(13.29/9.97) ≈ 13.33
            - Average case ratio: 22653/2243 ≈ 10.1
            - Worst case ratio: 123631/8987 ≈ 13.75
            Ratio is within the parameters, with the average case performing faster, which is
            to be expected from Big-O estimations being at the maximum of worst case estimations.

        """
        import time
        import random

        # AVERAGE CASE -- random numbers
        random.seed(80)
        data = random.sample(range(100000), 1000)  # data is 10000 random generated numbers
        descending_data = sorted(data, reverse=True)

            # Floyd
        start = time.perf_counter()  # mark the time
        floyd_minheap_average = InstrumentedMinHeap(data)
        duration = time.perf_counter() - start  # mark the time again, subtract the start time
        print(f"Duration of Floyd's (average): {duration}")
        print(f"Number of data movements: {floyd_minheap_average.percolate_down_counter}")

            # William
        start = time.perf_counter()  # mark the time
        william_minheap_average = InstrumentedMinHeap()
        for _ in data:
            william_minheap_average.insert(_)
        duration = time.perf_counter() - start  # mark the time again, subtract the start time
        print(f"Duration of William's (average): {duration}")
        print(f"Number of data movements: {william_minheap_average.percolate_up_counter}")

        # WORST CASE -- descending numbers

            # Floyd
        start = time.perf_counter()  # mark the time
        floyd_minheap_worst = InstrumentedMinHeap(descending_data)
        duration = time.perf_counter() - start  # mark the time again, subtract the start time
        print(f"Duration of Floyd (worst): {duration}")
        print(f"Number of data movements: {floyd_minheap_worst.percolate_down_counter}")

            # William
        start = time.perf_counter()  # mark the time
        william_minheap_worst = InstrumentedMinHeap()
        for _ in descending_data:
            william_minheap_worst.insert(_)
        duration = time.perf_counter() - start  # mark the time again, subtract the start time
        print(f"Duration of William's (worst): {duration}")
        print(f"Number of data movements: {william_minheap_worst.percolate_up_counter}")


class MedianHeapTestCase(unittest.TestCase):

    # provided by professor
    def test3Elements1(self):
        list_of_data = [3, 2, 1]
        median_heap = MedianHeap(list_of_data)
        self.assertEqual(3, len(median_heap))
        self.assertEqual(2, median_heap.peek())
        self.assertEqual(2, median_heap.remove())
        self.assertEqual(3, median_heap.peek())
        self.assertEqual(3, median_heap.remove())
        self.assertEqual(1, median_heap.peek())
        self.assertEqual(1, median_heap.remove())

    def testRemovePeekEmptyHeap(self):
        median_heap = MedianHeap() # empty
        with self.assertRaises(IndexError):
            median_heap.remove()
        with self.assertRaises(IndexError):
            median_heap.peek()

    def testSingleElement(self):
        list_of_data = [1]
        median_heap = MedianHeap(list_of_data)
        self.assertEqual(1, len(median_heap))
        self.assertEqual(1, median_heap.peek())

    def test2InsertElements(self):
        list_of_data = [2, 1]
        median_heap = MedianHeap(list_of_data)
        self.assertEqual(2, len(median_heap))
        self.assertEqual(2, median_heap.peek())
        median_heap.insert(5)
        self.assertEqual(2, median_heap.peek())
        median_heap.insert(6)
        self.assertEqual(5, median_heap.peek())

    def testNegativeElements(self):
        list_of_data = [-1, 1, 2, 3]
        median_heap = MedianHeap(list_of_data)
        self.assertEqual(2, median_heap.peek())
        median_heap.insert(-2)
        median_heap.insert(-4)
        median_heap.insert(-6)
        self.assertEqual(-1, median_heap.peek())

    def testDuplicateElements(self):
        list_of_data = [2, 1, 3]
        median_heap = MedianHeap(list_of_data)
        self.assertEqual(2, median_heap.peek())
        median_heap.insert(3)
        self.assertEqual(3, median_heap.peek())

    def testRandomMedian(self):
        import random
        median_heap = MedianHeap()
        random.seed(80)
        data = random.sample(range(10000), 1001)  # data is 1001 random generated numbers

        # INSERT
        current_heap = [] # it's a list, but it's in the test, Professor! :)
        for d in data:
            median_heap.insert(d)
            current_heap.append(d)
            current_median = sorted(current_heap)[len(current_heap) // 2]  # [list][index of expected median]
            self.assertEqual(current_median, median_heap.peek())

        print(f"Successful Median Heap Insertion.  Length = {len(median_heap)}")
        self.assertEqual(1001, len(median_heap))
        print(f"Median: {median_heap.peek()}")