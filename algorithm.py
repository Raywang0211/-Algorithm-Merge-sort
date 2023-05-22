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