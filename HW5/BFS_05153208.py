#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict 
class Graph:

    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v)
        
    def count(self):
        count=0
        for k in self.graph:
            count+=1
        return count
  
    def BFS(self, s): 
        #先定義兩個 Queue
        Q1 = []
        Q2 = []
        
        #起點直接放入Q2
        Q2.append(s)
        while len(Q2) != self.count() :
            for item in self.graph[s]:
                if (item not in Q1 ) & (item not in Q2) :
                    Q1.append(item)
            s = Q1.pop(0)
            Q2.append(s)
        return Q2
                        
    def DFS(self, s):
        S=[]
        Q=[]
        
        Q.append(s)
        while len(Q) != self.count() :
            for item in self.graph[s]:
                if (item not in S) & (item not in Q) :
                    S.append(item)
            s =S.pop(-1)
            Q.append(s)           
        return Q

