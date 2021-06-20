def QuickSort(arr, left, right):
    
    if left >= right:
        return arr
    
    pivot = arr[right]
    index = left
    
    for i in range(left, right):
        
        if arr[i] < pivot:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        
        yield arr

    arr[right], arr[index] = arr[index], arr[right]

    yield arr
    yield from QuickSort(arr, left, index - 1)
    yield from QuickSort(arr, index + 1, right)