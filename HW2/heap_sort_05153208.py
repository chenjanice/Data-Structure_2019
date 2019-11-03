
# coding: utf-8

# ### Heap Sort
# - 概述
#   - Heapsort(堆積排序)：是指利用堆積這種資料結構所設計的一種排序演算法。
#   - 一個近似完全二元樹的結構，並同時滿足堆積的性質：即子節點的鍵值或索引總是小於（或者大於）它的父節點。
# 
# - 做法
#   - 重複從最大堆積取出數值最大的結點(把根結點和最後一個結點交換，把交換後的最後一個結點移出堆)，並讓殘餘的堆積維持最大堆積性質。
# 
# 參考資料：[堆積排序 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
# 

# ### 我對Heap Sort 的了解
# Heap Sort分為Max Heap及min Heap，根據老師上課的教法，屬於Max Heap。
# 再次理解之後發現和上課的教法有些許的不太相同(或是我上課沒聽懂XD)
# 在第一次排序時，是先從下層往上檢查，找到最大值後，放到最下面(不動)，再由倒數第二個交換至最上層。
# 接下來就是照著上課老師說的方式檢查並交換，持續到整個Tree呈現遞增狀態。
# 
# 參考資料：[[演算法] 堆積排序法(Heap Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)

# 想自己先試試看，從0開始卻又不知從何下手，又怕看了程式碼會跳脫不出參考程式碼的框架，因此我決定先複製維基百科上參考程式碼(先不看也先不理解)，刪掉所有的程式碼只留下架構，自己先試著打打看。(以下為架構)

# In[4]:

def heap_sort(lst):
    def sift_down(start, end):
          #[1]最大堆调整
     
#[2]創建最大堆
    
#[3]堆排序
  
if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)
    print(l)


# 我的想法是，開始先從最後一個數逐一檢查Child是否存在，若沒有Child則不用比較，
# 若有Child存在，則三者(父與兩子)比較大小、並交換位置(index)。

# In[16]:

'''[1]最大堆调整'''
#尋找child是否存在
#當自己的index為 i，左邊小孩：2i+1，右邊小孩：2i+2
#從最後一個數檢查回來
def compare(i):
    if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
        if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
            return
        elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
            l[i],l[2*i+1]=l[2*i+1],l[i]

        elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
            l[i],l[2*i+2]=l[2*i+2],l[i]
        
    elif (2*i+1)in index:                           #只有左孩子存在
        if l[i]>l[2*i+1]:
            return
        else:
            l[i],l[2*i+1]=l[2*i+1],l[i]
            
    elif (2*i+2)in index:                           #只有右孩子存在
        if l[i]>l[2*i+2]:
            return
        else:
            l[i],l[2*i+2]=l[2*i+2],l[i]
    


l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
index=[]
for i in range(len(l)-1,-1,-1):  #從最後一個數檢查
    index.append(i)              
    compare(i)
print(l)
        


# 差了一點！在交換後，被往下調的那個數，需要繼續檢查以下子樹(自已&左右孩子)是否還需要交換。

# In[17]:

'''[1]最大堆调整'''
#尋找child是否存在
#當自己的index為 i，左邊小孩：2i+1，右邊小孩：2i+2
#從最後一個數檢查回來
def compare(i):
    if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
        if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
            return
        elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】   
            compare(num)

        elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2      # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)
        
    elif (2*i+1)in index:                           #只有左孩子存在
        if l[i]>l[2*i+1]:
            return
        else:
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)
            
    elif (2*i+2)in index:                           #只有右孩子存在
        if l[i]>l[2*i+2]:
            return
        else:
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)    
    


l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
index=[]
for i in range(len(l)-1,-1,-1):  #從最後一個數檢查
    index.append(i)              
    compare(i)
print(l)


# 完成第一階段的調整！(存保留心態，因為Tree的數字排法不一樣會有不同問題，遇到再來想辦法)

