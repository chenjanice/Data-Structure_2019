# Hash
## 介紹
雜湊（英語：Hashing）是電腦科學中一種對資料的處理方法，通過某種特定的函式/演算法（稱為雜湊函式/演算法）將要檢索的項與用來檢索的索引（稱為雜湊，或者雜湊值）關聯起來，生成一種便於搜尋的資料結構（稱為雜湊表）。

**【1】雜湊函數 (Hash function)**   
主要是將不定長度訊息的輸入，演算成固定長度雜湊值的輸出，且所計算出來的雜湊值必須符合兩個主要條件:
 - 由雜湊值是無法反推出原來的訊息
 - 雜湊值必須隨明文改變而改變



**【2】雜湊表 (Hash table)**    
在用雜湊函數運算出來的雜湊值，根據 鍵 (key) 來儲存在數據結構中，而存放這些記錄的數組就稱為雜湊表。


## 原理
### 【1】Hash 
把任意長度的輸入，通過Hash算法變成固定長度的輸出。這個映射的規則就是對應的Hash算法，而原始數據映射後的二進位串就是HASH值。活動開發中經常使用的MD5和SHA都是歷史悠久的Hash算法。   


EX.echo `md5("這是一個測試文案")`;     


// 輸出結果：`2124968af757ed51e71e6abeac04f98d`   
在這個例子裡，這是一個測試文案是原始值，2124968af757ed51e71e6abeac04f98d就是經過hash算法得到的Hash值。整個Hash算法的過程就是把原始任意長度的值空間，映射成固定長度的值空間的過程。



###  【2】碰撞

#### 1)鏈地址法
使用一個鍊表數組，來存儲相應數據，當hash遇到衝突的時候依次添加到鍊表的後面進行處理。
添加一個元素的時候，首先計算元素key的hash值，確定插入數組中的位置。如果當前位置下沒有重複數據，則直接添加到當前位置。當遇到衝突的時候，添加到同一個hash值的元素後面，行成一個鍊表。這個鍊表的特點是同一個鍊表上的Hash值相同。




#### 2)開放地址法
開放地址法是指大小為 M 的數組保存 N 個鍵值對，其中 M > N。我們需要依靠數組中的空位解決碰撞衝突。基於這種策略的所有方法被統稱為「開放地址」哈希表。線性探測法，就是比較常用的一種「開放地址」哈希表的一種實現方式。線性探測法的核心思想是當衝突發生時，順序查看錶中下一單元，直到找出一個空單元或查遍全表。簡單來說就是：一旦發生衝突，就去尋找下 一個空的散列表地址，只要散列表足夠大，空的散列地址總能找到。對於開放尋址衝突解決方法，除了線性探測方法之外，還有另外兩種比較經典的探測方法，二次探測（Quadratic probing）和雙重散列（Double hashing）。

#### HASH TABLE
![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/hash_table.jpg?raw=true)

## 應用
在日常運營活動中，我們活動開發經常遇到的應用場景是信息加密、數據校驗、負載均衡。下面分別對這三種應用場景進行講解。

## 流程圖
![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/hashflowchart.jpg?raw=true)
![image](https://github.com/chenjanice/Data-Structure_2019/blob/master/images/hash_flowchart.jpg?raw=true)


## 參考網站
* [[資料結構] 雜湊 (Hash) - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10208884)
* [hash 算法原理及應用漫談 - 每日頭條](https://kknews.cc/code/q96465y.html)



## 練習
>  [**HW5**](https://github.com/chenjanice/Data-Structure_2019/tree/master/HW5)　　前往>> [我的練習程式碼](https://github.com/chenjanice/Data-Structure_2019/blob/master/week11/HashTable_%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81HashTable%E3%80%81HashFunction%20%E5%8E%9F%E7%90%86_05153208.ipynb)
>  前往>> [.py](https://github.com/chenjanice/Data-Structure_2019/blob/master/week11/hash_table_05153208.py)

## 實作概念
> * 將key利用MD5 -->轉為Hash值
> * 根據capacity-->找到bucket值
> * 放入Hash值，若碰撞則用LinkedList串連資料
