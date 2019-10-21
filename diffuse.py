from random import choice
npart=500
side=51
density = choice((0,1))
maxsteps = 10000
perc = 0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
for ipart in range(npart):
    x,y = side//2,side//2
    for x in range(side):
        x = density
        for y in range(side):
            y = density
    for isteps in range(maxsteps):
        grid[x][y]=0
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x ==1 or y ==1:
            continue
        if x<0 or y<0 or x==side or y==side:
            perc+= 1
            break
        grid[x][y]=1
print("Probability of the particle percolatin out of the system =%5.2f"%(perc/npart))
