
# coding: utf-8

# In[6]:

from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        hashvalue,bucket=self.hashdata(key) 
        node=ListNode(hashvalue)
        if self.data[bucket] == None:
            self.data[bucket]=node
        else:
            cur=self.data[bucket]
            while cur.next != None:
                cur=cur.next
            cur.next=node
            
    def hashdata(self,key):
        h=MD5.new()
        h.update(key.encode('utf-8'))
        hashvalue=h.hexdigest()
        x=int(hashvalue,16)
        bucket=x%(self.capacity)
        return hashvalue,bucket  #回傳 加密後的值、放入的bucket
    
    def contains(self, key):
        hashvalue,bucket=self.hashdata(key)
        if self.data[bucket] == None:
            return False
        else:
            cur=self.data[bucket]
            
            while (hashvalue != cur.val) and (cur.next != None):
                    cur=cur.next
            if hashvalue == cur.val:
                return True
            else:
                return False
            
    def remove_node(self, key):
        hashvalue,bucket=self.hashdata(key)
        
        cur= self.data[bucket]
        
        if cur.val == hashvalue:
            self.data[bucket]=cur.next
            #cur = None
        else:
            while cur.next!= None and cur.next.val != hashvalue : #存在並且不等於值
                cur=cur.next  #停的原因：cur.next為值 或 cur.next為None
            
            if cur.next!=None and cur.next.val == hashvalue: #存在且等於值
                if cur.next.next == None:
                    cur.next=None
                else:
                    cur.next=cur.next.next
                
    def remove(self, key):
        while self.contains(key):
            self.remove_node(key)

