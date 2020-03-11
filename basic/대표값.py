import sys
sys.stdin = open('/home/pirl/Downloads/coding_test/섹션 2/4. 대표값/in1.txt', 'r')

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp==min:
        if x > score:
            score=x
            res = idx+1
print(ave, res)
