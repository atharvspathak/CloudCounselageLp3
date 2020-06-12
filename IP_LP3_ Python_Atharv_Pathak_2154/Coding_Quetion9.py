'''
Problem Statement:

Write a Python program to check whether a given a binary tree is a valid binary search
tree (BST) or not.
Let a binary search tree (BST) is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

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

#BST
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

#Not BST
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

'''
Output:
Given tree is a BST                    #Output
Given tree is not a BST                #Output
'''





