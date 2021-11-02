# import sys
# def solve(a):
#     return(sum(a))

# if __name__ == "__main__":
#     n = list(map(int, sys.stdin.readline().split()))
#     print(solve(n))

def self_num_count():
    sum_save =[]
    num = []
    for i in range(10000):
        thu_num = i // 1000
        hun_num = (i % 1000) // 100
        ten_num = (i % 100) // 10
        one_num = i % 10
        num.append(i)
        sum = i + thu_num + hun_num + ten_num + one_num
        if sum < 10000:
            sum_save.append(sum)
    sum_save.sort()
    for j in range(10000):
        if j in sum_save:
            None
        else:
            print(j)

if __name__ == "__main__":
    self_num_count()
  
    
