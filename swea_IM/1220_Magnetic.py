T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    # sum = 0
    count = 0
    # 매그내릭 1과 2의 교착상태 구하기

    for j in range(N):  # 열로 짜른 슬라이싱 구하기
        for i in range(N):
            col = [arr[i][j] for i in range(N)]
        for start in range(len(arr) - N + 1):
            end = start + N
            sliced_part = col[start:end]    # sliced_part = for 문 돌리기 편하게 slice
            # print(sliced_part)

        for n in sliced_part:   
            if n == 1 and not stack:    # n이 1이거나 스택에 없으면
                stack.append(n)         # 스택에 넣기
            elif n == 2:                # n이 2일때
                if stack:               # 스택이 존재하면
                    stack.pop()         # 1을 pop
                    count += 1          # count +1 해주기
                elif not stack:         # 스택이 없으면
                    pass                # 패스
                # sum += count
        if stack:
            stack = []                  # 빛 가람의 도움으로
                                        # stack을 매번 초기화 시켜줘야지 지인아 제발 생각을 좀
    print(f'#{tc} {count}')
