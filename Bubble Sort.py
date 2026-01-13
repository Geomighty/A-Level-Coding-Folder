def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] > array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array

numbers = [23, 17, 45, 6, 78, 21]
print(bubble_sort(numbers))