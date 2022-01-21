import sys
save = []
def dfs():
    if len(save) == B:
        print(' '.join(map(str,save)))
        return
    for i in range(1, A+1):
        if i not in save:
            save.append(i)
            dfs()
            save.pop()
if __name__ == "__main__":
    A, B = list(map(int,sys.stdin.readline().split()))
    dfs()
    
#참고: https://jiwon-coding.tistory.com/21
#재귀, 수열 이해가 좀 더 필요할듯 