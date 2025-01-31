
# we are now learning hashing in python

class dictionary:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):
        index = hash(key) % self.size
        while self.slots[index] is not None:
            if self.slots[index] == key:
                self.values[index] = data
                return
            index = (index + 1) % self.size
        self.slots[index] = key
        self.values[index] = data

    def get(self, key):
        index = hash(key) % self.size
        while self.slots[index] is not None:
            if self.slots[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
        index = hash(key) % self.size
        while self.slots[index] is not None:
            if self.slots[index] == key:
                self.slots[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

    def display(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(self.slots[i], ":", self.values[i])



d = dictionary()
d.put("apple", 10)
d.put("orange", 20)
d.put("carrot", 30)
d.put("banana", 40)
d.display()
print("value of key orange:", d.get("orange"))
d.remove("orange")
d.display()
print("value of key orange:", d.get("orange"))
d.put("guava", 50)
d.display()