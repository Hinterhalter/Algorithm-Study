import sys

sys.stdin = open("/home/pirl/Downloads/coding_test/섹션 2/6. 자릿수의 합/in1.txt",'r')

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x%10
        x = x//10
    return sum

def digit_sum1(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max=-2147000000

for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)