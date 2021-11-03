# import sys
# def solve(a):
#     return(sum(a))

# if __name__ == "__main__":
#     n = list(map(int, sys.stdin.readline().split()))
#     print(solve(n))

# def self_num_count():
#     sum_save =[]
#     num = []
#     for i in range(10000):
#         thu_num = i // 1000
#         hun_num = (i % 1000) // 100
#         ten_num = (i % 100) // 10
#         one_num = i % 10
#         num.append(i)
#         sum = i + thu_num + hun_num + ten_num + one_num
#         if sum < 10000:
#             sum_save.append(sum)
#     sum_save.sort()
#     for j in range(10000):
#         if j in sum_save:
#             None
#         else:
#             print(j)

# if __name__ == "__main__":
#     self_num_count()
  

def han_num(A):
    count = 0
    if A > 1000: None
    else:
        for i in range(1,A+1):
            if i < 100:
                count +=1
            else:
                hun_num = i // 100
                ten_num = (i % 100) // 10
                one_num = i % 10

                if (ten_num - hun_num) == (one_num - ten_num):
                    count +=1
                else:
                    None
        print(count)

if __name__ == "__main__":
    A = int(input())
    han_num(A)

#참조 : https://evga7.tistory.com/44 등차수열은 1~10자리는 차와 상관없이 등차수열.
