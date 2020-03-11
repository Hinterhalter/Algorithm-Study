import sys
path = 'C:/Users\Joshua\PythonWorkspace\Algorithm\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\\5. 수들의 합\in1.txt'
path=path.replace('\\', '/')
sys.stdin = open(path,'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot<m:
        if rt<n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot==m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)