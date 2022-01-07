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

import math
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    save = []
    prime_save=[]
    for i in range(A,B+1):
        if prime(i):
            save.append(i)
        else:
            save.append(-1)
    for j in save:
        if j != -1 and j != 1:
            prime_save.append(j)
            
    if len(prime_save) == 0:
        print(-1)
    else:
        print(sum(prime_save))
        print(min(prime_save))