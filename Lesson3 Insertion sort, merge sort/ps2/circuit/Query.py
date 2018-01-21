# import sys
# class PriorityQueue:
#     """Array-based priority queue implementation."""
#
#     def __init__(self):
#         """Initially empty priority queue."""
#         self.queue = []
#         self.min_index = None
#         self.heap_size = 0
#
#     def __len__(self):
#         # Number of elements in the queue.
#         return len(self.queue)
#
#     def left(self, i):
#         return 2 * i
#
#     def right(self, i):
#         return 2 * i + 1
#
#     def parent(self, i):
#         return i // 2
#
#     def min_heapify(self, i):
#         l = self.left(i)
#         r = self.right(i)
#         if l <= self.heap_size and self.queue[l-1] < self.queue[i-1]:
#             least = l
#         else:
#             least = i
#         if r <= self.heap_size and self.queue[r-1] < self.queue[i-1]:
#             least = r
#         if least != i:
#             temp = self.queue[i-1]
#             self.queue[i-1] = self.queue[least-1]
#             self.queue[least-1] = temp
#             self.min_heapify(least)
#
#     # def build_min_heap(self):
#     #     self.heap_size = len(self.queue)
#     #     for i in range(len(self.queue) // 2, -1, -1):
#     #         self.min_heapify(i)
#
#     def heap_increase_key(self, i, key):
#         if key > self.queue[i-1]:
#             raise ValueError("new key is larger than current key")
#         self.queue[i-1] = key
#         while i > 1 and self.queue[self.parent(i)-1] > self.queue[i-1]:
#             tmp = self.queue[self.parent(i)-1]
#             self.queue[self.parent(i)-1] = self.queue[i-1]
#             self.queue[i-1] = tmp
#             i = self.parent(i)
#
#     def append(self, key):
#         """Inserts an element in the priority queue."""
#         if key is None:
#             raise ValueError('Cannot insert None in the queue')
#         self.heap_size += 1
#         self.queue.insert(self.heap_size-1, sys.maxsize)
#         self.heap_increase_key(self.heap_size, key)
#         self.min_index = None
#
#     def min(self):
#         """The smallest element in the queue."""
#         if self.heap_size == 0:
#             return None
#         return self.queue[0]
#
#     def pop(self):
#         """Removes the minimum element in the queue.
#
#         Returns:
#             The value of the removed element.
#         """
#         if self.heap_size == 0:
#             return None
#         self._find_min()
#         popped_key = self.queue.pop(self.min_index)
#         self.heap_size -= 1
#         print(self.queue, self.heap_size)
#         if self.heap_size != 0:
#             self.queue[0] = self.queue[self.heap_size-1]
#             self.min_heapify(0)
#             self.min_index = None
#         return popped_key
#
#     def _find_min(self):
#         # Computes the index of the minimum element in the queue.
#         #
#         # This method may crash if called when the queue is empty.
#         if self.min_index is not None:
#             return
#         self.min_index = 0

class PriorityQueue:
    """Heap-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        self.heap = [None]

    def __len__(self):
        # Number of elements in the queue.
        return len(self.heap) - 1

    def append(self, key):
        """Inserts an element in the priority queue."""
        if key is None:
            raise ValueError('Cannot insert None in the queue')

        i = len(self.heap)
        self.heap.append(key)
        while i > 1:
            parent = i // 2
            if key < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], key
                i = parent
            else:
                break

    def min(self):
        """Returns the smallest element in the queue."""
        return self.heap[1]

    def pop(self):
        """Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        heap = self.heap
        popped_key = heap[1]
        if len(heap) == 2:
            return heap.pop()
        heap[1] = key = heap.pop()

        i = 1
        while True:
            left = i * 2
            if len(heap) <= left:
                break
            left_key = heap[left]
            right = i * 2 + 1
            right_key = right < len(heap) and heap[right]
            if right_key and right_key < left_key:
                child_key = right_key
                child = right
            else:
                child_key = left_key
                child = left
            if key <= child_key:
                break
            self.heap[i], self.heap[child] = child_key, key
            i = child
        return popped_key

A = PriorityQueue()
A.append(1)
A.append(4)
A.append(3)
print(A.heap)
A.append(2)
print(A.heap)
A.append(0)
print(A.heap)
A.append(7)
A.append(6)
A.append(5)
# print(A.pop())
# print(A.pop())
# print(A.pop())
# print(A.pop())
# print(A.pop())
# print(A.pop())
# print(A.pop())
# print(A.pop())


