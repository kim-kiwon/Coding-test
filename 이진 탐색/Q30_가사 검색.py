words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
from bisect import bisect_left, bisect_right

def count_by_range(arr, left_val, right_val):
    right_index = bisect_right(arr, right_val)
    left_index = bisect_left(arr, left_val)
    return right_index - left_index

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    for val in words:
        arr[len(val)].append(val)
        reversed_arr[len(val)].append(val[::-1])
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    for q in queries:
        if q[0] != '?':
            result = count_by_range(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            result = count_by_range(reversed_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(result)
    return answer

print(solution(words,queries))