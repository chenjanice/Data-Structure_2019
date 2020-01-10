#  Codesignal-Python

>#### 1. Collection Truthness  
>```python3
>xs=[()]
>res=[False]*2
>
>if xs:             #一個有物件的list
>    res[0]=True
>if xs[0]:          #None
>    res[1]=True
>    
>print(res)
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>[True, False]
>```




>#### 2. Efficient Comparision 
>```python3
>if L<x**y<=R:                   #correct
>if x**y>L and x**y<=R:   
>if x**y in range(L+1,R+1):
>````````````````````````````````````````````




>#### 3. pecial Conditional  
>```python3
>a=True
>b=False
>print(a == (not b))
>print(not a==b)
>#print(a == not b)  #ERROR
>print(not(a==b))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>True
>True
>True
>```




>#### 4. language Diffrernces (除法java,c++,python)
>```python3
>def division(x,y):
>    return(x//y)
>
>print(division(5,10))
>print(division(15,-4))  
>print(division(-10,-3))
>print(division(-8,2))
>print(division(17,13))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>0
>-4
>3
>-4
>1
>```
>
>```python3
>def division(x,y):
>    return(x/y)
>print(division(5,10))   #-->0
>print(division(15,-4))  #-->-3
>print(division(-10,-3)) #-->3
>print(division(-8,2))   #-->-4
>print(division(17,13))  #--> 1
>````````````````````````````````````````````
>
>#### **OUTPUT**
>```
>0.5
>-3.75
>3.3333333333333335
>-4.0
>1.3076923076923077
>```
>#### **Note**
> * Java、C/C++遵循的取整方式为：向零取整
> * Python遵循的取整方式为：向下取整
>   * 向上取整：即在所有计算的结果中，取最接近+∞的那个值为最终的商。如10 ÷ (-3) = -3……1而不是10 ÷ (-3) = -4……-2。
>   * 向下取整：同理，在所有计算的结果中，取最接近-∞的那个值为最终的商。如-10 ÷ 3 = -4……2而不是-10 ÷ 3 = -3……-1。
>   * 向零取整：即，在所有计算的结果中，取最接近0的那个值为最终的商。




>#### 5. Count Bits (十進位轉二進位)
>```python3
>def countBits(n):
>    return n.bit_length() ##一種method
>
>print(countBits(50))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>6
>```




>#### 6. Modulus (判斷是否為整數)
>##### `方法一`：利用除以1取餘數等於0
>```python3
>def modulus(n):
>    if n%1 == 0:
>        return n % 2
>    else:
>        return -1
>print(modulus(15))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>1
>```
>
>
>##### `方法二`：使用type()
>```python3
>def modulus(n):
>    if type(n) == int:   #使用type()
>        return n % 2
>    else:
>        return -1
>print(modulus(15))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>1
>```





>#### 7. Simple Sort
>##### `方法一`：利用暫存的方式，替換兩數
>```python3
>def simpleSort(arr):
>    n = len(arr)
>    for i in range(n):
>        j = 0
>        stop = n - i
>        while j < stop - 1:
>            if arr[j] > arr[j + 1]:
>                t=arr[j+1]
>                arr[j+1] =arr[j]
>                arr[j]=t
>            j += 1
>    return arr
>arr=[2, 4, 1, 5]
>print(simpleSort(arr))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>[1, 2, 4, 5]
>```
>
>##### `方法二`：直接對調，更為快速！
>```python3
>def simpleSort(arr):
>    n = len(arr)
>    for i in range(n):
>        j = 0
>        stop = n - i
>        while j < stop - 1:
>            if arr[j] > arr[j + 1]:
>                arr[j],arr[j+1]=arr[j+1],arr[j]
>            j += 1
>    return arr
>arr=[2, 4, 1, 5]
>print(simpleSort(arr))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>[1, 2, 4, 5]
>```





>#### 8. Base Conversion (任意進位 轉為 十六進位)
>```python3
>import os,sys
>def baseConversion(n, x):
>    return  hex(int(str(n),x))[2:]
>print(con(1302,5))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>ca
>```
>#### **Note**
>> * 先將任意進位轉為十進位：int('任意進位數字(須為字串)',x進位制)
>> * 再將十進轉為十六進位：hex(十進位數字(須為int))
>> * 刪除開頭的0x，只印出後面的：[2:]




>#### 9. Mex Fuction
>```python3
>def mexFunction(s, upperBound):
>    found = -1
>    for i in range(upperBound):
>        if not i in s:
>            found = i
>            break
>    else:
>        found = upperBound
>    return found
>
>s=[0, 4, 2, 3, 1, 7]
>upperBound=10
>print(mexFunction(s,upperBound))
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>5
>```




>#### 10. List Beautiful 
>##### `方法一`：利用pop刪除第一個值與最後一個值
>```python3
>def listBeautifier(a):
>    res = a[:]
>    while res and res[0] != res[-1]:
>        res.pop(0)  #利用pop刪除第一個值與最後一個值
>        res.pop(-1)
>    return res
>
>a=[3, 4, 2, 4, 38, 4, 5, 3, 2]
>listBeautifier(a)
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>[4, 38, 4]
>```
>
>##### `方法二`：利用extended unpacking
>```python3
>def listBeautifier(a):
>    res = a[:]
>    
>    while res and res[0] != res[-1]:
>        a, *res, b=res #利用extended unpacking
>    return res
>
>a=[3, 4, 2, 4, 38, 4, 5, 3, 2]
>listBeautifier(a)
>````````````````````````````````````````````
>#### **OUTPUT**
>```
>[4, 38, 4]
>```
