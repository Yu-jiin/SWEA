t = 'TTTTTABC'
p = 'TTA'
N = len(t)
M = len(p)
cnt = 0
for i in range(N-M+1):  # 비교구간의 시작위치
    for j in range(M):
        if t[i + j] != p[j]:
            break   #  for j, 다음 글자부터 비교 시작
    else:   # for j가 중단없이 반복되면
        cnt += 1    # 패턴 개수 1증가

print(cnt)

# 최악의 경우 텍스트의 모든 위치에서 패턴을 비교해야 함으로 길이가 길고
# 패턴이 긴 문자열에서는 어마무시한 비교가 일어난다
#  비교횟수를 줄일 수 있는 방법은 ?
    # = KMP 알고리즘 



