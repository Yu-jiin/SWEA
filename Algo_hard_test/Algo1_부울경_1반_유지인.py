T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count = 1                                   # 세는 값 (조건에 맞지않을 때 마다 초기화 됨)
    final_count = 1                             # 최종 결과

    for i in range(1, N-1):                     # 인덱스 처리를 위해 1부터, N-1까지
        for x in range(1, N//2+1):              # 좌우 대칭을 위한 for 문
            if 0 <= i-x < N and 0 <= i+x < N:   # index out of range 방지
                if arr[i-x] == arr[i+x]:        # 좌우가 같다면
                    count += 2                  # count를 2씩 증가
                    if final_count < count:     # final_count 보다 count가 크다면 갱신
                        final_count = count
                        # count = 0
                else:
                    count = 1                   # 좌우 대칭이 같지않다면 count를 초기화하고 break
                    break
            else:                               # index를 벗어났다면 count 초기화 및 break
                count = 1
                break
        else:
            count = 1
            break

    print(f'#{tc} {final_count}')
