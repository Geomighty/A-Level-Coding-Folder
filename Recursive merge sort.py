def SplitList(array):
    length = len(array)
    split_point = length // 2
    array_left_half = array[:split_point]
    array_right_half = array[split_point:]
    return array_left_half, array_right_half

def MergeTwoLists(array_left_half, array_right_half):
    array = []
    left_point = 0
    right_point = 0
    while len(array) != (len(array_left_half) + len(array_right_half)):
        if array_left_half[left_point] > array_right_half[right_point]:
            array.append(array_right_half[right_point])
            right_point += 1
        elif array_left_half[left_point] < array_right_half[right_point]:
            array.append(array_left_half[left_point])
            left_point += 1
        else:
            array.append(array_left_half[left_point])
            array.append(array_right_half[right_point])
            left_point += 1
            right_point += 1

def MergeSort(array):
    if len(array)