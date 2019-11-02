
# coding: utf-8

# 首先，先對MergeSort有一個概要的了解
# 
# Merge Sort 合併排序法
# 
# [簡介]
# - 採用分治法:
#    - 分割：遞迴地把目前序列平均分割成兩半。
#    - 整合：在保持元素順序的同時將上一步得到的子序列整合到一起（合併）。
#    
# - 合併操作：
#   將兩個已經排序的序列合併成一個序列的操作(兩種方式)
#   - 遞迴法（Top-down）：
#      1.申請空間，使其大小為兩個已經排序序列之和，該空間用來存放合併後的序列
#      2.設定兩個指標，最初位置分別為兩個已經排序序列的起始位置
#      3.比較兩個指標所指向的元素，選擇相對小的元素放入到合併空間，並移動指標到下一位置
#      4.重複步驟3直到某一指標到達序列尾
#      5.將另一序列剩下的所有元素直接複製到合併序列尾
#      
#   - 疊代法（Bottom-up）:
#      1.將序列每相鄰兩個數字進行合併操作，形成(n/2)個序列，排序後每個序列包含兩/一個元素
#      2.若此時序列數不是1個則將上述序列再次合併，形成(n/4)個序列，每個序列包含四/三個元素
#      3.重複步驟2，直到所有元素排序完畢，即序列數為1
#   
# 參考：[合併排序 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)

# 由於合併操作有兩種方式，以下則採取遞迴法嘗試寫寫看。  

#  - 先設計一個切分數列的方式

# In[34]:

alist=[5,6,8,1,4,9,12,24,14,34,45,67]

A1=[]
A2=[]

