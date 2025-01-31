#we are also using hash function and chaining and loadfactor 0.7 in this code
# if load factor is greater than 0.7 then we will double the size of the dictionary

class Node:


    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:


    def __init__(self,n=10):
        self.size = n
        self.list = [None]*self.size
        self.count = 0

    def put(self,key,value):
        index = hash(key)%self.size
        temp = self.list[index]
        if temp is None:
            self.list[index] = Node(key,value)
            self.count += 1
        else:
            while temp.next is not None and temp.key != key:
                temp = temp.next
            if temp is None:
                return "The key is not present in the dictionary"
            if temp.key == key:
                temp.value = value
            else:
                temp.next = Node(key,value)
            self.count += 1  
        # Check load factor and resize if necessary
        if self.count / self.size > 0.7:
            self.resize()

    def resize(self):
        new_size = self.size * 2
        new_list = [None] * new_size 
        for i in range(self.size):
            temp = self.list[i]
            while temp is not None:
                new_index = hash(temp.key) % new_size
                if new_list[new_index] is None:
                    new_list[new_index] = Node(temp.key, temp.value)
                else:
                    new_temp = new_list[new_index]
                    while new_temp.next is not None:
                        new_temp = new_temp.next
                    new_temp.next = Node(temp.key, temp.value)
                temp = temp.next
        self.size = new_size
        self.list = new_list

    def get(self,key):
        index = hash(key)%self.size
        temp = self.list[index]
        while temp is not None:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return "The key is not present in the dictionary"

    def remove(self,key):
        index = hash(key)%self.size
        temp = self.list[index]
        if temp.key == key:
            self.list[index] = temp.next
            self.count -= 1
            return
        while temp.next is not None:
            if temp.next.key == key:
                temp.next = temp.next.next
                self.count -= 1
                return   
            temp = temp.next
        return "The key is not present in the dictionary"
    def __len__(self):
        return self.count
 
    def display(self):
        keys = []
        for i in self.list:
            temp = i
            while temp is not None:
                keys.append(temp.key)
                temp = temp.next
        keys.sort()
        for key in keys:
            index = hash(key) % self.size
            temp = self.list[index]
            while temp is not None:
                if temp.key == key:
                    print(temp.key, ":", temp.value)
                    break  # Exit the loop once the key is found
                temp = temp.next

# Example usage
d = HashTable()
d.put("apple", 10)
d.put("zebra",999)
d.put("banana", 20)
d.put("cherry", 30)
d.put("donkey",22)
d.display()
print("the size of hashtable is",len(d))