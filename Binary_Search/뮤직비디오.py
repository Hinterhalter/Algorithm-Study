import sys
# sys.stdin = open('input.txt','r')
#
# n,m = map(int,inpt().split())
# Music = list(map(int, input().split()))


def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum+=x
    return cnt

n = 9
m = 9
Music = [1,2,3,4,5,6,7,8,9]
maxx = max(Music)


lt = 1
rt = sum(Music)
res = 0

while lt <= rt:
    mid = (lt + rt)//2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)
