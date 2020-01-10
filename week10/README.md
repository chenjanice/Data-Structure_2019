# Red Black Tree 紅黑樹

紅黑樹（英語：Red–black tree）是一種自平衡二元搜尋樹，是在電腦科學中用到的一種資料結構，典型的用途是實現關聯陣列。

## 性質
紅黑樹是每個節點都帶有顏色屬性的二元搜尋樹，顏色為紅色或黑色。在二元搜尋樹強制一般要求以外，對於任何有效的紅黑樹我們增加了如下的額外要求：

1. 節點是紅色或黑色。
2. 根是黑色。
3. 所有葉子都是黑色（葉子是NIL節點）。
4. 每個紅色節點必須有兩個黑色的子節點。（從每個葉子到根的所有路徑上不能有兩個連續的紅色節點。）
5. 從任一節點到其每個葉子的所有簡單路徑都包含相同數目的黑色節點。

## 具體的紅黑樹的圖例：
![image](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Red-black_tree_example.svg/450px-Red-black_tree_example.svg.png)

## 操作
因為每一個紅黑樹也是一個特化的二元搜尋樹，因此紅黑樹上的唯讀操作與普通二元搜尋樹上的唯讀操作相同。然而，在紅黑樹上進行插入操作和刪除操作會導致不再符合紅黑樹的性質。恢復紅黑樹的性質需要少量（{\displaystyle {\text{O}}(\log n)}{\displaystyle {\text{O}}(\log n)}）的顏色變更（實際是非常快速的）和不超過三次樹旋轉（對於插入操作是兩次）。雖然插入和刪除很複雜，但操作時間仍可以保持為{\displaystyle {\text{O}}(\log n)}{\displaystyle {\text{O}}(\log n)}次。

## 參考資料
* [紅黑樹 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E7%BA%A2%E9%BB%91%E6%A0%91)