# 第二個步驟，最上層的數字和最後一個數字交換，由上往下比較，重複這個動作，直到完成整個排序。
# 比較有趣的地方是，網路上很多圖解都是讓最大的數字放在原Tree的最後面，而老師是將最大的數移開，由最後一個數字來替補。
# 目前的猜想是，若希望程式碼簡單一點，可能採用老師的方式會容易一些(因為不需要固定最大值在最後面，怕比較時不小心移動到而造成混亂)
# 因此，我決定另外創一個list，來裝目前為止的最大數。

# In[42]:

'''[2]創建最大堆 Build Max Heap'''
l=[9, 7, 8, 4, 6, 1, 5, 3, 2]
sorted_l=[]
index=[8, 7, 6, 5, 4, 3, 2, 1, 0]

#[1]第一個和最後一個數字交換(將2和9交換)
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print(l)

#[2]將最後一個數字放入sorted_l，並從l中移除(9放入sorted_l，從l中刪除)
sorted_l.insert(0,l[len(l)-1])
print(sorted_l)
l.pop(-1)
print(l)

#[3]也需要刪除最大值，因為compare會用到
index.pop(0)  
print(index)


# 接下來要重複的動作即為：
# 
# [從上往下檢查每一個數字-->第一個與最後一個交換-->刪掉最後一個數]
# 
# 直到所有的數字都進入sorted_l中。

# In[30]:

l=[2, 7, 8, 4, 6, 1, 5, 3]
sorted_l=[9]

def compare(i):
    if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
        if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
            return
        elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1          
            compare(num)

        elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       
            compare(num)
        
    elif (2*i+1)in index:                           #只有左孩子存在
        if l[i]>l[2*i+1]:
            return
        else:
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1       
            compare(num)
            
    elif (2*i+2)in index:                           #只有右孩子存在
        if l[i]>l[2*i+2]:
            return
        else:
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       
            compare(num)    
    

while len(l) != 0:  #只要l還有元素
    i=0    #每一次都從最上面的數開始檢查！
    compare(i)
    print("比較完的l：",l)
    
    #第一個和最後一個數字交換
    l[0],l[len(l)-1]=l[len(l)-1],l[0]
    print("交換完的l：",l)

    #將最後一個數字放入sorted_l，並從l中移除
    sorted_l.insert(0,l[len(l)-1])
    print("新增完的sorted_l：",sorted_l)
    l.pop(-1)
    print("剩下的l：",l)
    print("----------")
    


# 出現了IndexError，不曉得是為什麼讓迴圈停了下來，我決定不用迴圈看看是哪一行讓他停下來。
# (徒手煉鋼法XD)

# In[32]:

l=[2, 7, 8, 4, 6, 1, 5, 3]
sorted_l=[9]

def compare(i):
    if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
        if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
            return
        elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1          
            compare(num)

        elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       
            compare(num)
        
    elif (2*i+1)in index:                           #只有左孩子存在
        if l[i]>l[2*i+1]:
            return
        else:
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1       
            compare(num)
            
    elif (2*i+2)in index:                           #只有右孩子存在
        if l[i]>l[2*i+2]:
            return
        else:
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       
            compare(num)    
    


i=0
compare(i)
print("比較完的l：",l)
    
#第一個和最後一個數字交換
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("交換完的l：",l)

#將最後一個數字放入sorted_l，並從l中移除
sorted_l.insert(0,l[len(l)-1])
print("新增完的sorted_l：",sorted_l)
l.pop(-1)
print("剩下的l：",l)
print("----------")

i=0
compare(i)
print("比較完的l：",l)
    
#第一個和最後一個數字交換
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("交換完的l：",l)

#將最後一個數字放入sorted_l，並從l中移除
sorted_l.insert(0,l[len(l)-1])
print("新增完的sorted_l：",sorted_l)
l.pop(-1)
print("剩下的l：",l)
print("----------")

i=0
compare(i)
print("比較完的l：",l)
    
