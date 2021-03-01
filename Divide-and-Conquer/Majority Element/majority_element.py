# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    left = 0
    right = len(elements)

    if left == right:
        return -1
    if left+1 == right:
        return elements[left]

    left_part = majority_element(elements[:left + (right-left)//2])
    right_part = majority_element(elements[left + (right-left)//2:])

    left_count = 0
    for i in elements:
        if i == left_part:
            left_count += 1
    if left_count > (right-left)//2:
        return left_part

    right_count = 0
    for i in elements:
        if i == right_part:
            right_count += 1
    if right_count > (right - left)//2:
        return right_part

    return -1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    #print(majority_element_naive(input_elements))
    print(1 if majority_element(input_elements) != -1 else 0)
