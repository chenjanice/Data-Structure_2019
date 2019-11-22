
# coding: utf-8

# In[3]:

import copy

class TreeNode(object): 
    def __init__(self,x): 
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution(object):

    def insert(self, root, val):
        cur = root
        while (cur != None):
            p = cur
            if val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right
        
        cur=TreeNode(val)
        cur.parent = p
        
        if val <= p.val :
            p.left=cur
        else:
            p.right=cur
        
        return cur
    
    def insert1(self,root,val): 
        if root is None: 
            root = TreeNode(val)
        else: 
            if val > root.val: 
                if root.right is None: 
                    node = TreeNode(val)
                    root.right = node
                    node.parent = root
                                       
                else:
                    Solution().insert1(root.right, val) 
            else: 
                if root.left is None: 
                    node = TreeNode(val)
                    root.left = node
                    node.parent = root 
                else: 
                    Solution().insert1(root.left, val)
        return root
    
    def findroot(self,node): 
        while  node.parent != None:
            node=node.parent
        return node
           
    def search(self,root,target): 
      
        if root is None or root.val == target: 
            return root 
        elif target > root.val: 
            return Solution().search(root.right,target) 
        elif target <= root.val: 
            return Solution().search(root.left,target) 


    def preorder(self, root, lis):
        lis.append(root.val)
        if root.left:
            Solution().preorder(root.left,lis)
        if root.right:
            Solution().preorder(root.right,lis)
        return lis
    
    def minValueNode(self,node): 
        cur= node 
        while(cur.left is not None): 
            cur = cur.left  
        return cur
    
    def deletenode(self,root,target): 
        if root is None: 
            return root
        if target < root.val: 
            root.left = Solution().deletenode(root.left,target) 
        elif(target > root.val): 
            root.right = Solution().deletenode(root.right,target)  
        else: 
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  

            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 
            temp = Solution().minValueNode(root.right) 
            root.val = temp.val
            root.right = Solution().deletenode(root.right,temp.val) 
        return root
    
    def delete(self,root,target):
        while Solution().search(root,target)!=None:
            root=Solution().deletenode(root,target)
        return root
    
    def modify(self, root, target, new_val):
        liss=[]
        liss=Solution().preorder(root, liss)
        c=0
        while target in liss:
            c+=1
            liss.pop(liss.index(target))
        for _ in range(c):
            root=Solution().insert1(root,new_val)
            root=Solution().deletenode(root,target)
        return root
            



root = TreeNode(5)
node1 = TreeNode(3)
node2 = TreeNode(3)
node3 = TreeNode(-5)
node4 = TreeNode(8)
node5 = TreeNode(7)
node6 = TreeNode(6)
node7 = TreeNode(10)

root.left = node1
node1.left = node2
node2.left = node3
root.right = node4
node4.left = node5
node5.left = node6
node4.right = node7


root1=copy.deepcopy(root)
root2=copy.deepcopy(root)
root3=copy.deepcopy(root)
root4=copy.deepcopy(root)

#insert
print('insert')
print(Solution().insert(root1,4)==root1.left.right)
print('-----------------------------------------------')

#delete
print('delete')
root2=Solution().delete(root2,3)
print(root2.val==5 and root2.left.val==-5 and root2.left.left==None and root2.left.right==None)
print(root2.right.right.val==10 and root2.right.left.val==7 and root2.right.left.left.val==6)
print(root2.right.right.right==None and root2.right.right.left==None and root2.right.left.right==None)
print(root2.right.left.left.left==None and root2.right.left.left.right==None and root2.right.val==8)
print('-----------------------------------------------')      

#search
print('search')
print(Solution().search(root3,10)==root3.right.right)
print('-----------------------------------------------')      

#modify
print('modify')
root4=Solution().modify(root4,7,4)
print(isBinarySearchTree(root4))
print('-----------------------------------------------') 

