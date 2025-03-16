

class QuickSort():
    def __init__(self,arr):
        self.arr = arr
    def quick_sort(self):
        return self.quick_sort_recursive(0,len(self.arr)-1)
    
    def quick_sort_recursive(self,start,end):
        # start and end is the INDEX SO REMEMBER
 