#第一個和最後一個數字交換
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("交換完的l：",l)

#將最後一個數字放入sorted_l，並從l中移除
sorted_l.insert(0,l[len(l)-1])
print("新增完的sorted_l：",sorted_l)
l.pop(-1)
print("剩下的l：",l)
print("----------")


    


# 發現Error出現在 compare中的index，忘記index這個list也要隨著l的減少，也要同步減少！

# ### -  試著把所有程式碼合併起來 -

# In[43]:


####全部


def compare(i):
    if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
        if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
            return
        elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】   
            compare(num)

        elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2      # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)
        
    elif (2*i+1)in index:                           #只有左孩子存在
        if l[i]>l[2*i+1]:
            return
        else:
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)
            
    elif (2*i+2)in index:                           #只有右孩子存在
        if l[i]>l[2*i+2]:
            return
        else:
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)    
    

### [一]第一階段：

l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
index=[]
for i in range(len(l)-1,-1,-1):  #從最後一個數檢查
    index.append(i)              
    compare(i)

    


### [二]第二階段：進行第一次交換

#[1]第一個和最後一個數字交換(將2和9交換)
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print(l)

#[2]將最後一個數字放入sorted_l，並從l中移除(9放入sorted_l，從l中刪除)
sorted_l=[]
sorted_l.insert(0,l[len(l)-1])
print(sorted_l)
l.pop(-1)
print(l)

#[3]也需要刪除最大值，因為compare會用到
index.pop(0)  
print(index)    



while len(l) != 0:
    i=0
    compare(i)
    print("比較完的l：",l)
    
    #第一個和最後一個數字交換
    l[0],l[len(l)-1]=l[len(l)-1],l[0]
    print("交換完的l：",l)

    #將最後一個數字放入sorted_l，並從l中移除
    sorted_l.insert(0,l[len(l)-1])
    print("新增完的sorted_l：",sorted_l)
    l.pop(-1)
    print("剩下的l：",l)
    
    index.pop(0)  
    print("剩下的index：",index) 
    print("----------")
    
    
    


# 竟然完成了..............(痛哭流涕)
# 第一次從來沒有參考程式碼就用自己的邏輯寫出來(嗚嗚嗚)..
# 
# 雖然我用的方法不見的是最有效率的，但是有老師上課給的index概念真的相對好下手很多！
# 
# (PS.寫到後來才發現和原本要用的維基百科的架構也搭不上邊...XD)

# 但是帶入助教給的測試值，發現沒考慮到兩數相等： (左孩子=右孩子)>父 的情況，
# 所以在compare增加了一個比較。

# In[62]:


####全部


def compare(i):
    if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
        if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
            return
        elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】   
            compare(num)

        elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2      # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)
        
        elif l[2*i+1]==l[2*i+2] and l[2*i+1]>l[i]:    #(左孩子=右孩子)>父
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】   
            compare(num)
        
    elif (2*i+1)in index:                           #只有左孩子存在
        if l[i]>l[2*i+1]:
            return
        else:
            l[i],l[2*i+1]=l[2*i+1],l[i]
            num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)
            
    elif (2*i+2)in index:                           #只有右孩子存在
        if l[i]>l[2*i+2]:
            return
        else:
            l[i],l[2*i+2]=l[2*i+2],l[i]
            num=2*i+2       # 【被下調的數繼續檢查：孩子存在與否並比較】
            compare(num)    
    

### [一]第一階段：

l = [3,2,-4,6,4,2,19]
index=[]
for i in range(len(l)-1,-1,-1):  #從最後一個數檢查
    index.append(i)              
    compare(i)

    


### [二]第二階段：進行第一次交換

#[1]第一個和最後一個數字交換(將2和9交換)
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("1. 第一次比完&第一個和最後一個數字交換後:",l)

