import sys
sys.stdin = open("C:/Users/Joshua/PythonWorkspace/Algorithm/\
파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/9. 봉우리/in1.txt", 'r')

# 상하좌우 좌표값 초기화
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 가장자리 0으로 초기화

a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)