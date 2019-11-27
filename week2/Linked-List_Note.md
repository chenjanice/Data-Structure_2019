### 目錄：
   * [簡介：Linked List(連結串列)](https://github.com/chenjanice/Data-Structure_2019/new/master/week2#%E7%B0%A1%E4%BB%8Blinked-list%E9%80%A3%E7%B5%90%E4%B8%B2%E5%88%97)
   * [比較：Array 與Linked List](https://github.com/chenjanice/Data-Structure_2019/new/master/week2#%E6%AF%94%E8%BC%83array-%E8%88%87linked-list)
     * [Array](https://github.com/chenjanice/Data-Structure_2019/new/master/week2#array)
     * [Linked list](https://github.com/chenjanice/Data-Structure_2019/new/master/week2#linked-list)
   * [實作概念](https://github.com/chenjanice/Data-Structure_2019/new/master/week2#%E5%AF%A6%E4%BD%9C%E6%A6%82%E5%BF%B5)
   * [題目練習](https://github.com/chenjanice/Data-Structure_2019/new/master/week2#%E9%A1%8C%E7%9B%AE%E7%B7%B4%E7%BF%92)
   * [參考資料]()




## 簡介：Linked List(連結串列)
> 1.	一種常見資料結構、資料儲存方式
> 2.	使用node(節點)來記錄、表示、儲存資料
> 3.	利用pointer將每個node串連起來
> 4.	每個node內部至少包含：data(代表資料)與pointer(指向下一個node)
![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/linkedlist1.png)
![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/linkedlist2.png)

 

## 比較：Array 與Linked List
![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/linkedlist3.png)
### Array
> `優點`：
> 1.	random access：只要利用index即可在O(1)時間對Array的資料做存取。
> 2.	較Linked list為節省記憶體空間：因為Linked list需要多一個pointer來記錄下一個node的記憶體位置。
>
> `缺點` ：
> 1.新增/刪除資料很麻煩：若要在第一個位置新增資料，就需要O(N)時間把矩陣中所有元素往後移動。同理，若要刪除第一個位置的資料，也需要O(N)時間把矩陣中剩餘的元素往前移動。
> 2.若資料數量時常在改變，要時常調整矩陣的大小，會花費O(N)的時間在搬動資料(把資料從舊的矩陣移動到新的矩陣)。
>
> `適用時機`：
> 1.	希望能夠快速存取資料。
> 2.	已知欲處理的資料數量，便能確認矩陣的大小。
> 3.	要求記憶體空間的使用越少越好。


### Linked list
> `優點`：
> 1.	新增/刪除資料較Array簡單：只要對O(1)個node(所有與欲新增/刪除的node有pointer相連的node)調整pointer即可，不需要如同Array般搬動其餘元素。
> 2.	若要刪除特定node，或者在特定位置新增node，有可能需要先執行O(N)的「搜尋」。
> 3.	Linked list的資料數量可以是動態的，不像Array會有resize的問題。
>
> `缺點` ：
> 1.	因為Linked list沒有index，若要找到特定node，需要從頭(ListNode *first)開始找起，搜尋的時間複雜度為O(N)。
> 2.	需要額外的記憶體空間來儲存pointer。
>
> `適用時機`：
> 1.	無法預期資料數量時，使用Linked list就沒有resize的問題。
> 2.	需要頻繁地新增/刪除資料時。

## 參考網站
> * [Linked List: 新增資料、刪除資料、反轉](http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html)
> * [Linked List: Intro(簡介)](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
> * [707. Design Linked List - 知乎](https://zhuanlan.zhihu.com/p/50563240)
> * [用python實作linked-list - Tobby Kuo - Medium](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)
> * [Singly Linked List: How To Insert and Print Node | Python Central](https://www.pythoncentral.io/singly-linked-list-insert-node/)

## 題目練習
>  [**Leetcode | 707 Designed Linked List**](https://leetcode.com/problems/design-linked-list/)　　前往>>  [我的練習程式碼](https://github.com/chenjanice/Data-Structure_2019/blob/master/week2/Linkedlist.py)

## 實作概念
> * 我把整個linked-list的實作分成兩個類別（class），一個是包含了資料及指標兩個屬性的節點（class ListNode），另一個則是定義出各種資料結構操作的list本身（class SingleLinkedList）。
> * 程式碼部分很多是參考自[這裡](https://zhuanlan.zhihu.com/p/50563240)，我的完整程式碼[在這](https://github.com/chenjanice/Data-Structure_2019/blob/master/week2/Linkedlist.py)。
> * 由於每個節點只有指向下一個結點，而沒有指出上一個結點，所以屬於single linked-list，相對於有指出上一個節點的double linked-list。
