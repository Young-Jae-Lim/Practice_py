# import sys

# A,B = map(int, sys.stdin.readline().split())
# C = list(map(int, sys.stdin.readline().split()))
# save = []
# for i in C:
#     for j in C:
#         if i == j:
#             continue
#         for z in C:
#             if i == z or j == z:
#                 continue
#             clu = i + j + z
#             if clu <= B:
#                 save.append(clu)
# print(max(save))

# import sys

# A = int(sys.stdin.readline())
# result = 0
# for i in range(1, A+1):
#     B = list(map(int, str(i)))
#     result = i + sum(B)
#     if result == A:
#         print(i)
#         break
#     if i == A:
#         print(0)

# #하다가 꼬인듯.. 참고: https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-2231%EB%B2%88-%EB%B6%84%ED%95%B4%ED%95%A9-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

import sys
A = int(sys.stdin.readline())
save = []
ans_save = []
for i in range(A):
    B,C = map(int,sys.stdin.readline().split())
    save.append([B,C])
    
for i in save:
    count = 0
    for j in save:
        if i == j:
            pass
        else:
            if j[0] > i[0] and j[1] > i[1]:
                count+=1
    ans_save.append(count+1)
    
print(' '.join(str(i) for i in ans_save))