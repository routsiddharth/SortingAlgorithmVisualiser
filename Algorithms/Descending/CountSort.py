def CountSort(arr):

    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
        yield arr[::-1]

    i = 0

    for a in range(m):
        for c in range(count[a]):

            arr[i] = a
            i += 1
            yield arr[::-1]

        yield arr[::-1]