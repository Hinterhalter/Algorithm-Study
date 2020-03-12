import sys
sys.stdin = open("C:/Users/Joshua/PythonWorkspace/Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/8. 곳감/in1.txt","r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0: # 왼쪽 방향 회전
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

for x in a:
    print(x)

start = 0
end = n-1
res = 0

for i in range(n):
    for j in range(start, end+1):
        res += a[i][j]
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(res)

