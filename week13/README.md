# 深度優先搜尋（Depth-First Search）

### 簡介
核心精神便如同Pre-Order Traversal：「先遇到的vertex就先Visiting」，並且以先遇到的vertex作為新的搜尋起點，直到所有「有edge相連的vertex」都被探索過。
沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。屬於盲目搜尋。

### 動畫實例
![image](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Graph%20series/DFS_fig/maze.gif?raw=true)

### 作法
1. 利用一個 **Queue**一個**Stack** -- 後進先出
2. Queue放已經走訪的點
3. Stack放已經走訪的點的鄰點
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
* [Graph: Depth-First Search(DFS，深度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
* [深度優先搜尋 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)
