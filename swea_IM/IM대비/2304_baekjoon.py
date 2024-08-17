# 창고
N = int(input())
total_list = []
for _ in range(1, N+1):
    L, H = map(int, input().split())
    # L = 기둥 위치
    # H = 높이
    total_list.append([L, H])   # 전체 다 담아버리고
total_list.sort()   # 위치 순으로 오름차순 정렬
# print(total_list)

max_height = 0
for i in range(N):
    if max_height < total_list[i][1]:
        max_height = total_list[i][1]
        max_ground = i

ground_sum = total_list[max_ground][1]

# 제일 높이가 큰 기둥 기준 왼쪽 비교
for j in range(max_ground):
    if total_list[j][1] <= total_list[j+1][1]:
        sum_v = (total_list[j+1][0] - total_list[j][0]) * total_list[j][1]
        ground_sum += sum_v
    else:
        total_list[j+1][1] = total_list[j][1]
        sum_v = (total_list[j+1][0] - total_list[j][0]) * total_list[j][1]
        ground_sum += sum_v

# 제일 높이가 큰 기둥 기준 오른쪽 비교
for x in range(N-1, max_ground, -1):
    if total_list[x][1] <= total_list[x-1][1]:
        sum_v = (total_list[x][0] - total_list[x-1][0]) * total_list[x][1]
        ground_sum += sum_v
    else:
        total_list[x-1][1] = total_list[x][1]
        sum_v = (total_list[x][0] - total_list[x-1][0]) * total_list[x][1]
        ground_sum += sum_v

print(ground_sum)









