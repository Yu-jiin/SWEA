T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [input().strip() for _ in range(N)]

    max_value = 1
    max_word = ""
    # 행 비교
    for i in range(N):
        for j in range(N):
            for k in range(j, N):
                string1 = ""
                for l in range(j, k+1):
                    string1 += arr[i][l]
                # print(string1)



