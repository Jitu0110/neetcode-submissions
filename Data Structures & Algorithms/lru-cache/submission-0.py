class Node: # Doubly Linked List
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        #One capacity variable, one dictionary, left and right nodes connected to each other

        self.cap = capacity
        self.cache = {} # map key to node. 1-> node, 2-> node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left # left -> <- right

    #Helper
    def remove(self, node): #Remove from anywhere
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    #Helper
    def insert(self, node): #Add only in the right end
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node


    #O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    #O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #Removing from anywhere in DLL
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]




        
