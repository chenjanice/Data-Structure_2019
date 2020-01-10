# Merge Sort 合併排序法

## [簡介]
- 採用分治法：
   - 分割：遞迴地把目前序列平均分割成兩半。
   - 整合：在保持元素順序的同時將上一步得到的子序列整合到一起（合併）。
   
   
- 合併操作：
  將兩個已經排序的序列合併成一個序列的操作(兩種方式)
  - 遞迴法（Top-down）：
     1.申請空間，使其大小為兩個已經排序序列之和，該空間用來存放合併後的序列
     2.設定兩個指標，最初位置分別為兩個已經排序序列的起始位置
     3.比較兩個指標所指向的元素，選擇相對小的元素放入到合併空間，並移動指標到下一位置
     4.重複步驟3直到某一指標到達序列尾
     5.將另一序列剩下的所有元素直接複製到合併序列尾
     
  - 疊代法（Bottom-up）:
     1.將序列每相鄰兩個數字進行合併操作，形成(n/2)個序列，排序後每個序列包含兩/一個元素
     2.若此時序列數不是1個則將上述序列再次合併，形成(n/4)個序列，每個序列包含四/三個元素
     3.重複步驟2，直到所有元素排序完畢，即序列數為1
     
## 自己對於遞迴運作的理解
![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/mersort1.jpg)

## 流程圖
![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/mergesort_flowchart2.png?raw=true)


## 系統流程圖
![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/mergesort_flowchart1.png?raw=true)


## 參考資料
* [合併排序 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)
