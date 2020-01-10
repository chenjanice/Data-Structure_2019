class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=None

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.size=0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.head == None:
            self.head = Node(x)
            self.size += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            node = Node(x)
            cur.next = node
            self.size += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size == 0:
            return False
        else:
            val=self.head.val
            self.head = self.head.next
            self.size-=1
            return val
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.head.val
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size == 0:
            return True
        else:
            return False

        
queue=MyQueue()       
queue.push(1)
queue.push(2)  
print(queue.peek())  # returns 1
print(queue.pop())   # returns 1
print(queue.empty())
