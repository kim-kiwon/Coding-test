array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selectionsort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] #swap 기능.

def insertionsort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break #자신보다 더 작은놈을 만나면 break. 즉 이미 거의 정렬된 상태라면 시간복잡도 매우적음.

def quicksort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quicksort(array, start, right-1)
    quicksort(array, right + 1, end)


def countsort(array):
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end = ' ')

#insertionsort(array)
#selectionsort(array)
#quicksort(array, 0, len(array)-1)
#print(array)
countsort(array)