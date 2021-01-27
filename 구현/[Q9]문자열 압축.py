def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        result = ""
        prev = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + prev
                else:
                    result += prev
                prev = s[j:j + i]
                count = 1
        if count >= 2:
            result += str(count) + prev
        else:
            result += prev
        answer = min(answer, len(result))
    return answer