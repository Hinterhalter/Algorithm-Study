import sys

sys.stdin = open("/home/pirl/Downloads/coding_test/섹션 2/8. 뒤집은 소수/in1.txt", 'r')

# 숫자를 거꾸로 만들어주는 함수
def reverse(x):
    res = 0
    while x > 0:
        t = x%10
        res = res * 10 + t
        x = x//10

    return res

# 소수인지 아닌지를 확인하는 함수
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        # 약수 확인
        if x % i == 0:
            return False
    # for 문이 return으로 끝나지 않고 정상적으로 종료된다면 else를 실행
    else:
        return True

n = int(input())
a = list(map(int,input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')