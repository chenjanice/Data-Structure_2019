# Binary Search Tree

* 二元搜尋樹（英語：Binary Search Tree）：是指一棵空樹或者具有下列性質的二元樹：
   1. 若任意節點的左子樹不空，則左子樹上所有節點的值均小於它的根節點的值
   2. 若任意節點的右子樹不空，則右子樹上所有節點的值均大於它的根節點的值
   3. 任意節點的左、右子樹也分別為二元搜尋樹
   4. 沒有鍵值相等的節點

####  `尋找`:  
   1. 若b是空樹，則搜尋失敗，否則：
   2. 若x等於b的根節點的資料域之值，則尋找成功；否則：
   3. 若x小於b的根節點的資料域之值，則搜尋左子樹；否則：
   4. 尋找右子樹。
   
   *【 Pre-Order Traversal 】*
     * Depth-First Search(DFS，深度優先搜尋)的核心精神便如同Pre-Order Traversal：「先遇到的vertex就先Visiting」
     * 只要有路就繼續往前走！


#### `插入(向一個二元搜尋樹b中插入一個節點s的演算法)`:  
   1. 若b是空樹，則將s所指節點作為根節點插入，否則：
   2. 若s->data等於b的根節點的資料域之值，則返回，否則：
   3. 若s->data小於b的根節點的資料域之值，則把s所指節點插入到左子樹中，否則：
   4. 把s所指節點插入到右子樹中。（新插入節點總是葉子節點）


#### `刪除(分三種情況討論)`:  
   - Case1：no child  直接刪
   - Case2：one child 父母直接指向小孩
   - Case3：2 child 找到右子樹的最小值(或左子樹最大值)、更新數字、並將被移上去的數字刪除。此時再根據遇到的情況做case123的方式處理
   

   
## 參考資料

* [二元搜尋樹 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)

* [Graph: Depth-First Search(DFS，深度優先搜尋)](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

* [樹的前序、中序、後序遍歷及深度優先算法DFS、廣度優先算法BFS及python實現 - 台部落](https://www.twblogs.net/a/5c9ea876bd9eee7523887fc1)

* [Binary Search Tree: Search(搜尋資料)、Insert(新增資料)](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)

*  [Binary Search Tree | Set 2 (Delete) - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)
