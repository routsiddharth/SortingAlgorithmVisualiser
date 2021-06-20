def ShellSort(arr):

    subarrs = len(arr) // 2

    while subarrs > 0:

      for start_position in range(subarrs):
        yield from GISort(arr, start_position, subarrs)

      subarrs //= 2

def GISort(nlist,start,gap):

    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position >= gap and nlist[position-gap] > current_value:

            nlist[position]=nlist[position-gap]
            position = position-gap
            yield nlist

        nlist[position] = current_value
        yield nlist