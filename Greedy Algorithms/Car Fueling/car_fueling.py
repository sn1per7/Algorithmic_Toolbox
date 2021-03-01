# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    '''stops.append(d)
    dis_covered = 0
    no_stops = 0
    last_stop = -1

    while dis_covered < d:
        #print(dis_covered)
        possible_stop = 0
        if stops[last_stop if last_stop >= 0 else (last_stop + 1)] + m >= d:
            dis_covered = d
            #print("reached")
            break
        for i in range(last_stop+1, len(stops)):
            #print(i)
            if stops[i] <= (dis_covered+m) and stops[i] < d:
                possible_stop = 1
                last_stop = i
                continue
            else:
                if possible_stop == 0:
                    return -1
                no_stops += 1
                dis_covered = stops[last_stop]
                break

    return no_stops'''

    no_stops = 0
    curr_stops = 0
    stops = [0] + stops + [d]
    while curr_stops <= len(stops)-2:
        last_stops = curr_stops
        while curr_stops <= len(stops)-2 and stops[curr_stops+1]-stops[last_stops] <= m:
            curr_stops += 1
        if curr_stops == last_stops:
            return -1
        if curr_stops <= len(stops)-2:
            no_stops += 1

    return no_stops


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
