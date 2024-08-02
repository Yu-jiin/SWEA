import sys
a = ''
b = 'a'
c = 'ab'
d = 'abc'

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))

# s1 = list(input())
# s2 = input()
#
# print(s1)   # ['a', 'b', 'c']
# print(s2)   # abc

s1 = list(input())
s2 = input()
# 리스트에 저장 안해도 인덱스로 접근이 가능함
print(s1[0])    # a
print(s2[0])    # a
s1[0] = 'A'     # list로 저장하면 가능
s2 = 'Abc'
print(s1[0])    # A
print(s2[0])    # a
# s2[0] = 'A'     # TypeError: 'str' object does not support item assignment


# def strlen(a):
#     i = 0
#     count = 0
#     while a[i] != '\0':
#        count += 1

# 문자열 뒤집기
# for i in range(N // 2):
#     arr[i],arr[N-1,-i] = arr[N-1,-i],arr[i]


s1 = 'abc'
s2 = 'abc'
print(s1 == s2)     # True
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)     # True

s3 = s1[:2] + 'c'
print(s3)       # abc
print(s2 == s3)     # True
print(s2 is s3)     # False  is 는 내용물이 같은 참조값인가를 확인
print(s1 is s2)     # True      slicing으로 만들면 내용은 같은데 다른 참조값


ss1 = 'A'
print(ord('A'))     # 아스키 코드 값 65
print(chr(65))      # A

# a = 123
# a % 10 = 3
# a // 10 = 2
