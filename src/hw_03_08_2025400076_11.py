def heapify(array, root, count):
    left = root * 2+1
    if left >=count:
        return
    right = root*2+2
    largest = left
    if right < count:
        if array[right] > array[largest]:
            largest = right
        if array[largest] > array[root] :
            array[root], array[largest] = array[largest], array[root]
            heapify(array, largest, count)


def heap_sort(array):
    count = len(array)
    if count > 1:
        for root in range(count//2-1, -1, -1):
            heapify(array, root, count)
    for end in range(count-1, 0, -1):
        array[end], array[0] = array[0], array[end]
        heapify(array, 0, end)



def count_sort(array):
    counts = [0] * (max(array) + 1)
    for value in array:
        counts[value] += 1
    result = []
    for value, count in enumerate(counts):
        result.extend([value] * count)
    array[:] = result





if __name__ == "__main__":

    data = [42, 17,8,99,23,4,75,61,30,12]
    heap_data = list(data)
    
    print("Heap Sort")
    print("정렬 전:", heap_data)

    heap_sort(heap_data)
    print("정렬 후:", heap_data)
    print()


    count_data = list(data)
    print("Count Sort")
    print("정렬 전:", count_data)

    count_sort(count_data)
    print("정렬 후:", count_data)
    print()
