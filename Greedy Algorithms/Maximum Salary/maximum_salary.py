# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = list(map(str, numbers))
    #print(numbers)
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] + numbers[j+1] < numbers[j+1] + numbers[j]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

    answer = "".join(numbers)
    #print(answer)
    return int(answer)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
