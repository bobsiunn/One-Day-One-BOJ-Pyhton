import sys
import copy

input = sys.stdin.readline()

def spreadvirus(vl, arr):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    spread_virus_cnt = 0
    global safe_area

    while vl:
        x,y = vl.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(if 0)