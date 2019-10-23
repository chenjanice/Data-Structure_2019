class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None   #屬性：首項物件、大小
        self.size=0
       
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        #步驟：
        # <1> 需檢查 linkedlist是否為空
        # <2> 需檢查index值
        # <3> 回傳cur.val
        
        if self.head == None:  #通常使用self.head == None：表示此linkedlist無任何物件
            return -1
        if index < 0 or index >=self.size:  #index >= self.size： 因為index = size-1
            return -1
        
        cur=self.head
        for _ in range(index):
            cur=cur.next
        return cur.val
            
       

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        #需要調整的項目：
        # <1> 建一個 node
        # <2> node.next：node的.next屬性
        # <3> self.head：需定義為新node
        # <4> self.size +1
        
        node=Node(val)
        node.next=self.head
        self.head=node
        self.size+=1
            

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        
        #需要調整的項目：
        # <1> 建一個 node
        # <2> cur.next：linked list最後一項的.next屬性
        # <3> self.head：若linked list 為空：self.head需定義
        # <4> self.size +1
        
        if self.size == 0:    #或 self.head == None
            self.head = Node(val)
        
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=Node(val) #創建一個node，node=Node(val)
                               #更改原本最後一個物件的.next屬性：cur.next=node
                               #可合併
        
        self.size += 1
    
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        #需要調整的項目：
        # <1> 建一個 node
        # <2> cur.next：[index-1]物件的.next屬性
        # <3> node.next：新物件的.next屬性
        # <4> 需檢查index值   
        # <5> self.size +1  
        
        if index ==self.size:         ###能夠加快運算速度！
            self.addAtTail(val)
            return
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
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        
        #需要調整的項目：
        # <1> 刪除項目前一個的.next屬性
        # <2> cur.next：[index-1]物件的.next屬性
        # <3> node.next：新物件的.next屬性
        # <4> 需檢查index值
        
        
        if self.head == None:
            return -1
        elif index < 0  or index >= self.size:
            return -1
        
        else:
            cur=self.head
            for _ in range(index-1):
                cur=cur.next
            cur.next=cur.next.next
            self.size-=1
            
            
            
 #Q：為什麼有時候要 return -1  ，有時候不用?
