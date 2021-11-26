# import sys
# A, B, C = map(int, sys.stdin.readline().split())
# if C>B: print(A//(C-B)+1)
# else: print(-1)

# #런타임 에러 B==C 0일 때 발생하므로 C를 기준으로 잡아야함
# #A고정, B,C가변이므로 가변끼리 계산하여 고정을 빼면 갯수가 나옴 갯수이므로 +1

# A = int(input())
# B,C = 2,7
# count = 1
# while True:
#     if A == 1:
#         print(1)
#         break
#     elif B <= A <= C:
#         print(count+1)
#         break
#     else:
#         B += 6*(count)
#         C += 6*(count+1)
#         count+=1 

# A = int(input())
# line = 1
# while A > line:
#     A -= line
#     line += 1
# if line % 2 == 0:
#     up = A
#     down = line - A + 1
# else:
#     up = line - A + 1
#     down = A  
# print("{0}/{1}".format(up,down))
# #이해가 잘 안댐, 나중에 한번더 볼 필요가 있다.

# import sys
# A,B,V = map(int, sys.stdin.readline().split())
# clu = (V - B) / (A - B)
# if clu == int(clu):
#     print(int(clu))
# else:
#     print(int(clu)+1)  

# import sys
# A = int(input())
# for i in range(A):
#     H,W,C = map(int, sys.stdin.readline().split())
#     if H * W < C: None
#     else:
#         floor = C % H
#         ho = C / H
#         if ho == int(ho):
#             if floor == 0:
#                 print((H * 100) + int(ho))
#             else:
#                 print((floor * 100) + int(ho))
#         else:
#             print((floor*100) + (int(ho)+1))

# A = int(input())
# for i in range(A):
#     B = int(input())
#     C = int(input())
#     save = list(range(1,C+1))
#     for j in range(B):
#         for z in range(1,C):
#             save[z] += save[z-1]
#     print(save[-1])
    
# #https://ooyoung.tistory.com/89

# A = int(input())
# bag = 0
# while A >=0:
#     if A % 5 == 0:
#         bag += (A // 5)
#         print(bag)
#         break
#     A -=3
#     bag+=1
# else:
#     print(-1)

import sys
B,C = map(int, sys.stdin.readline().split())
print(B+C)