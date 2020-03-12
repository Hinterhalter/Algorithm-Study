import sys
sys.stdin = open("C:/Users/Joshua/PythonWorkspace/Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/7. 사과나무/in1.txt","r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0

start = end = n//2

for i in range(n):
    for j in range(start, end + 1):
        res += a[i][j]
    if i < n//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
print(res)