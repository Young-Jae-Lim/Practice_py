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

# save = []
# for i in range(9):
#     A = int(input())
#     save.append(A)
# save_big = save[0]
# count = 0
# for j in save:
#     if j > save_big:
#         save_big = j
# print(save_big)
# print(save.index(save_big)+1)

# A = int(input())
# B = int(input())
# C = int(input())
# save = A * B * C
# save_arr = []
# for i in str(save):
#     save_arr.append(i)
# for z in range(10):
#     print(save_arr.count(str(z)))
# save_count = []
# zero = one = two = three = four = five = six = seven = eight = nine = 0
# save_arr = list(map(int, save_arr))
# for j in save_arr:
#     if j == 0:
#         zero +=1
#     elif j == 1:
#         one +=1
#     elif j == 2:
#         two +=1
#     elif j == 3:
#         three +=1
#     elif j == 4:
#         four +=1
#     elif j == 5:
#         five +=1
#     elif j == 6:
#         six +=1
#     elif j == 7:
#         seven +=1 
#     elif j == 8:
#         eight +=1
#     elif j == 9:
#         nine +=1
# save_count.append(zero)
# save_count.append(one)
# save_count.append(two)
# save_count.append(three)
# save_count.append(four)
# save_count.append(five)
# save_count.append(six)
# save_count.append(seven)
# save_count.append(eight)
# save_count.append(nine)
# for k in save_count:
#     print(k)

#너무 노가다 한거같음, 수정해야할듯.. 정수형 노가다(swith case문 생각해서 함)
#중간부분 수정함 한결 간결해짐.       

# import sys
# A_save = []
# B_save = []
# for i in range(10):
#     A = int(input())
#     A_save.append(A)
# for j in A_save:
#     B_save.append(j % 42)
# B_save.sort()
# count = 1
# for z in range(9):
#     if B_save[z] != B_save[z+1]:
#         count+=1
# print(count)

#리스트 범위 생각 잘하자 전체 탐색할 경우 try except도 사용 가능

# import sys
# A = int(input())
# B = list(map(int, sys.stdin.readline().split()))
# save = []
# if len(B) > A:
#     None
# else:
#     big = B[0]
#     for i in B:
#         if i > big:
#             big = i
#     for j in range(A):
#             save.append(((B[j] / big) * 100))
#     print(sum(save)/A)

import sys
A = int(input())
save = []
count = 0
for i in range(A):
    B = list(map(str, sys.stdin.readline()))
    for j in B:
        if j == 'O':
            count +=1
            save.append(count)
        else:
            count = 0
            save.append(count)
    print(sum(save))
    save.clear()

