# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break
# #https://conak-diary.tistory.com/7


A = int(input())
count = 1
if A < 10:
    Ten_save = 0
else:
    Ten_save = A//10
one_save = A%10
cal_save = Ten_save + one_save
save = ((one_save * 10) + (cal_save %10))

while A != save:
    save_ten = save // 10
    save_one = save % 10
    save_cal = save_ten + save_one
    save = ((save_one * 10) + (save_cal % 10))
    count +=1
print(count)

#백준 while 