# import sys
# save = []
# def dfs():
#     if len(save) == B:
#         print(' '.join(map(str,save)))
#         return
#     for i in range(1, A+1):
#         if i not in save:
#             save.append(i)
#             dfs()
#             save.pop()
# if __name__ == "__main__":
#     A, B = list(map(int,sys.stdin.readline().split()))
#     dfs()
    
#참고: https://jiwon-coding.tistory.com/21
#재귀, 수열 이해가 좀 더 필요할듯 

# import sys
# save = []
# def dfs(start):
#     if len(save) == B:
#         print(' '.join(map(str,save)))
#         return
#     for i in range(start, A+1):
#         if i not in save:
#             save.append(i)
#             dfs(i+1)
#             save.pop()
# if __name__ == "__main__":
#     A, B = list(map(int,sys.stdin.readline().split()))
#     dfs(1)
    
# import sys
# save = []
# def dfs():
#     if len(save) == B:
#         print(' '.join(map(str,save)))
#         return
#     for i in range(1, A+1):
#         save.append(i)
#         dfs()
#         save.pop()
# if __name__ == "__main__":
#     A, B = list(map(int,sys.stdin.readline().split()))
#     dfs()
    
# import sys
# save = []
# def dfs(start):
#     if len(save) == B:
#         print(' '.join(map(str,save)))
#         return
#     for i in range(start, A+1):
#         save.append(i)
#         dfs(i)
#         save.pop()
# if __name__ == "__main__":
#     A, B = list(map(int,sys.stdin.readline().split()))
#     dfs(1)    

# import sys
# def check(n):
#     for i in range(n):
#         if chess[n] == chess[i] or abs(chess[n]-chess[i]) == n-i:
#             return False
#     return True

# def dfs(n):
#     global count
#     if n == A:
#         count +=1
#     else:
#         for i in range(A):
#             chess[n] = i
#             if check(n):
#                 dfs(n+1)
                
# A = int(sys.stdin.readline())
# chess = [0] * A
# count = 0
# dfs(0)
# print(count)
# #참고: https://sso-feeling.tistory.com/415?category=913126 조금더 이해가 필요할듯
# #한번 더 풀어볼 필요가 있음

import sys
A = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
B = [(i, j) for i in range(9) for j in range(9) if A[i][j]==0 ]

def square(x,y):
    number = [i for i in range(1, 10)]
    for j in range(9):
        if A[x][j] in number:
            number.remove(A[x][j])
        if A[j][y] in number:
            number.remove(A[j][y])
        
    x = x//3
    y = y//3
    for k in range(x*3,(x+1)*3):
        for z in range(y*3, (y+1)*3):
            if A[k][z] in number:
                number.remove(A[k][z])
    return number

flag = False

def dfs(count):
    global flag
    if flag:
        return
    
    if count == len(B):
        for i in A:
            print(' '.join(map(str, i)))
        flag = True
        return
    
    (i,j) = B[count]
    clu = square(i,j)
    for num in clu:
        A[i][j] = num
        dfs(count+1)
        A[i][j] = 0
        
dfs(0)

#참고: https://zidarn87.tistory.com/344
#골드문제 다시 풀기 