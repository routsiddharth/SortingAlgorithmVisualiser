def HeapSort(arr):

    n = len(arr)

    for i in range(n, -1, -1):
        yield from heapify(arr,n,i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        yield arr
        yield from heapify(arr, i, 0)

def heapify(arr, n, i):

    largest = i
    l = i*2+1
    r = i*2+2

    while l < n and arr[l] > arr[largest]:
        largest = l

    while r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        yield arr
        yield from heapify(arr, n, largest)