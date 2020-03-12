import sys
sys.stdin = open("C:/Users/Joshua/PythonWorkspace/Algorithm/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/6. 격자판 최대합/in1.txt","r")
"""
n = int(input())
data_list = []
for _ in range(n):
    temp = list(map(int, input().split()))
    data_list.append(temp)

res_list = []

for i in data_list:
    res_list.append(sum(i))

sero_list = list(zip(*data_list))

for i in sero_list:
    res_list.append(sum(i))

x = 0
temp2 = []
temp3 = []
while x < n:
    temp2.append(data_list[x][x])
    temp3.append(data_list[n - x - 1][x])
    x += 1
res_list.append(sum(temp2))
res_list.append(sum(temp3))

print(max(res_list))

"""

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)
