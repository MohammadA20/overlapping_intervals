"""
    This program will merge the overlapping intervals in the list,
    it works as a sequence if numbers,
    if the maximum of the first
    is greater than the minimum of the second list and less than the maximum second,
    then overlapp minimum first with max second
"""

def merge_intervals(intervals):
    """
    Function of merge will take a list of intervals
    """
    intervals.sort(key = lambda start: start[0])
    overlapping_sequence = []
    start_sequence, increment_sequence = intervals[0]
    for start in range(len(intervals)):
        start_loop, end_loop = intervals[start]
        if start_loop <= increment_sequence:
            increment_sequence = max(increment_sequence, end_loop)
        else:
            overlapping_sequence.append([start_sequence, increment_sequence])
            start_sequence = start_loop
            increment_sequence = end_loop
    overlapping_sequence.append([start_sequence, increment_sequence])
    return overlapping_sequence
MERGE_OVERLAPPING = merge_intervals([[2,8],[4,10],[5,6]])
print(MERGE_OVERLAPPING)
