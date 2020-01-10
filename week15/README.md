# Kruskal's algorithm(找Minimum Spanning Tree)

### 簡介
- Kruskal 演算法是一種用來尋找 MST(minimum spanning tree) 的演算法
- 依次找尋圖形中加權值最小的邊加入spanning tree，嘗試連結圖的N個頂點，但不使用會造成圖形成環路的邊，直到產生N-1個邊。
- **生成樹Spanning Tree**：
   - 一棵【包含圖上所有點】的樹，稱作該圖的生成樹
   - 一張圖的生成樹可能會有很多種
   - 完全連通圖才有生成樹 (不連通時，則稱為生成森林)
   - 生成樹的權重為樹上每條邊的權重總和
- **最小生成樹Minimum Spanning Tree**：擁有最小權重的生成樹，稱為最小生成樹

### 舉例
![image](http://wiki.csie.ncku.edu.tw/acm/MST_Kruskal.gif)

### 作法

1. 將所有的邊，依照權重的大小排序。
2. 依序加入權重最小的邊，如果造成cycle時，則必須捨棄。
3. 直到增加了n - 1條邊為止。(假設有 n 個節點)

### 流程圖
![image](https://raw.githubusercontent.com/chenjanice/Data-Structure_2019/master/images/Dijkstra%26Krusdal.jpg)


### 參考資料
* [克魯斯克爾演算法 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)
* [Wiki - acm/course/MST](http://wiki.csie.ncku.edu.tw/acm/course/MST)
* [克魯斯克爾演算法 (Kruskal's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/kruskal.html)

-----------------------------------------------------
