def get_nbr(maze,cur,r,c):
    nbr = []
    if cur[0] > 0 and maze[cur[0]-1][cur[1]] != "X":
        nbr.append([cur[0]-1,cur[1]])
        
    if cur[1] < (c-1) and maze[cur[0]][cur[1]+1] !="X":
        nbr.append([cur[0],cur[1]+1])
        
    if cur[0] < (r-1) and maze[cur[0]+1][cur[1]] !="X":
        nbr.append([cur[0]+1,cur[1]])
    
    if cur[1] >0  and maze[cur[0]][cur[1]-1] !="X":
        nbr.append([cur[0],cur[1]-1])
    
    return nbr


def bfs(maze,s,r,c):
    queue = []
    
    queue.append(s)
    
    maze[s[0]][s[1]] == "X"

    
    while queue:
        v = queue.pop(0)
        
        for i in get_nbr(maze,v,r,c):
            if maze[i[0]][i[1]] == "*":
                return True
            
            queue.append(i)
            maze[i[0]][i[1]] = "X"
    
    return False
            
        
t = int(input())


for _ in range(t):
    r,c = map(int,input().split())
    maze = []
    source = []
    for i in range(r):
        row = list(input())
        if "M" in row:
            source.append(i)
            source.append(row.index("M"))
        maze.append(row)
        
    if bfs(maze,source,r,c):
        print("yes")
    else:
        print("no")


