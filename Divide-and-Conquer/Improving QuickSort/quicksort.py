# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    j = i = left
    k = right
    while i <= k:
        if array[i] < x:
            array[i], array[j] = array[j], array[i]
            j += 1
            i += 1
        elif array[i] == x:
            i += 1
        else:
            array[k], array[i] = array[i], array[k]
            k -= 1
    return j, k


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    #make a call to partition3 and then two recursive calls
#to randomized_quick_sort
    p1, p2 = partition3(array, left, right)

    randomized_quick_sort(array, left, p1-1)
    randomized_quick_sort(array, p2+1, right)



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
