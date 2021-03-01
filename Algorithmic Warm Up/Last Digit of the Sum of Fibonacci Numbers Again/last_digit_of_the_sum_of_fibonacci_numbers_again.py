# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

def fib_sum_last_digit(index):
    pp = 60
    index = (index % pp) + 2

    previous, current = 0, 1
    if index == 0:
        return 0
    elif index == 1:
        return 1
    for i in range(index - 1):
        previous, current = current, (previous + current) % 10

    if current==0:
        current = 9
    else:
        current = current -1

    return current


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if from_index==0:
        f1 = 0
    else:
        f1 = fib_sum_last_digit(from_index-1)
    f2 = fib_sum_last_digit(to_index)
    if (f2-f1)<0:
        return ((10 + f2) - f1)
    return f2-f1


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
