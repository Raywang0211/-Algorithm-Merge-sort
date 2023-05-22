# -Algorithm-Merge-sort
using resursion to sove merge sort

### 簡介：

主要的排序思維是將一整個數組進行拆分，拆分完之後再組合，且組合的過程中進行排序，由小到大或由大到小

## 執行過程：

會使用到遞迴的divid and conquer (top-down)，整個流程分成兩個步驟，拆分以及排序合併

1. 拆分: 將list拆分成1:N N:-1 的兩組list，一路拆分到當元素剩下一個時停止
2. 排序合併: 建立一個新的result list，開始比較兩個list的元素大小進行合併。

bottom up 

1. 直接將list差分成獨立的元素
2. 排序合併

### 舉例：

[1,3,5,2,6,4,7]

1. 拆分:

[1,3,5,2],[6,4,7]

[1,3],[5,2],[6,4][7]

[1],[3],[5],[2],[6],[4],[7]

1. 排序合併:

[1,3],[2,5],[4,6],[7]

[1,2,3,5],[4,6,7]

[1,2,3,4,5,6,7]

## 注意：

分成 top-down跟bottom up，範例為top-down

## 複雜度：

時間複雜度

最差：O(nlogn)

最佳：O(nlogn)

平均：O(nlogn)

空間複雜度: O(1)

最差：O(n)

## 程式：

```python
data = [1,3,5,2,6,4,7]

def merge(left, right):
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result+left if len(left) else result+right
    return result

def mergeSort(array):
    #base case
    if len(array) < 2:
        return array
    
    #splite relative
    mid = len(array)//2
    leftArray = array[:mid]
    rightArray = array[mid:]

    return merge(mergeSort(leftArray),mergeSort(rightArray))

print(mergeSort(data))
```
