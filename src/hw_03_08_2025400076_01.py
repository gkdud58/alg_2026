def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    pass
 

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    pass


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        while i-1 >= 0 and temp < array[i-1]:
            array[i] = array[i-1]
            i -= 1
        array[i] = temp
    pass

if __name__ == "__main__":

    data = [42, 17,8,99,23,4,75,61,30,12]
    bubble_data = list(data)
    print("Bubble Sort")
    print("정렬 전:", bubble_data)

    bubble_sort(bubble_data)
    print("정렬 후:", bubble_data)
    print()

    selection_data = list(data)
    print("Selection Sort")
    print("정렬 전:", selection_data)

    selection_sort(selection_data)
    print("정렬 후:", selection_data)
    print()

    insertion_data = list(data)
    print("Insertion Sort")
    print("정렬 전:", insertion_data)

    insertion_sort(insertion_data)
    print("정렬 후:", insertion_data)
