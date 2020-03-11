import sys
sys.stdin = open("input.txt", 'r')

lst = list(range(1,21))

for i in range(10):
    start, end = map(int, input().split())
    s = start - 1
    e = end
    new_lst = lst[s:e]
    lst[s:e] = new_lst[::-1]

print(lst)