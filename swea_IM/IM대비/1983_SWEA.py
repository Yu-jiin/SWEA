# 조교의 성적 매기뿌라
scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

# print(scores)
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    stu_score_list = []
    for _ in range(N):
        test1, test2, hw = map(int, input().split())
        stu_score = (test1 * 0.35) + (test2 * 0.45) + (hw * 0.2)
        stu_score_list.append(stu_score)

    # 뽑을 K 인덱스 뽑아갈비
    target = stu_score_list[K-1]
    stu_score_list.sort(reverse=True)   # 점수 순대로 정렬갈비
    n = N // 10     # 몇명씩 점수 줄 지 정해갈비
    answer = stu_score_list.index(target) // n
    result = scores[answer]
    print(f'#{tc} {result}')



