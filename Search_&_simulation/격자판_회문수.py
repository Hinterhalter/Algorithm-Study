import sys
sys.stdin = open("C:/Users/Joshua/PythonWorkspace/Algorithm/\
파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/11. 격자판 회문수/in1.txt",'r')

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
            else:
                cnt += 1

print(cnt)