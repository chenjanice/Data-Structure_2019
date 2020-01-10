class Node:
    def __init__(self, val, nextNode=None):
        self.val=val
        self.topNode_Min=val  #每新增一個節點，存著此節點(top)以下的最小值
        self.next=nextNode
    
class MinStack:

    def __init__(self):
        self.topNode=None   ### 起初格式：沒有任何節點

    def push(self, x: int) -> None:
        if self.topNode == None:
            self.topNode=Node(x,None)
        else:
            temp=self.topNode.topNode_Min
            
            newNode=Node(x, self.topNode) #建立一個新的節點[[.next指標為self.topNode]]!!!!!!
            self.topNode=newNode          #.topNode改為新建的節點
            
            if temp < self.topNode.val :
                self.topNode.topNode_Min=temp
        
    def pop(self) -> None:
        self.topNode=self.topNode.next
        
    def top(self) -> int:
        return self.topNode.val

    def getMin(self) -> int:
        return self.topNode.topNode_Min
        
