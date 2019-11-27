## Stack 堆疊
> 具有 **「Last-In-First-Out」** 的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。 
> 
> 特點： 
> 1. 先入後出，後入先出。  
> 2. 除頭尾節點之外，每個元素有一個前驅，一個後繼。   

#### 操作：  
> *  Push(data)：把資料放進Stack。
>    * 把書放進箱子。
> *  Pop：把「最上面」的資料從Stack中移除。
>    * 把位於箱子「最上面」的書拿出來。
> *  Top：回傳「最上面」的資料，不影響資料結構本身。
>    * 確認目前位於箱子「最上面」的是哪本書。
> *  IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。
>    * 確認箱子裡面有沒有書。
> *  getSize：回傳Stack裡的資料個數，不影響資料結構本身。
>    * 記錄目前箱子已經裝了多少本書。

#### 參考資料：  
> *  [Stack: Intro(簡介)](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)  
> *  [Stack: 以Array與Linked list實作](http://alrightchiu.github.io/SecondRound/stack-yi-arrayyu-linked-listshi-zuo.html)  
> *  [堆疊 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%A0%88)  


## Queue 隊列
> 具有「First-In-First-Out」的資料結構，如同排隊買車票的隊伍即可視為Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。
>
> 特點：
> 1. 隊伍有前方(以front表示)以及後方(以back表示)之分。
> 2. 若要進入隊伍(Push)，一定是從back進入。
> 3. 若要離開隊伍(Pop)，一定是從front離開。

### 操作：
> * Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。
>    * 在Queue中新增資料又稱為enqueue。
> * Pop：把front所指向的資料從Queue中移除，並更新front。
>   * 從Queue刪除資料又稱為dequeue。
> * getFront：回傳front所指向的資料。
> * getBack：回傳back所指向的資料。
> * IsEmpty：確認Queue裡是否有資料。
> * getSize：回傳Queue裡的資料個數。

### 應用：
> * 演算法：Breadth-First Search(廣度優先搜尋)與Tree的Level-Order Traversal會用到Queue。
> * 作業系統：被多個程式共享的資源(例如CPU、印表機、網站伺服器)，一次只能執行一個需求(例如request、interrupt)，因此需要有個Queue來安排多個程式的執行順序(例如device queue、job queue)。

#### 參考資料：  
> *  [Queue: Intro(簡介)，並以Linked list實作](http://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html)
