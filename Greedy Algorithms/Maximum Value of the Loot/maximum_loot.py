# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    answer = 0
    price_per_weight = []
    for i in range(len(prices)):
        price_per_weight.append(prices[i]/weights[i])
    price_per_weight, sweights, sprices = zip(*sorted(zip(price_per_weight, weights, prices), reverse=True))
    '''print(price_per_weight)
    print(sprices)
    print(sweights)'''
    weight_remaining = capacity
    for i in range(len(sprices)):
        curr_capacity = min(sweights[i], weight_remaining)
        weight_remaining -= curr_capacity
        answer += (sprices[i]*curr_capacity)/sweights[i]
        if weight_remaining == 0:
            break

    return answer

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    '''input_capacity = 650
    input_prices = [100, 40, 500, 800]
    input_weights = [50, 10, 250, 1000]'''
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
