# import sys
# A = int(input())
# B = list(map(int, sys.stdin.readline().split()))
# count = 0
# if A != len(B):
#     None
# else:
#     for i in B:
#         set = 0
#         if i == 0:
#             continue
#         for j in range(2, i+1):
#             if i % j == 0:
#                 set +=1
#         if set == 1:
#             count+=1
#     print(count)

# import math
# def prime(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     A = int(input())
#     B = int(input())
#     save = []
#     prime_save=[]
#     for i in range(A,B+1):
#         if prime(i):
#             save.append(i)
#         else:
#             save.append(-1)
#     for j in save:
#         if j != -1 and j != 1:
#             prime_save.append(j)
            
#     if len(prime_save) == 0:
#         print(-1)
#     else:
#         print(sum(prime_save))
#         print(min(prime_save))

# A = int(input())
# clu = 2

# while A != 1:
#     if A % clu == 0:
#         print(clu)
#         A/=clu
#     else:
#         clu+=1

# import sys
# import math

# def prime(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     save = []
#     A,B = map(int, sys.stdin.readline().split())
#     for i in range(A, B+1):
#         if prime(i):
#             if i == 1:
#                 pass
#             else:
#                 print(i)

# import math

# def prime(n):
#     if n == 1:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n))+1):
#             if n % i == 0:
#                 return False
#         return True

# if __name__ == "__main__":
#     save = []
#     for i in range(1, (2*123456)+1):
#         if prime(i):
#             save.append(1)
#         else:
#             save.append(0)
#     while True:
#         A = int(input())
#         B = 2 * A
#         if A == 0:
#             break
#         c = save[A:B]
#         print(c.count(1))

# import math

# def prime(n):
#     if n == 1:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n))+1):
#             if n % i == 0:
#                 return False
#         return True

# if __name__ == "__main__":
#     A = int(input())
#     for i in range(A):
#         B = int(input())
#         C, D = B//2, B//2
#         for j in range(B//2):
#             if prime(C) and prime(D):
#                 print(C,D)
#                 break
#             else:
#                 C-=1
#                 D+=1              
#참고 https://velog.io/@sharea/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-9020%EB%B2%88-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-%EB%8B%A4%EB%A5%B8-%EC%82%AC%EB%9E%8C%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%91%BC%EA%B1%B0%EC%A7%80

# import sys
# x,y,w,h = map(int, sys.stdin.readline().split())
# save = []
# save.append(x-0)
# save.append(y-0)
# save.append(w-x)
# save.append(h-y)
# print(min(save))

# import sys
# x = []
# y = []
# for i in range(3):
#     a, b = map(int, sys.stdin.readline().split())
#     x.append(a)
#     y.append(b)
# for i in range(3):
#     if x.count(x[i]) == 1:
#         four_x = x[i]
#     if y.count(y[i]) == 1:
#         four_y = y[i]
# print(four_x,four_y)

# import sys
# def pita(a,b,c):
#     if c ** 2 == (a**2) + (b**2):
#         return True
#     return False
# if __name__ == "__main__":
#     while True:
#         a = list(map(int, sys.stdin.readline().split()))
#         max_a = max(a)
#         if sum(a) == 0:
#             break
#         a.remove(max_a)
#         if pita(a[0],a[1],max_a):
#             print("right")
#         else:
#             print("wrong")

# from math import pi
# A = int(input())
# print('%.6f' %((A**2) * pi))
# print('%.6f' %((A**2) * 2))

import math
A = int(input())
for i in range(A):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dis = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
     
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2 == dis or abs(r1-r2) == dis:
            print(1)
        elif (abs(r1-r2) < dis) and (dis < r1 + r2):
            print(2)
        else:
            print(0)
            
# https://itstory1592.tistory.com/33 내외접 참고