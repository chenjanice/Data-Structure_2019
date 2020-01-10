class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashs = [0] * len(nums)    #先建一個相同數量的list：可視為一個個index桶子
        missing = -1     
        for i in range(len(nums)): #為了用index(0~n)叫出所有nums裡面的數
            a=nums[i]-1    #將 每一個 nums裡面的數-1：使之從 1 ~ n --> a：0 ~ n-1  (達到轉變成和index起始相同的目的)    
                           #將轉變完的nums【每一個a】可以當作 index=數值的list
            
            hashs[a] += 1  #將hash當作一個桶子，當a這個數值出現、就在hash中以a為index的位置+1
        return [hashs.index(2) + 1, hashs.index(0) + 1]  #回傳hash桶子為2(出現兩次)、為0(消失的) 【切記：因為前面的調整 都要+1】
