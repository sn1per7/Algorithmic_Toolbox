# python3


def linear_search(keys, query):

    for i in range(len(keys)):
        if keys[i] == query:
            return i
    return -1


def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4
    lower_bound = 0
    upper_bound = len(keys) - 1

    while lower_bound <= upper_bound:
        mid = lower_bound + (upper_bound - lower_bound) // 2
        if keys[mid] == query:
            return mid
        elif query < keys[mid]:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return -1

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    #input_keys = list(range(10**4))
    #input_queries = [287]
    #linear_search(input_keys, input_queries)
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
