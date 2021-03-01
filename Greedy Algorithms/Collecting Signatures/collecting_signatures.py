# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    answer = []
    segments = sorted(segments, key = lambda x: x.end)
    signed_upto = -1
    for s in segments:
        if signed_upto < s.start:
            signed_upto = s.end
            answer.append(s.end)
    return answer


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
