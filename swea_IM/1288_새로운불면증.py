# N의 배수 번호인 양을 센다
T = int(input())
for tc in range(1, T+1):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    n = int(input())
    number = 1
    count = 0
    total_count = 0
    while count < 10:
        total_count += 1
        result = str(n * number)
        for s in result:
            if int(s) in numbers:
                s = int(s)
                numbers.remove(s)
                count += 1
                number += 1


    print(f'#{tc} {count}')

