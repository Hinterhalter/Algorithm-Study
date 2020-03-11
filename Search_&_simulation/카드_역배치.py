import sys
sys.stdin = open("input.txt", 'r')

# lst = list(range(1,21))
#
# for i in range(10):
#     start, end = map(int, input().split())
#     s = start - 1
#     e = end
#     new_lst = lst[s:e]
#     lst[s:e] = new_lst[::-1]
#
# print(lst)

a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(a, end=' ')