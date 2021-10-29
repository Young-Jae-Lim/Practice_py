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

A = int(input())
B = int(input())
C = int(input())

save = A * B * C
zero = one = two = three = four = five = six = seven = eight = nine = 0
save_arr = []
save_count = []
for i in str(save):
    save_arr.append(i)
save_arr = list(map(int, save_arr))
for j in save_arr:
    if j == 0:
        zero +=1
    elif j == 1:
        one +=1
    elif j == 2:
        two +=1
    elif j == 3:
        three +=1
    elif j == 4:
        four +=1
    elif j == 5:
        five +=1
    elif j == 6:
        six +=1
    elif j == 7:
        seven +=1 
    elif j == 8:
        eight +=1
    elif j == 9:
        nine +=1
save_count.append(zero)
save_count.append(one)
save_count.append(two)
save_count.append(three)
save_count.append(four)
save_count.append(five)
save_count.append(six)
save_count.append(seven)
save_count.append(eight)
save_count.append(nine)
for k in save_count:
    print(k)

#너무 노가다 한거같음, 수정해야할듯..
       