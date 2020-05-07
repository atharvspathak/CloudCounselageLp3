'''
Program:Check whether given tree is binary tree or not

Output: (1)Given tree is a BST (if True)
		(2)(1)Given tree is a BST (if False)
'''

class Node: 

	def __init__(self, data): 
		self.data = data
		self.left = None
		self.right = None

def isBst(root,left=None,right=None)->bool: 
	if (root==None) : 
		return True
	if (left!=None and left.data>=root.data) : 
		return False
	if (right!=None and right.data<=root.data) : 
		return False

	return isBst(root.left,left,root) and isBst(root.right,root,right) 


root=None
root = Node(5) 
root.left = Node(2) 
root.right = Node(8) 
root.right.left = Node(6) 
root.right.right = Node(9) 

if (isBst(root)): 
	print("Given tree is a BST") 
else: 
	print("Given tree is not a BST") 

root=None
root = Node(5) 
root.left = Node(6) 
root.right = Node(2) 
root.right.left = Node(5) 
root.right.right = Node(4) 

if (isBst(root)): 
	print("Given tree is a BST") 
else: 
	print("Given tree is not a BST") 

