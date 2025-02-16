class Heap:
    def __init__(self):
        """Initialize the max-heap."""
        self.arr = []

    def _heapify_down(self, index):
        """Move the element up to maintain the max-heap property."""
        largest = index
        left = 2*index+1
        right = 2*index+2
        n = len(self.arr)
        if (left<= n-1 and self.arr[left]>self.arr[largest]):
            largest = left
        if (right <= n-1 and self.arr[right]>self.arr[largest]):
            largest = right

        if (index != largest):
            self.arr[index],self.arr[largest] = self.arr[largest],self.arr[index]
            self._heapify_up(largest)

    def _heapify_up(self, index):
    # If the current element is not at the root
        if index > 0:
            parent = (index - 1) // 2  # Calculate parent's index
        # If the current element is greater than its parent, swap them
            if self.arr[index] > self.arr[parent]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            # Continue to bubble up recursively
            self._heapify_up(parent)
    def push(self, value):
        """Insert an element into the heap."""
        self.arr.append(value) 
        self._heapify_up(len(self.arr)-1)

    def pop(self):
        """Remove and return the root element of the heap."""
        pass

    def peek(self):
        """Return the root element without removing it."""
        print(self.arr[0])

    def size(self):
        """Return the number of elements in the heap."""
        print("the size of emements is ", len(self.arr))

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.arr)==0 
    def print(self):
        print("the array is ",self.arr)




heap = Heap()
heap.push(22)
heap.push(12)
heap.push(88)
heap.push(2)
heap.print()