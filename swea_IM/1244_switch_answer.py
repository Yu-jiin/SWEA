

N = int(input())
switch = [0] + list(map(int, input().split()))
M = int(input())

def change(sex, idx, switch):
    if sex == 1:                                           # 남자
        for i in range(1, N+1):
            if i % idx == 0:
                switch[i] = [1, 0][switch[i]]
    else:                                                     # 여자
        max_len = min(idx-1, N-idx)
        while max_len >= 0:
            if switch[idx-max_len:idx+max_len+1] == switch[idx-max_len:idx+max_len+1][::-1]:
                for j in range(idx-max_len, idx+max_len+1):
                    switch[j] = [1, 0][switch[j]]
                return
            max_len -= 1

# 함수 적용
for _ in range(M):
    sex, idx = map(int, input().split())
    change(sex, idx, switch)

# 몇줄 출력할지 정하기
if N % 20 == 0:
    print_times = N//20
else:
    print_times = (N//20) + 1

# 출력하기
for idx in range(print_times):
    answer = switch[1+20*idx:1+20*idx+20]
    ans = ' '.join(str(info) for info in answer)
    print(ans)