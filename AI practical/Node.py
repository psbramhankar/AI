# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:19:12 2023

@author: Shivani Gomase
"""
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPostorder(root):
    if root:
       printPostorder(root.left)
       printPostorder(root.right)
       print(root.val)
       
def printPreorder(root):
    if root:
       print(root.val)
       printPreorder(root.left)
       printPreorder(root.right)
       
def CreateTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right= Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

choice=input("Enter choice(1/2/3")

if choice=="1":
    root1=CreateTree()
    print("\nInoreder traversal of binary tree is")
    printInorder(root1)
    
elif choice=="2":
     root2=CreateTree()
     print("\nPostoreder traversal of binary tree is")
     printPostorder(root2)
     
elif choice=="3":
     root2=CreateTree()
     print("\nPretoreder traversal of binary tree is")
     printPreorder(root3)     
     
else:
   print("invalid input")     
     
       