# Dijkstra's algorithm(Single Source Shortest Paths)

### 簡介
- 每次新擴展一個距離最短的點，更新與其相鄰的點的距離。
- 當所有邊權都為正時，由於不會存在一個距離更短的沒擴展過的點，所以這個點的距離永遠不會再被改變，因而保證了演算法的正確性。
- 不能有負權邊，因為擴展到負權邊的時候會產生更短的距離，有可能就破壞了已經更新的點距離不會改變的性質。

### 舉例
如果圖中的頂點表示城市，而邊上的權重表示著城市間開車行經的距離。 Dijkstra演算法可以用來找到兩個城市之間的最短路徑。
![image](https://wiki.mbalib.com/w/images/6/65/Dijkstra%E7%AE%97%E6%B3%95%E5%9B%BE.jpg)

### 作法

1. 頂點放入群組
2. 把頂點的cost放入matrix：第一步驟


3. 找到最小值
4. 將最小值放入群組
5. 群組內的cost直接貼上
6. 群組外飛0的cost一一比對



7. 重複3-6 直到結束


### 流程圖

![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/Dijkstra%26Krusdal.jpg)



### 參考資料
* [Dijkstra演算法 - MBA智库百科](https://wiki.mbalib.com/zh-tw/Dijkstra%E7%AE%97%E6%B3%95)
* [戴克斯特拉算法 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)
* [代克思托演算法 (Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)

-----------------------------------------------------
