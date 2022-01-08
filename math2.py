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

import math

def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

if __name__ == "__main__":
    save = []
    for i in range(1, (2*123456)+1):
        if prime(i):
            save.append(1)
        else:
            save.append(0)
    while True:
        A = int(input())
        B = 2 * A
        if A == 0:
            break
        c = save[A:B]
        print(c.count(1))