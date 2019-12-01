## Binary Search Tree 功能說明 
--------------------------------------------------

### Insert
> `def insert (self,root,val):` 
>  * 此功能即是在一個以root為根的二元搜尋樹中，新增一個值為val的節點。  
>  * 首先，帶入root與value之後，會先檢查root是不是存在，若root為None，則令root為TreeNode(val)為根節點。  
>  * 若root存在，則令current=root並將要插入的值value和root值比較，若value較大，且root.right為空值，則將value建立一個節點放在這個位置；若此位置並非空值，則將current =current .right，利用while迴圈（符合bst的規則）直到找到正確的位置並且為空值，則可insert節點在這個位置上。    
>  * 若value小於等於root的值，且toot.left為空值，則insert value在此；若非空值則同上述（除走訪方向為current =current.left）。
>

### Search
> `def search (self,root,target):`
>  * 此功能在於尋找以root為根節點的二元搜尋樹，值為target且離root最近的節點。   
>  * 這個功能寫成一個recursion，首先將root值和target比較，若target較大則再帶入以root.right（若target較小則為root.left）為節點的方式，繼續尋找target，直到root值等於target，表示找到值，回傳此節點（此時節點為root）。
> 

### Delete
> `def delete(self,root,target):`
>  * 我在delete寫了兩個function，一個為deletenode（只刪除一個節點）、delete則為利用while迴圈將所有的target值刪除，最後再回傳刪除完的root。  
>  * 再deletenode當中，會讓root值做recursion不斷與target比較，target值若比root值大，則將root.right為root帶入deletnode中（若較小則帶入root.left），直到root為和target值相等的節點。則判斷此節點有幾個小孩，若沒有小孩則直接刪除；若有一個小孩則，先令其小孩為temp，再將root的父母直接指向小孩；若有兩個小孩，則先找到右子樹的最小值節點，並且將root的值更新為此最小值，再將這個最小值節點刪除。  
>

### Modify
> `def modify (self,root,target,new_val):`
>  * 此功能為修正，將以root為根節點的二元搜尋樹中所有值為target的節點更正為新值new_val。考量到修正完仍需符合二元搜尋樹的規則，因此此功能拆解則為，刪除二元搜尋樹中所有值為target的節點，並且插入同等數量的new_val。在程式設計當中，我先用preorder 的探訪，將整棵樹輸出成一個list，並且在這個list當中計算值為target的節點總數c。接著，利用for迴圈進行c次的刪除（delete）與插入（insert），此方式可確保修正後的二元搜尋樹仍符合規則。  
>

-----------------------------------
### 參考資料
>  * [(126) Delete a node from Binary Search Tree - YouTube](https://www.youtube.com/watch?v=gcULXE7ViZw)
>  * [二元樹(Binary Tree)基礎 -](https://kopu.chat/2017/06/18/%e4%ba%8c%e5%85%83%e6%a8%b9/)

