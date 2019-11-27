## Quicksort [快速排序法]
> * Quick Sort：「把大問題分成小問題處理」的方法 - Divide and Conquer algorithm
> * 概念：在數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」。將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。
> * Partition(調整數列)： 的功能就是把數列「區分」成「小於pivot」與「大於pivot」兩半。


### 步驟

> * 其中,劃分元素的 選取 直接影響到快速排序演算法的效率,通常選擇列表的第一個元素或者中間元素或者最後一個元素作為劃分元素,當然也有更復雜的選擇方式;劃分 過程根據劃分元素重排列表,是快速排序演算法的關鍵所在,該過程的原理示意圖如下:
>
#### [1]選取劃分元素
>![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/q1.jpg)
#### [2]劃分過程
>![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/q2.jpg)
#### [3]劃分結果
>![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/q3.jpg)
>* 快速排序演算法的優點是：原位排序（只使用很小的輔助棧），平均情況下的時間複雜度為 O(n log n)。快速排序演算法的缺點是：它是不穩定的排序演算法，最壞情況下的時間複雜度為 O(n2)。


## 參考網站
> * [The Quick Sort — Problem Solving with Algorithms and Data Structures](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)   
> * [Comparison Sort: Quick Sort(快速排序法)](https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html)

## 練習
> [HW1 程式碼練習過程](https://github.com/chenjanice/Data-Structure_2019/blob/master/week5/Quicksort.ipynb)
