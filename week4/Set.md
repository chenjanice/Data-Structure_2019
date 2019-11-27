# Set (集合)
> Set 是不講求順序(order)的資料彙集(collection)
> 用大括號 {} 表示：資料的集合，沒有順序，沒有重複，且為可改變內容（mutable）
> 例如買樂透時，哪個號碼「先對中」並不影響最後的中獎結果。


### 特性
> *　無序性：一個集合中，每個元素的地位都是相同的，元素之間是無序的。
> *　互異性：一個集合中，任何兩個元素都認為是不相同的，即每個元素只能出現一次。
> *　確定性：給定一個集合，任給一個元素，該元素或者屬於或者不屬於該集合，二者必居其一，不允許有模稜兩可的情況出現。


### 操作
>> * `set.add(x)` ：將變數 x 加到集合中。
>> * `set.remove(x)` ：從集合中刪除變數 x，如果集合沒有 x，發生 KeyError。
>> * `set.pop()` ：從集合刪除一個元素，然後回傳該元素，實測應該會刪除第一個。
>> * `set.copy()` ：回傳集合的副本。
>> * `set.clear()` ：刪除集合內的所有元素。
>
>> * `set.issubset(S)` ：如果集合是 S 的子集合，回傳 True，否則回傳 False。
>> * `set.issuperset(S)` ：如果集合是 S 的超集合，回傳 True，否則回傳 False。
>> * `set.isdisjoint(S)` ：如果集合與 S 沒有交集，也就是沒有任何元素是一樣的，回傳 True，否則回傳 False。（英文的 disjoint 是互斥的概念）>
>
>> * `set.union(S)` ：S1|S2，回傳集合聯集 S 的集合。
>> * `set.intersection(S)` ：S1&S2，回傳集合交集 S 的集合。
>> * `set.difference(S)` ：回傳集合差集 S 的集合。
>> * `set.symmetric_difference(S)` ：回傳集合對稱差集 S 的集合（也就是聯集減掉交集的部分）。



## 參考網站
> * [Linked List: 新增資料、刪除資料、反轉](https://zh.wikipedia.org/wiki/%E9%9B%86%E5%90%88_(%E6%95%B0%E5%AD%A6))
> * [Set：以Array表示](http://alrightchiu.github.io/SecondRound/setyi-arraybiao-shi.html)
> * [Python set(集合) 这一定是最全的介绍集合的博文 - Steve Wang's blog - CSDN博客](https://blog.csdn.net/Solo95/article/details/78753265)
> * [Python 學習筆記 #006：序對 Tuple、集合 Set 與字典 Dict 的介紹與使用方法 - Kung’s Daily Life - Medium](https://medium.com/kung-%E7%9A%84%E6%97%A5%E5%B8%B8/python-%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-006-%E5%BA%8F%E5%B0%8D-tuple-%E9%9B%86%E5%90%88-set-%E8%88%87%E5%AD%97%E5%85%B8-dict-33186c42049c)


## 題目練習
>  [**Leetcode | 645. Set Mismatch**](https://leetcode.com/problems/set-mismatch/)　　前往>>  [我的練習程式碼](https://github.com/chenjanice/Data-Structure_2019/blob/master/week4/645.%20Set%20Mismatch.ipynb)

## 實作概念
> * 參考hash的方式：統計每個位置出現的次數
