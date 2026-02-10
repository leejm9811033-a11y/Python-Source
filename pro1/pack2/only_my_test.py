import sys
sys.stdin = open("1_sample_input.txt", "r")
rd = sys.stdin.buffer.readline

T = int(rd().strip())

# T = 1

for tc in range(1, T + 1):

    H, W = map(int, rd().split())

    board = list(list(map(str, rd().split())) for _ in range(H))

    print(board)
    print()