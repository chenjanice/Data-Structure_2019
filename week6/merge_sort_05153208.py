
# coding: utf-8

# In[ ]:

class Solution:
        def separate(self,arr):
            if len(arr)>1:
                mid=len(arr)//2
                left=arr[0:mid]
                right=arr[mid:len(arr)]
                Solution().separate(left)
                Solution().separate(right)
                arr = Solution().sort_and_merge(arr,left,right)
            return arr

        def sort_and_merge(self,arr,left,right):
            L=0  #left指標
            R=0  #right指標
            i=0  #arr指標
    
            #左右皆仍有數字
            while L<len(left) and R<len(right):
                if left[L]<right[R]:
                    arr[i]=left[L]
                    L+=1
                elif left[L]>right[R]:
                    arr[i]=right[R]
                    R+=1
                elif left[L] == right[R]:
                    arr[i]=left[L]
                    L+=1
                i+=1
            
            #只剩左邊有數字    
            while L<len(left):
                arr[i]=left[L]
                L+=1
                i+=1
        
            #只剩右邊有數字
            while R<len(right):
                arr[i]=right[R]
                R+=1
                i+=1
        
            return arr
        
        def mergesort(self,arr):
            Solution().separate(arr)
            return arr
        


Numbers = [3,2,-4,6,4,2,19]
output=Solution().mergesort(Numbers)
output

