#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [
            ["-" for column in range(vertices)]  
                    for row in range(vertices)] 
        self.group=[]
        
        self.graph1 = defaultdict(list)
        self.weight = []
        self.head = defaultdict(list)
        self.answer=dict()
    
    
    def findmin(self,step):
        temp=[]
        for i in range(self.V):
            if (i in self.group) or (self.graph_matrix[step][i]=='-'):
                temp.append(1000000000000)
            else:
                temp.append(self.graph_matrix[step][i])

        return min(temp),temp.index(min(temp))

    
    def paste(self,step):
        for i in range(self.V):
            if i in self.group:
                self.graph_matrix[step][i]=self.graph_matrix[step-1][i]
        return self.graph_matrix

    
    def upgrade(self,step):
        top=self.group[0]
        point=self.group[-1]

        for i in range(self.V):
            if (i not in self.group) and (self.graph[point][i]!=0):
                num=self.graph_matrix[step-1][point]+self.graph[point][i]
                if self.graph_matrix[step-1][i]=='-':
                    self.graph_matrix[step][i]=num
                elif self.graph_matrix[step-1][i] > num:
                    self.graph_matrix[step][i]=num
                elif self.graph_matrix[step-1][i] <num:
                    self.graph_matrix[step][i]=self.graph_matrix[step-1][i]
        return self.graph_matrix

    
    def down(self,step):
        for i in range(self.V):
            if (self.graph_matrix[step][i]=='-') and (self.graph_matrix[step-1][i]!='-'):
                self.graph_matrix[step][i]=self.graph_matrix[step-1][i]
        return self.graph_matrix
    
    
    def to_dic(self):
        temp=self.graph_matrix[-1]
        d=dict()
        for i in range(len(temp)):
            d[str(i)]=temp[i]
        return d


    def Dijkstra(self, s):

        self.group.append(s)
        self.graph_matrix[0][s]=0
        for i in range(self.V):
            if self.graph[s][i] !=0:
                self.graph_matrix[0][i]=self.graph[s][i]

        cost,point=Graph.findmin(self,0)
        self.group.append(point)

        for t in range(1,self.V):
            self.graph_matrix=Graph.paste(self,t)
            self.graph_matrix=Graph.upgrade(self,t)
            cost,point=Graph.findmin(self,t)
            self.group.append(point)
            self.graph_matrix=Graph.down(self,t)
        d=Graph.to_dic(self)
        return d
    
    
    

    def addEdge(self,u,v,w): 
        lst=[u,v]
        self.graph1[w].append(lst)
        self.weight.append(w)
        self.head[u]= -1
        self.head[v]= -1
        
        
    def check(self,a,b):
        if (self.head[a] == -1) and (self.head[b] == -1):
            self.head[a]=a
            self.head[b]=a
            return True
        elif (self.head[a] == -1) and (self.head[b] != -1):
            self.head[a]=self.head[b]
            return True
        elif (self.head[a] != -1) and (self.head[b] == -1):
            self.head[b]=self.head[a]
            return True
        elif (self.head[a] != -1) and (self.head[b] != -1) and (self.head[a] == self.head[b]):
            return False
        elif (self.head[a] != -1) and (self.head[b] != -1) and (self.head[a] != self.head[b]):
            for k in self.head:
                if self.head[k]==self.head[b]:
                    self.head[k]=self.head[a]
            return True
        

    def Kruskal(self):
        e=0
        v=self.V
        
        while e != v-1:
            x=min(self.weight)
            a,b=self.graph1[x][0]
            key='%s-%s'%(a,b)
            if Graph.check(self,a,b):
                key='%s-%s'%(a,b)
                self.answer[key]=x
                e+=1
            self.weight.pop(self.weight.index(x))
            c=self.graph1[x]
            d=self.graph1[x][0]
            self.graph1[x].pop(c.index(d))            
        return self.answer