#[2]將最後一個數字放入sorted_l，並從l中移除(9放入sorted_l，從l中刪除)
sorted_l=[]
sorted_l.insert(0,l[len(l)-1])
print("2. 將最後一個數字放入sorted_l:",sorted_l)
l.pop(-1)
print("3. 從l中移除:",l)

#[3]也需要刪除最大值，因為compare會用到
index.pop(0)  
print("4. 需要刪除最大值的index:",index)
print()
print("---進行過程---")




while len(l) != 0:
    i=0
    compare(i)
    print("比較完的l：",l)
    
    #第一個和最後一個數字交換
    l[0],l[len(l)-1]=l[len(l)-1],l[0]
    print("交換完的l：",l)

    #將最後一個數字放入sorted_l，並從l中移除
    sorted_l.insert(0,l[len(l)-1])
    print("新增完的sorted_l：",sorted_l)
    l.pop(-1)
    print("剩下的l：",l)
    
    index.pop(0)  
    print("剩下的index：",index) 
    print("----------")

    
print('Answer:',sorted_l)
    

    


# ### -----修改為標準格式-----

# In[55]:


class Solution(object):  
    def heap_sort(self,nums):
        
        def compare(i):
            if (2*i+1)in index and (2*i+2)in index:         #左右孩子都存在
                if l[i]>l[2*i+1] and l[i]>l[2*i+2]:            #父>左孩子 & 父>右孩子
                    return
                elif l[2*i+1]>l[i] and l[2*i+1]>l[2*i+2]:      #左孩子>父 & 左孩子>右孩子
                    l[i],l[2*i+1]=l[2*i+1],l[i]
                    num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】   
                    compare(num)

                elif l[2*i+2]>l[i] and l[2*i+2]>l[2*i+1]:      #右孩子>父 & 右孩子>左孩子
                    l[i],l[2*i+2]=l[2*i+2],l[i]
                    num=2*i+2      # 【被下調的數繼續檢查：孩子存在與否並比較】
                    compare(num)
                    
                elif l[2*i+1]==l[2*i+2] and l[2*i+1]>l[i]:    #(左孩子=右孩子)>父
                    l[i],l[2*i+1]=l[2*i+1],l[i]
                    num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】   
                    compare(num)
                    
        
            elif (2*i+1)in index:                           #只有左孩子存在
                if l[i]>l[2*i+1]:
                    return
                else:
                    l[i],l[2*i+1]=l[2*i+1],l[i]
                    num=2*i+1      # 【被下調的數繼續檢查：孩子存在與否並比較】
                    compare(num)
            
            elif (2*i+2)in index:                           #只有右孩子存在
                if l[i]>l[2*i+2]:
                    return
                else:
                    l[i],l[2*i+2]=l[2*i+2],l[i]
                    num=2*i+2       # 【被下調的數繼續檢查：孩子存在與否並比較】
                    compare(num)

        
        ### [一]第一階段：
        l=nums
        index=[]
        for i in range(len(l)-1,-1,-1):  #從最後一個數檢查
            index.append(i)              
            compare(i)
            
            
        ### [二]第二階段：進行第一次交換

        #[1]第一個和最後一個數字交換
        l[0],l[len(l)-1]=l[len(l)-1],l[0]

        #[2]將最後一個數字放入sorted_l，並從l中移除
        sorted_l=[]
        sorted_l.insert(0,l[len(l)-1])
        l.pop(-1)
    

        #[3]也需要刪除最大值，因為compare會用到
        index.pop(0)  
        while len(l) != 0:
            i=0
            compare(i)
               
            #第一個和最後一個數字交換
            l[0],l[len(l)-1]=l[len(l)-1],l[0]
            
            #將最後一個數字放入sorted_l，並從l中移除
            sorted_l.insert(0,l[len(l)-1])
            l.pop(-1)
            index.pop(0)  
                
        return sorted_l
               
                
                
nums=[3,2,-4,6,4,2,19]
output=Solution().heap_sort(nums)
output
                