#奇數個元素
if len(alist)%2 == 1:
    num=(len(alist)//2)+1
    for i in range(num):
        A1.append(alist[i])
    for i in range(num,len(alist)):
        A2.append(alist[i])
        
    print(A1)
    print(A2)

#偶數個元素
else:
    num=(len(alist)//2)
    for i in range(num):
        A1.append(alist[i])
        
    for i in range(num,len(alist)):
        A2.append(alist[i])
    print(A1)
    print(A2)


# ##參考了網路上的方法，發現自己多此一舉...

# In[39]:

alist=[5,6,8,1,4,9,12,24,14,34,45,67]
num=len(alist)//2
arrleft=alist[0:num]
arrright=alist[num:len(alist)]
print(arrleft)
print(arrright)


# ##想辦法用迴圈持續把arr切分

# In[91]:

def separate(alist):
    num=len(alist)//2
    arrleft=alist[0:num]
    arrright=alist[num:len(alist)]
    
    print(arrleft)
    print(arrright)
    
    while len(arrleft)>1:
        separate(arrleft)
    while len(arrright)>1:
        separate(arrright)
        
    
alist=[6,5,8,4,1]
separate(alist)



# ##出現無限的遞迴狀況....
# 發現自己的遞迴的概念可能不夠清楚，

# In[94]:

def separate(alist):
    if len(alist)>1:
        num=len(alist)//2
        arrleft=alist[0:num]
        arrright=alist[num:len(alist)]
    
        print(arrleft)
        print(arrright)
    
        separate(arrleft)
        separate(arrright)
        
    
alist=[6,5,8,4,1]
separate(alist)


# ##參考資料：[初學者學演算法｜排序法進階：合併排序法 - AppWorks School - Medium](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)
# 
#     
# ##參考了以上的參考資料：將while 改成 if 並且放在開頭檢查即可改善這個問題。
# 並且決定針對這份程式碼做詳細的遞迴分解，想辦法理解當中的遞迴方式。

# In[81]:


array=[6,5,8,4,1]
def mergesort(array):
    
    if len(array)>1:
        mid=len(array)//2
        arrleft=array[0:mid]
        arrright=array[mid:len(array)]
        print(arrleft)
        print(arrright)
        print('----')
        
        mergesort(arrleft) 
        mergesort(arrright)
        
        print('當array元素皆等於1時：')
        leftmark=0
        rightmark=0
        mergemark=0
        
        while leftmark<len(arrleft) and rightmark<len(arrright):
            if arrleft[leftmark]< arrright[rightmark]:
                array[mergemark]=arrleft[leftmark]
                leftmark+=1         
            elif arrleft[leftmark] > arrright[rightmark]:
                array[mergemark]=arrright[rightmark]
                rightmark+=1               
            mergemark+=1
            print(array)
            
        while leftmark<len(arrleft):
            array[mergemark]=arrleft[leftmark]
            mergemark+=1
            leftmark+=1
            print(array)
            
        while rightmark<len(arrright):   
            array[mergemark]=arrright[rightmark]
            mergemark+=1
            rightmark+=1
            print(array)
            
        print('以上完成一次sort')
        print()
        
        
        
                
    
mergesort(array)

    
#參考資料：[初學者學演算法｜排序法進階：合併排序法 - AppWorks School - Medium](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e) 


# ##透過上述印出結果，可以了解到，每一個arrleft和arrright都會被帶入mergesort中，直到皆為1個元素時才會進行排序。
# 
# 自己對於遞迴運作的理解：
# ![title](images/mersort1.jpg)
# 

# 過了三個小時後自己練習打....

# In[123]:

def mergesort(arr):
    if len(arr) >1:
        mid=len(arr)//2
        arr1=arr[0:mid]
        arr2=arr[mid:len(arr)]
        
        mergesort(arr1)
        mergesort(arr2)
        arr=sortbeforemerge(arr,arr1,arr2)
        print('排序：',arr)

    
def sortbeforemerge(arr,arr1,arr2):
    arr1_index=0
    arr2_index=0
    arr_index=0
    
    while arr1_index<len(arr1) and arr2_index<len(arr2):
        if  arr1[arr1_index]<arr2[arr2_index]:
            arr[arr_index]=arr1[arr1_index]
            arr1_index+=1
        elif arr1[arr1_index]>arr2[arr2_index]:
            arr[arr_index]=arr2[arr2_index]
            arr2_index+=1
        arr_index+=1
            
    while arr1_index<len(arr1):
        arr[arr_index]=arr1[arr1_index]
        arr1_index+=1
        arr_index+=1
    while arr2_index<len(arr2):
        arr[arr_index]=arr2[arr2_index]
        arr2_index+=1
        arr_index+=1
    return arr
        
Numbers = [41, 33, 17, 80, 61, 5, 55]
mergesort(Numbers)
print(Numbers)


# In[ ]:

改成助教的格式：


# In[120]:

class Solution:

    def mergesort(self,arr):
        if len(arr) >1:
            mid=len(arr)//2
            arr1=arr[0:mid]
            arr2=arr[mid:len(arr)]
        
            Solution().mergesort(arr1)
            Solution().mergesort(arr2)
            arr=Solution().sortbeforemerge(arr,arr1,arr2)
            
        return arr  

    
    def sortbeforemerge(self,arr,arr1,arr2):
        arr1_index=0
        arr2_index=0
        arr_index=0
    
        while arr1_index<len(arr1) and arr2_index<len(arr2):
            if  arr1[arr1_index]<arr2[arr2_index]:
                arr[arr_index]=arr1[arr1_index]
                arr1_index+=1
            elif arr1[arr1_index]>arr2[arr2_index]:
                arr[arr_index]=arr2[arr2_index]
                arr2_index+=1
            arr_index+=1
            
        while arr1_index<len(arr1):
            arr[arr_index]=arr1[arr1_index]
            arr1_index+=1
            arr_index+=1
        while arr2_index<len(arr2):
            arr[arr_index]=arr2[arr2_index]
            arr2_index+=1
            arr_index+=1
        return arr
        
Numbers = [41, 33, 17, 80, 61, 5, 55]

output=Solution().mergesort(Numbers)
output


# 自己的測試值ok

# In[121]:

class Solution:

    def mergesort(self,arr):
        if len(arr) >1:
            mid=len(arr)//2
            arr1=arr[0:mid]
            arr2=arr[mid:len(arr)]
        
            Solution().mergesort(arr1)
            Solution().mergesort(arr2)
            arr=Solution().sortbeforemerge(arr,arr1,arr2)
            
        return arr  

    
    def sortbeforemerge(self,arr,arr1,arr2):
        arr1_index=0
        arr2_index=0
        arr_index=0
    
        while arr1_index<len(arr1) and arr2_index<len(arr2):
            if  arr1[arr1_index]<arr2[arr2_index]:
                arr[arr_index]=arr1[arr1_index]
                arr1_index+=1
            elif arr1[arr1_index]>arr2[arr2_index]:
                arr[arr_index]=arr2[arr2_index]
                arr2_index+=1
            arr_index+=1
            
        while arr1_index<len(arr1):
            arr[arr_index]=arr1[arr1_index]
            arr1_index+=1
            arr_index+=1
        while arr2_index<len(arr2):
            arr[arr_index]=arr2[arr2_index]
            arr2_index+=1
            arr_index+=1
        return arr
        
Numbers = [3,2,-4,6,4,2,19]

output=Solution().mergesort(Numbers)
output


# 用助教給的測試值卻發現沒有辦法跑出來，發現忘了處理兩數相等的情況。
# 因此調整：當兩數相等時，取先取左邊陣列的值。

# In[122]:

class Solution:

    def mergesort(self,arr):
        if len(arr) >1:
            mid=len(arr)//2
            arr1=arr[0:mid]
            arr2=arr[mid:len(arr)]
        
            Solution().mergesort(arr1)
            Solution().mergesort(arr2)
            arr=Solution().sortbeforemerge(arr,arr1,arr2)
            
        return arr  

    
    def sortbeforemerge(self,arr,arr1,arr2):
        arr1_index=0
        arr2_index=0
        arr_index=0
    
        while arr1_index<len(arr1) and arr2_index<len(arr2):
            if  arr1[arr1_index]<=arr2[arr2_index]:
                arr[arr_index]=arr1[arr1_index]
                arr1_index+=1
            elif arr1[arr1_index]>arr2[arr2_index]:
                arr[arr_index]=arr2[arr2_index]
                arr2_index+=1
            arr_index+=1
            
        while arr1_index<len(arr1):
            arr[arr_index]=arr1[arr1_index]
            arr1_index+=1
            arr_index+=1
        while arr2_index<len(arr2):
            arr[arr_index]=arr2[arr2_index]
            arr2_index+=1
            arr_index+=1
        return arr
        
Numbers = [3,2,-4,6,4,2,19]

output=Solution().mergesort(Numbers)
output

