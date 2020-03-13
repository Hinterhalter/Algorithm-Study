# 결정 알고리즘의 경우에는 특징이 있는데 답이 몇부터 몇까지 사이에 있다는 말이 있으면
# 이분 탐색을 통한 결정 알고리즘 문제라고 유추할 수 있다.

import sys
sys.stdin = open("C:/Users/Joshua/PythonWorkspace/Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)\
/섹션 4/2. 랜선자르기/in1.txt","r")

def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

k,n = map(int, input().split())

Line = []
res = 0
largest = 0

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)

