# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

def fib_last_digit(n):
    pp = 60
    n = (n % pp)

    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for  i in range(n-1):
        previous, current = current, (previous + current) % 10

    return current


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    side_1 = fib_last_digit(n)
    side_2 = fib_last_digit(n+1)
    #print(str(side_1) + str(side_2))
    ans = (side_1*side_2)%10
    return ans


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
