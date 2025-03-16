class heap():
    def __init__(self):
        self.arr = []
        
    def addition(self,val):
        self.arr.append(val)
        self.heapify()
        

    def printt(self):
        print(self.arr)

    def heapify(self):
        #we have to check 3 elements of that index 1. that index 2. indexs left child which is i*2+1  3.  indexs right child which is i*2+1 
        index = len(self.arr)-1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.arr[index] > self.arr[parent_index]:
                self.arr[index] , self.arr[parent_index] = self.arr[parent_index] , self.arr[index]
                index = parent_index
            else:
                break


 
        

heaptest = heap()
heaptest.addition(10)
heaptest.addition(9)
heaptest.addition(8)
heaptest.addition(6)
heaptest.addition(5)
heaptest.addition(4)
heaptest.addition(22)
heaptest.printt()



