# graph implementing using two methods 
from collections import deque
g = {
    'a':['b','c','d'],
    'b':['e','a'],
    'c':['a','d','e','f'],
    'd':['a','c','e'],
    'e':['a','b','c','d','f'],
    'f':['c','e'],
    }
queue = deque()
queue.append('a')
visited = []
while queue:
    if queue[0] not in visited:
        visited.append(queue[0])
        print("first element is ",queue[0])
        print("the children of first element is ",g[queue[0]])
        print("the remaining queue is ", queue)
        queue.extend(g[queue[0]])
    print("poped item",queue.popleft())
    
print("the visited is ",visited)

