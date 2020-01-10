class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head=None   
        self.size=0
        
    def get(self, index):
        if self.head == None:
            return -1
        elif index < 0 or index >=self.size: 
            return -1
        if index == 0:
            return self.head.val
        else:
            cur=self.head
            for _ in range(index):
                cur=cur.next
            return cur.val
        
    def addAtHead(self, val):
        if self.head == None:
            node=Node(val)
            self.head=node
            self.size+=1
        else:
            node=Node(val)
            cur=self.head
            node.next=cur
            self.head=node
            self.size+=1
            
    def addAtTail(self, val):
        if self.size == 0:   
            self.addAtHead(val)
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=Node(val)
        self.size += 1
    
    def addAtIndex(self, index, val):
        if index ==self.size:         
            self.addAtTail(val)
            return
        elif index==0:
            self.addAtHead(val)
        elif index < 0 or index >=self.size:
            return
        else:
            cur=self.head
            for _ in range(index-1):
                cur=cur.next
            node=Node(val)
            node.next=cur.next
            cur.next= node
            self.size+=1
        
    def deleteAtIndex(self, index):
        if self.head == None:
            return -1
        elif index < 0  or index >= self.size:
            return -1
        elif index == 0:
            cur = self.head
            self.head = cur.next
            cur = None
            self.size-=1
        elif index == (self.size-1):
            cur=self.head
            for _ in range(index-1):
                cur=cur.next
            cur.next=None
            self.size-=1
        else:
            cur=self.head
            for _ in range(index-1):
                cur=cur.next
            cur.next=cur.next.next
            self.size-=1
