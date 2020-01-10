# 廣度優先搜尋法（Breadth-First Search）

### 簡介
廣度優先搜尋法（Breadth-First Search, BFS）是一種樹（Tree）或圖（Graph）資料結構的搜索演算法，從圖的某一節點(vertex, node) 開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，才進一步走訪下一層級的節點。可應用於有向圖與無向圖的搜尋。

### 動畫實例
![image](https://seanlhlee.gitbooks.io/acosa/gitBook/pics/AnimatedExample.gif)

### 作法
1. 利用兩個 **Queue** -- 先進先出
2. 一個放已經走訪的點
3. 另一個放已經走訪的點的鄰點
4. 直到結束

# BFS  VS. DFS

### 比較

 項目      |BFS     |DFS
:----------|:--------|:------
定義      |遍歷完畢整張圖，按照就近原則進行。|逐個訪問每一條子路的最深處，再逐個回溯前驅節點。
方法|Queue|Stack
資料存取|先進先出|後進先出
記憶體空間|較多(與狀態數成正比)|較少(與遞迴深度成正比)
時間複雜度|O(|V|+|E|)|O(V+E)
缺點|占用記憶體、無俚頭探索|方向固定、耗時
應用|最短路徑、爬蟲|最大路徑、查找、迷宮、爬蟲

### 流程圖

![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/BFS%26DFS.jpg)

### 參考資料
* [bfs及dfs的比較 - IT閱讀](https://www.itread01.com/content/1541297601.html)
* [BFS & DFS 學習整理 | 程式前沿](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/#outline__1_1_1)
* [BFS 與 DFS 演算法之差異探討](https://www.shs.edu.tw/works/essay/2017/03/2017033023453259.pdf)
* [深度優先遍歷、廣度優先遍歷(dfs,bfs)詳解 - 每日頭條](https://kknews.cc/zh-tw/code/3453n3y.html)
* [資料結構：圖之DFS與BFS的複雜度分析 - IT閱讀](https://www.itread01.com/content/1549064200.html)
* [Breadth-First Search (BFS) · acosa](https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html)
* [Breadth-first search 廣度優先搜尋法](http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html)
-----------------------------------------------------
