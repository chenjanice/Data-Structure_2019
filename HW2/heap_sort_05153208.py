
# coding: utf-8

# In[ ]:


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

        
        ### [一]第一階段：最大堆調整(由下而上)
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
        
        ### [三]第三階段：重複由上至下檢查、交換的步驟直到完成
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
                

