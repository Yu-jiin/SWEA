# T = 10  # 테스트 케이스 개수
#
# for test_case in range(1, T + 1):
#     tc = int(input())  # 테스트 케이스 번호
#     N = 100  # 배열의 크기 (100x100)
#     arr = [input().strip() for _ in range(N)]  # 100x100 배열 입력 받기
#
#     max_length = 1  # 가장 긴 회문의 길이
#     max_palindrome = ""  # 가장 긴 회문
#
#     # 행에서 회문 찾기
#     for i in range(N):
#         for j in range(N):
#             for k in range(j, N):
#                 # 부분 문자열 추출
#                 substring = ""
#                 for l in range(j, k + 1):
#                     substring += arr[i][l]
#
#                 # 회문 확인
#                 left = 0
#                 right = len(substring) - 1
#                 is_palindrome = True
#                 while left < right:
#                     if substring[left] != substring[right]:
#                         is_palindrome = False
#                         break
#                     left += 1
#                     right -= 1
#
#                 # 가장 긴 회문 업데이트
#                 if is_palindrome and len(substring) > max_length:
#                     max_length = len(substring)
#                     max_palindrome = substring
#
#     # 열에서 회문 찾기
#     for j in range(N):
#         for i in range(N):
#             for k in range(i, N):
#                 # 부분 문자열 추출
#                 substring = ""
#                 for l in range(i, k + 1):
#                     substring += arr[l][j]
#
#                 # 회문 확인
#                 left = 0
#                 right = len(substring) - 1
#                 is_palindrome = True
#                 while left < right:
#                     if substring[left] != substring[right]:
#                         is_palindrome = False
#                         break
#                     left += 1
#                     right -= 1
#
#                 # 가장 긴 회문 업데이트
#                 if is_palindrome and len(substring) > max_length:
#                     max_length = len(substring)
#                     max_palindrome = substring
#
#     # 결과 출력
#     print(f"#{test_case} {max_palindrome}")


T = 10  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    tc = int(input())  # 테스트 케이스 번호
    N = 100  # 배열의 크기 (100x100)
    arr = [input().strip() for _ in range(N)]  # 100x100 배열 입력 받기
    max_length = 1  # 가장 긴 회문의 길이

    # 행에서 회문 찾기
    for i in range(N):
        for length in range(N, 0, -1):  # 길이를 길게부터 짧게
            for start in range(N - length + 1):
                substring = arr[i][start:start + length]
                if substring == substring[::-1]:  # 회문인지 확인
                    if length > max_length:
                        max_length = length
                    break  # 현재 길이에서 더 긴 회문은 없으므로 종료

    # 열에서 회문 찾기
    for j in range(N):
        for length in range(N, 0, -1):  # 길이를 길게부터 짧게
            for start in range(N - length + 1):
                substring = ''.join([arr[start + k][j] for k in range(length)])
                if substring == substring[::-1]:  # 회문인지 확인
                    if length > max_length:
                        max_length = length
                    break  # 현재 길이에서 더 긴 회문은 없으므로 종료

    # 결과 출력
    print(f"#{test_case} {max_length}")