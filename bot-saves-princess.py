#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    if grid[0][0] == 'p':
        for i in range((n-1)/2):
            print("LEFT")
        for i in range((n-1)/2):
            print("UP")
    if grid[0][n-1] == 'p':
        for i in range((n-1)/2):
            print("RIGHT")
        for i in range((n-1)/2):
            print("UP")
    if grid[n-1][0] == 'p':
        for i in range((n-1)/2):
            print("LEFT")
        for i in range((n-1)/2):
            print("DOWN")
    if grid[n-1][n-1] == 'p':
        for i in range((n-1)/2):
            print("RIGHT")
        for i in range((n-1)/2:
            print("DOWN")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
