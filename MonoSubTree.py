


class Node: 
    
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None
        
class Tree:
    
    def __init__(self):
        self.root = Node(3)
        
    def createTree(self):
        self.root.left = Node(6)
        self.root.left.left = Node(7)
        self.root.left.left.left = Node(7)
        self.root.right = Node(3)
        self.root.right.right = Node(5)
        self.root.right.right.right = Node(8)
        self.root.right.left = Node(4)
        self.root.right.left.right = Node(4)
        self.root.right.left.left = Node(4)
        
    def printTree(self):
        self.printSubTree(self.root,0)
    
    def printSubTree(self,root,index):
        s = Node(3)
        s = root
        print(s.value,index)
        if (s.left != None):
            self.printSubTree(s.left,index+1)
        if (s.right != None):
            self.printSubTree(s.right,index+2)

def count_mono_data_subtrees(bin_tree):
    tree = Tree()
    tree = bin_tree
    return count_mono_data_subtrees_helper(tree.root)
    
def count_mono_data_subtrees_helper(root):  
    s = Node(3)
    s = root
    if (s.left == None and s.right == None):
        return 1,1,s.value
    elif (s.left == None and s.right != None):
        x,y,z = count_mono_data_subtrees_helper(s.right)
        if (y == 1):
            if (z == s.value):
                return x+1,y,z
            else:
                return x,0,s.value
        else:
            return x,0,s.value
    elif (s.left != None and s.right == None):
        x,y,z = count_mono_data_subtrees_helper(s.left)
        if (y == 1):
            if (z == s.value):
                return x+1,y,z
            else:
                return x,0,s.value
        else:
            return x,0,s.value
    elif (s.left != None and s.right != None):
        x,y,z = count_mono_data_subtrees_helper(s.right)
        a,b,c = count_mono_data_subtrees_helper(s.left)
        if (y == 1 and b == 1):
            if (z == s.value and c == s.value):
                return x + a + 1,1,s.value
            else:
                return x + a,0,s.value
        else:
            return x + a,0,s.value
    
    
bin_tree = Tree()
bin_tree.createTree()
count,boolean,value = count_mono_data_subtrees(bin_tree)    
print("The count is: ", count)   
    
    
    
    
    