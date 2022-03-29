from collections import namedtuple
#from sys import stdin


Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    # first get our starting segment by sorting in place. When done the first element has the min start number
    segments.sort(key=lambda x: x.start)
    max_points = 0
    touchpoints = []
    while len(segments) > 1:
        touchpoints = []
        touchpoints.append(segments[0])
        current_segments = segments.copy()
        for n in range(1,len(current_segments)):
            if current_segments[n][0] >= current_segments[0][0] and current_segments[n][0] <= current_segments[0][1]:
                touchpoints.append(current_segments[n])
        for index in sorted(touchpoints, reverse=True):
            del segments[index]
        print (len(segments))
        if len(touchpoints) > 0:
            max_points += 1
    return max_points

segment1 = [Segment(1, 3), Segment(2, 5), Segment(3, 6)]
segment2 = [Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]

compute_optimal_points(segment1)

