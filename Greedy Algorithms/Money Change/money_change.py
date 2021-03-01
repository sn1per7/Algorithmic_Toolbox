# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    ans = 0
    ans = ans + money//10
    money = money % 10
    ans = ans + money//5
    money = money % 5
    ans = ans + money
    return ans


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
