list1 = [23, 12, 567, 34, 89, 9, 5,]
def sel_sort(array, size):
    for i in range(size -1):
        min = i
        for j in range(i+1, size):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
size = len(list1)
sel_sort(list1, size)
print(list1)


#done