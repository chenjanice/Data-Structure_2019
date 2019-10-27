{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# quicksort main class\n",
    "\n",
    "def quickSort(alist): #帶入需排序的list\n",
    "    \n",
    "    quickSortHelper(alist,0,len(alist)-1) \n",
    "    #參數：需排序的list,第一個值的index,最後一個值的index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#基準點左右的數列，繼續進入partition做比較\n",
    "\n",
    "def quickSortHelper(alist,first,last): \n",
    "    \n",
    "    if first<last:  #當[第一個值的index]<[最後一個值的index]\n",
    "        \n",
    "        splitpoint = partition(alist,first,last) \n",
    "        #將參數帶入partition\n",
    "        \n",
    "        quickSortHelper(alist,first,splitpoint-1)\n",
    "        #將基準點左邊的再比較一次 \n",
    "        #參數：list,第一個值的index,基準點左邊一個值的index\n",
    "        \n",
    "        quickSortHelper(alist,splitpoint+1,last)\n",
    "        #將基準點右邊的再比較一次 \n",
    "        #參數：list,基準點右邊一個值的index,最後一個值的index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def partition(alist,first,last):\n",
    "    \n",
    "    pivotvalue = alist[first] #使list中第一個值為基準點\n",
    "    \n",
    "    leftmark = first+1  #左邊指標：從基準點右邊第一個值的index開始\n",
    "    \n",
    "    rightmark = last  #右邊指標：最後一個值的index\n",
    "    \n",
    "    done = False  #預設 while 能 run\n",
    "    \n",
    "    while not done:\n",
    "        \n",
    "        while leftmark <= rightmark and alist[leftmark] <= pivotvalue: # 當左指標<=右指標 且 左指標之值 <=基準點：\n",
    "            leftmark +=  1                                             # 此值不動，且讓左指標+1，繼續檢查右邊一個值\n",
    "        \n",
    "        while alist[rightmark] >= pivotvalue and rightmark >= leftmark: # 當左指標<=右指標 且 右指標之值 >=基準點：\n",
    "            rightmark -=  1                                             # 此值不動，且讓右指標-1，繼續檢查左邊一個值\n",
    "            \n",
    "        if rightmark < leftmark:                                        # 當 右指標  <  左指標：\n",
    "            done = True                                                 # 此迴圈暫停\n",
    "        \n",
    "        else:                                                           #否則：使左右指標之值交換\n",
    "            temp = alist[leftmark]\n",
    "            alist[leftmark] = alist[rightmark]\n",
    "            alist[rightmark] = temp\n",
    "    \n",
    "    #使 [基準點] 與 [右指標之值] 交換\n",
    "    temp = alist[first]\n",
    "    alist[first] = alist[rightmark]\n",
    "    alist[rightmark] = temp\n",
    "    \n",
    "    #回傳[右指標的index]=現在基準點現在所在的位置\n",
    "    return rightmark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9, 11, 20, 23, 32, 33, 43, 55, 67, 89, 99, 100]\n"
     ]
    }
   ],
   "source": [
    "alist = [33,55,43,89,11,32,9,67,99,20,23,100]\n",
    "quickSort(alist)\n",
    "print(alist)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
