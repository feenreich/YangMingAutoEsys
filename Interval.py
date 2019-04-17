class Node: 
    def __init__(self,val,idx): 
        self.left = None
        self.right = None
        self.val = val 
        self.idx = idx

def insert(root,node): 
    if root is None:
        root = node 
    else:
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(f'{root.val} {root.idx}') 
        inorder(root.right)
        
def preorder(root): 
    if root: 
        print(f'{root.val} {root.idx}')
        preorder(root.left) 
        preorder(root.right)
        
def postorder(root):
    if root: 
        postorder(root.left) 
        postorder(root.right)    
        print(f'{root.val} {root.idx}')
        
def getidx(l,r,L):
    
    pass

nums = [20,30,40,50,60,70,80]
idx = []
getidx(1,len(nums))

r = build(l)

postorder(r)
