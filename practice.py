# number = input()
# if int(number) <= 0 or int(number) >= 10:
#     None
# else:
#     for i in range(1,10):
#         a = i * int(number)
#         print(number,"*",i,"=",a)

# A = input()
# B_save = []
# C_save = []
# for i in range(int(A)):
#     B , C = input().split()
#     B_save.append(int(B))
#     C_save.append(int(C))
# for j in range(int(A)):
#     sum = B_save[j] + C_save[j]
#     print(sum)

# A = input()
# A_Save = []
# if int(A) >=1 or int(A) <= 10000:
#     for i in range(1,int(A)+1):
#         A_Save.append(i)
#     print(sum(A_Save))
# else:
#     None

# import sys
# A = input()
# for i in range(int(A)):
#     b,c = map(int,sys.stdin.readline().split())
#     print(b+c)
# #참조: https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
# #참조: https://velog.io/@pyh8618/Python-map-%ED%95%A8%EC%88%98-%EC%82%AC%EC%9A%A9%EB%B2%95

# A = int(input())
# for i in range(A):
#     print(A)
#     A = A-1

# import sys
# A = int(input())
# B_save = []
# C_save = []
# for i in range(A):
#     b,c = map(int, sys.stdin.readline().split())
#     if A <= 0 or b >= 10:
#         break
#     else:
#         B_save.append(b)
#         C_save.append(c)
# for j in range(A):
#     print("Case #",j+1,": ",B_save[j]+C_save[j],sep='')
# #출력문 공백 때문에 틀림 (sep =) -> 구분 함수 

# import sys
# A = int(input())
# B_save = []
# C_save = []
# for i in range(A):
#     b,c = map(int, sys.stdin.readline().split())
#     if A <= 0 or b >= 10:
#         break
#     else:
#         B_save.append(b)
#         C_save.append(c)
# for j in range(A):
#     print("Case #",j+1,": ", B_save[j]," + ",C_save[j]," = ",B_save[j]+C_save[j],sep='')

# import sys
# A = int(input())
# for i in range(1,A+1):
#     print(" " * (A-i), "*" * i,sep="")
# #print문 제출핼때 여러개의 식을 쓸 때 구분문자가 들어가면 공백이 생기므로 함수를 써서 없애줘야한다.

import sys
A, B = map(int, sys.stdin.readline().split())
c = list(map(int,sys.stdin.readline().split()))
if len(c) > A:
    None
else:
    for i in c:
        if i < B:
            print(i, end=' ')

# end for문 안에서 한줄 출력해줌.