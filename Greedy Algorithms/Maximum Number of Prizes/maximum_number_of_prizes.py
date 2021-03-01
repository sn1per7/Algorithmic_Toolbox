# python3
import math

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    d = (1**2) - (4*1* -(2*n))
    sol1 = ((-1+(math.sqrt(d)))/2)
    sol2 = ((-1-(math.sqrt(d)))/2)
    for i in range(1, math.floor(sol1)):
        summands.append(i)

    summands.append(n - sum(summands))
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
