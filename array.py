# import sys
# A = int(input())
# B = list(map(int,sys.stdin.readline().split()))
# if A != len(B):
#     None
# else:
#     small = B[0]
#     big = B[0]
#     for i in B:
#         if i < small:
#             small = i
#         elif i > big:
#             big = i
#     print(small,big)

# #단순비교로 풀면 쉽게풀었음, sort생각해서 하다보니 생각이 꼬였음
# #참고: https://dojang.io/mod/page/view.php?id=1321

save = []
for i in range(9):
    A = int(input())
    save.append(A)
save_big = save[0]
count = 0
for j in save:
    if j > save_big:
        save_big = j
print(save_big)
print(save.index(save_big)+1)
