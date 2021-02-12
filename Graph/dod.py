import sys
input = sys.stdin.readline

dx = [-1,1,-1,-1,1,1,0,0]
dy = [0,0,1,-1,1,-1,1,-1]

def dfs(matrix, y, x, y_len, x_len):

    visit[y][x] = 1
    print(visit)

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if(0 <= ny < y_len and 0 <= nx < x_len):
            print(f'y: {y} x: {x}')
            print(f'ny: {ny} nx: {nx}')
            if(visit[ny][nx] == 0 and matrix[ny][nx] == 1):
                dfs(matrix, ny, nx, y_len, x_len)


while True:
    w,h = map(int, input().split())

    if(w == 0 and h == 0):
        break
    else:
        graph = [list(map(int, input().split())) for _ in range(h)]
        visit = [[0]*w for _ in range(h)]

        cnt = 0

        for i in range(h):
            for j in range(w):

                if(visit[i][j] == 0 and graph[i][j] == 1):
                    dfs(graph, i, j, h, w)
                    cnt += 1
                    #print(visit)
        print(cnt)
