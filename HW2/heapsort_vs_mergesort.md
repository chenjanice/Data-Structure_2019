## Heap Sort vs. Merge Sort
|Item|Heap Sort|Merge Sort|
|:---|:---|:---|
|原理 | - 利用堆積樹(Heap Tree)的性質來排序<br> - 最大堆積樹(Max Heap Tree)的根節點一定是最大值，一一與最後一個樹葉節點交換後，取出加入已排序數列<br>  - 將原來的樹重新調整為最大堆積樹| - 將數列對分成兩個子數列，並遞回對分<br> - 對分至只有一個元素時，將元素回傳合併  |
|作法|•	將數列轉換成**Max Heap**<br>•	排序**最大堆積樹(Max Heap) **的**樹根**一定是最大值) <br>o	[1]將`樹根(最大值)`與`最後一個節點`調換，將最後一個節點(原樹根)`取出`，並加入已排序數列<br>o	[2]對整棵樹重新調整為`最大堆積樹` ⇒ 調整後樹根為`Max Node`<br>o	重複步驟1、2|•	將數列對分成**左子數列**、**右子數列**<br>•	分別對左、右子數列作上一個步驟 ⇒ **遞迴(Recursive)** <br>o	直到左子數列、右子數列被分割成`只剩一個元素`為止<br>o	將僅剩的一個元素作為遞迴的結果回傳<br>•	對回傳的左子數列、右子數列`依大小排列合併`<br>•	將`合併的結果`作為遞迴的結果回傳|
|時間複雜度|建立MaxHeap：Ο(n) <br>執行n-1次Delete Max：(n-1) × Ο(log n) = Ο( n log n) -> Ο(n) + Ο( n log n) = Ο( n log n) |T(n) = MergeSort(左子數列) + MergeSort(右子數列) + Merge<br>= T(n/2) + T(n/2) + c×n = O(n log2n)| 
|BEST|Ο(n log n)|Ο(n log n)|
|WORST|Ο(n log n)|Ο(n log n)|
|AVERAGE|Ο(n log n)|Ο(n log n)|
|空間複雜度|Ο(1)<br>原地置換(In-Place)<br>(只需要固定的額外空間)|Ο(n) <br>需要暫時性的暫列存放每回合Merge後的結果|
|穩定性|穩定性	不穩定(Unstable)|穩定(Stable)|


[[演算法] 排序演算法(Sort Algorithm)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Sort.php)

[[演算法] 合併排序法(Merge Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Merge/Merge.php)

[[演算法] 堆積排序法(Heap Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)
