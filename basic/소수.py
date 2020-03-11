# 에라토스테네스 체

# import sys
# sys.stdin = open("/home/pirl/Downloads/coding_test/섹션 2/7. 소수(에라토스테네스 체)/in1.txt", 'r')
n = int(input())
a = [0]*(n+1)
cnt = 0

for i in range(2, n+1):
    if a[i]==0:
        cnt += 1
    for j in range(i, n+1, i):
        a[j] = 1

print(cnt)