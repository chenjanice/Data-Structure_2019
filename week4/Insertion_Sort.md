# Insertion Sort (插入排序法)
> * 對於未排序資料，在已排序序列中從後向前掃描，找到相應位置並插入。 
> * Insertion Sort 的方法為：將 **第i張** 紙牌加入 **「前i−1張排序過」** 的紙牌組合，得到i張排序過的紙牌組合。
>   和打撲克牌時，從牌桌上逐一拿起撲克牌，在手上排序的過程相同。   
> * 舉例：     
>   Input: {5 2 4 6 1 3}。  
>   首先拿起第一張牌, 手上有 {5}。   
>   拿起第二張牌 2, 把 2 insert 到手上的牌 {5}, 得到 {2 5}。  
>   拿起第三張牌 4, 把 4 insert 到手上的牌 {2 5}, 得到 {2 4 5}。  
>   以此類推。  


### 特性  
> * 實作簡單易理解。  
> * 資料量少時較高效，且比其他 $O(n^2) $ 的排序法高效（selection sort/bubble sort）。  
> * 自適應排序：可根據當前資料排序情形加速排序，資料越接近排序完成，效率越高。  
> * 穩定排序：相同鍵值的元素，排序後相對位置不改變。  
> * 原地排序：不需額外花費儲存空間來排序。  
> * 即時演算法：可處理逐步輸入的資料，不需等資料完全備妥。  


### 步驟
> 1.  取第一個元素，將該元素視為已排序。
> 2.  出下一元素，該元素將插入序列的部分排序區域。
> 3.  找正確位置：若部分排序元素比新元素大，則互換位置。並重複步驟 2 - 3，直到部分排序元素小於等於新元素。
> 4.  入元素：將新元素插入最後的位置。
> 5.  複步驟 2 - 4，直到排序完成。



## 參考網站
> * [Comparison Sort: Insertion Sort(插入排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-insertion-sortcha-ru-pai-xu-fa.html)
> * [插入排序 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F)
> * [插入排序 Insertion sort - Rust Algorithm Club](https://rust-algo.club/sorting/insertion_sort/)



## 題目練習
>  [**Leetcode | 147. Insertion Sort List**](https://leetcode.com/problems/insertion-sort-list/)　　前往>>  [我的練習程式碼]()

## 實作概念
> * 
