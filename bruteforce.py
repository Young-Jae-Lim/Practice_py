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

import sys

A = int(sys.stdin.readline())
result = 0
for i in range(1, A+1):
    B = list(map(int, str(i)))
    result = i + sum(B)
    if result == A:
        print(i)
        break
    if i == A:
        print(0)
            