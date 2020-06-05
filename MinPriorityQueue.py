
class LinkedMinHeap:    
    
    class Node:        
        def __init__(self, item):            
            self.item = item 
            self.parent = None
            self.left = None
            self.right = None           
            
    class Item:        
        def __init__(self, priority, value=None):            
            self.priority = priority            
            self.value = value 
 
        def __lt__(self, other):            
            return self.priority < other.priority 
 
    def __init__(self):        
        self.root = None        
        self.size = 0 
        
    def __len__(self): 
        return self.size      
     
    def is_empty(self):   
        return self.size == 0
        
    def min(self):    
        return self.root    
    
    def isLeaf(self,root):
        return root.left == None and root.right == None
      
    def heapify(self):
        self._heapify(self.root)
        
    def _heapify(self,root):
        if (root.left != None):
            if (root.left.item.priority < root.item.priority):
                root.left.item.priority, root.item.priority = root.item.priority, root.left.item.priority
        if (root.right != None):
            if (root.right.item.priority < root.item.priority):
                root.right.item.priority, root.item.priority = root.item.priority, root.right.item.priority
        if (root.right != None):
            self._heapify(root.right)
        if (root.left != None):
            self._heapify(root.left)
        
    def print(self):
        if(self.is_empty() == False):
            self._print(self.root,0)
        else:
            print("Empty")
        
    def _print(self,root,index):
        if (root.parent == None):
            print("Priority: ",root.item.priority, " Index number: ", index," Parent: ",root.parent)
        else:
            if (index%2 == 0):
                print("Priority: ",root.item.priority, " Right Child of Parent with Priority: ",root.parent.item.priority)
            else:
                print("Priority: ",root.item.priority, " Left Child of Parent with Priority: ",root.parent.item.priority)
        if (root.left != None):
            self._print(root.left, index +1)
        if (root.right != None):
            self._print(root.right, index +2)
        
    def insert(self, priority, value=None):
        if (self.is_empty()):
            item = self.Item(priority,value)
            self.root = self.Node(item)
            self.size = self.size + 1
        else: 
            self._insert(priority,value,self.root)
            self.size = self.size + 1
        self.heapify()
        
    def _insert(self,priority,value,root):
        if (root.left == None):
            item = self.Item(priority,value)
            root.left = self.Node(item)
            root.left.parent = root
        elif(root.right == None):
            item = self.Item(priority,value)
            root.right = self.Node(item)
            root.right.parent = root
        elif(root.left.left == None or root.left.right == None):
            self._insert(priority,value,root.left)
        elif(root.right.left == None or root.right.right == None): 
            self._insert(priority, value, root.right)
        else:
            self._insert(priority,value,root.left)
        
           
            
        
    def delete_min(self):        
        item = self.findLastElement()
        self.root.item = item
        
    def findLastElement(self):
        if (self.is_empty()):
            print("Min-Heap is empty")
        
        elif(self.root.right == None and self.root.left == None):
            temp = self.root.item
            self.root = None
            return temp
        
        else:
            stack = []
            
            num = self.size
            while(num > 1):
                if (num%2 == 1):
                    stack.append(1)
                else:
                    stack.append(0)
                num = int(num/2)
                 
            nextNode = self.root
            while(len(stack) > 0):
                if (stack.pop() == 1):
                    nextNode = nextNode.right
                else:
                    nextNode = nextNode.left
            
            temp = nextNode.item
            if (self.size%2 == 0):
                nextNode.parent.left = None
            else:
                nextNode.parent.right = None
            return temp
                
arr = [3,7,5,1,8,4,6,11,13,2,10]
heap = LinkedMinHeap()
for i in arr:
    heap.insert(i, i%5)
heap.print()
    