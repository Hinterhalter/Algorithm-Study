import sys

sys.stdin = open('/home/pirl/Downloads/coding_test/섹션 2/10. 점수 계산/in2.txt','r')

n = int(input())
data_list = list(map(int, input().split()))
# score_list = [0] * n
#
# for i in range(n):
#     if data_list[i] == 1:
#         score_list[i] = 1
#         if data_list[i-1] == data_list[i]:
#             score_list[i] = score_list[i-1] + 1
# print(sum(score_list))

sum = 0
cnt = 0

for x in data_list:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt=0
print(sum)