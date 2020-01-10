class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def insertionSortList(self, head):
        if head == None:
            return head
        else:
            dummy=ListNode(0) #建一個頭節點
            dummy.next=head   #頭節點 直接接input的linkedlist
            
            cur=head
            while cur.next:
                if cur.val < cur.next.val:
                    cur=cur.next
                else:
                    
                    pre=dummy
                    while pre.next.val < cur.next.val :
                        pre = pre.next
                    
                    temp = cur.next
                    
                    cur.next=temp.next
                    pre.next=temp
                    temp.next=pre.next
                    
            return dummy.next
