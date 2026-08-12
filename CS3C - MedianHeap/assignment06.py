"""
CS3C, Assignment #6, MedianHeap
Matthew Heitman

The program below inherits minheap code and implements a median heap
"""

from minheap import *

class MedianHeap:
    """
    The MedianHeap class uses two heaps: a min heap and a max heap.

    - The max heap is an instance of MinHeap, but negated upon insertion, eg [1, 2, 3] would become
    [-3, -2, -1], so the top of max heap will be -3.  When removed (eg to insert into minheap for rebalancing)
    -3 will be negated and move to minheap as 3.
    - The design is such that the median will always be at the top of the _min_heap.
    - The values of the max heap are less than or equal to the values in the min heap.
    - The minheap always has either the same amount of elements as the max heap or exactly one more
    - After each insert or removal, it will call the rebalance method to ensure that is true.
    """

    def __init__(self, initial_data=None):
        self._min_heap = MinHeap()
        self._max_heap = MinHeap()
        if initial_data is not None:
            for _ in initial_data:
                self.insert(_)

    def __len__(self):
        return len(self._min_heap) + len(self._max_heap)

    def __str__(self):
        return (f"size={len(self)}, max heap={self._max_heap._heap}, "
                f"min heap = {self._min_heap._heap}")

    def insert(self, data):
        if len(self._min_heap) == 0: # if it's empty, add to min heap
            self._min_heap.insert(data)
        elif data < self._min_heap.peek(): # if it's less than the min heap root, add negated to max heap
            self._max_heap.insert(-(data))
        else: # otherwise add to min heap
            self._min_heap.insert(data)
        self.rebalance()

    def rebalance(self):
        if len(self._min_heap) > len(self._max_heap) + 1: # if min heap heavy
            min_removed = self._min_heap.remove() # remove top of min heap
            self._max_heap.insert(-(min_removed)) # insert into max heap
        elif len(self._max_heap) > len(self._min_heap): # if max heap heavy
            max_removed = self._max_heap.remove() # remove top of max heap
            self._min_heap.insert(-(max_removed)) # insert negated element into min heap

    def remove(self):
        if len(self) == 0:
            raise IndexError("Trying to remove from empty median heap")
        median_removed = self._min_heap.remove()
        self.rebalance()
        return median_removed

    def peek(self):
        if len(self) == 0:
            raise IndexError("Trying to peek in an empty median heap")

        return self._min_heap.peek() # top of the min heap is the median

# EXTRA CREDIT
class InstrumentedMinHeap(MinHeap):
    def __init__(self, initial_data=None):
        self.percolate_up_counter = 0
        self.percolate_down_counter = 0
        super().__init__(initial_data)

    def _percolate_up(self):
        data = self._heap[len(self)]

        child_index = len(self)
        parent_index = child_index // 2  # Typically implemented as bit shift
        while child_index > 1 and data < self._heap[parent_index]:
            self.percolate_up_counter += 1 # add one for each data movement
            self._heap[child_index] = self._heap[parent_index]
            child_index = parent_index
            parent_index = child_index // 2

        self._heap[child_index] = data
        self.percolate_up_counter += 1 # add final counter for this movement

    def _percolate_down(self, starting_index):
        # Remember the data at the starting place
        data = self._heap[starting_index]

        while starting_index <= len(self):
            # While we are within the heap
            min_child_index = self._get_min_child_index(starting_index)
            if min_child_index is None:
                # No child, done
                break

            if data > self._heap[min_child_index]:
                # If the parent data is bigger than the smaller child, pull it up
                self.percolate_down_counter += 1
                self._heap[starting_index] = self._heap[min_child_index]
                # Move down to the smaller child
                starting_index = min_child_index
            else:
                # Otherwise, the parent data is smaller already, done
                break

        self._heap[starting_index] = data
        self.percolate_down_counter += 1
