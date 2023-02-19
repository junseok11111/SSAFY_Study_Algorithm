import sys;sys.stdin=open('input.txt', 'r')

# 카운트 버전
lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(int(input())):
    test_case, N = input().split()

    A = input().split()
    c = [0] * 10

    # 빈도수 계산
    for val in A:
        for i in range(10):
            if val == lst[i]:
                c[i] += 1

    print(test_case)
    for i in range(10):
        print(*[lst[i]]*c[i], end=' ')  # 리스트의 각 요소에 대해, 빈도수를 곱해서 출력
    print()

# 딕셔너리 버전
# for _ in range(int(input())):
#     test_case, N = input().split()
# 
#     A = input().split()
# 
#     dic = {}
#     for val in A:
#         dic[val] = dic.get(val, 0) + 1
# 
#     print(test_case)
#     for i in lst:
#         print(*[i] * dic[i], end=' ')
#     print()
