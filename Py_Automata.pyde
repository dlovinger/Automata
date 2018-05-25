import copy
#enter seed type
# 1. random center symmetric seed
# 2. random cells everywhere
# 3. cells everywhere, symmetric
# 4. user-defined 1: Pulsar
# 5. user-defined 2: Pulsar
# 5. user-defined 2: Centro-symmetric
startSeed = 1

fps = 8.0
#define size, midpoint, etc
s = 8     #EVEN sxs pixel cell
height = 800
width = 800

if s%2 == 0:
    h = height
    w = width
else:
    h = height + s
    w = width + s
mid = ceil(float(w/s)/2)

if startSeed == 1:
    #generate random seed of central initial cells
    seed_cent = int(random(0,2))
    seed_face1 = int(random(0,2))
    seed_corner1 = int(random(0,2))
    seed_face2 = int(random(0,2))
    seed_corner2 = int(random(0,2))
    seed_mid2 = int(random(0,2))
    cells = [[0 for i in range(w/s)] for j in range(h/s)]
    for i in range(-2,3,4):
        if i < 0:
            a = -1
        else:
            a = 1
        cells[mid+i][mid+i] = seed_corner2
        cells[mid-i][mid+i] = seed_corner2
        cells[mid+i-a][mid+i] = seed_mid2
        cells[mid+i][mid+i-a] = seed_mid2
        cells[mid-i+a][mid+i] = seed_mid2
        cells[mid+i][mid-i+a] = seed_mid2
        cells[mid][mid+i] = seed_face2
        cells[mid+i][mid] = seed_face2
    for i in range(-1,2,2):
        cells[mid+i][mid+i] = seed_corner1
        cells[mid-i][mid+i] = seed_corner1
        cells[mid][mid+i] = seed_face1
        cells[mid+i][mid] = seed_face1
    cells[mid][mid] = seed_cent
    
if startSeed == 2:
    #random cells initially populated
    cells = [[int(random(0,2)) for i in range(w/s)] for j in range(h/s)]

if startSeed == 3:
    #for symmetric cells
    cells = [[int(random(0,2))]*(w/s) for i in range(h/s)]
    cells[mid][mid] = 1
    cells[mid][mid+1] = 1
    cells[mid+1][mid] = 1
    cells[mid+1][mid+1] = 1

if startSeed ==4:
    cells = [[0 for i in range(w/s)] for j in range(h/s)]
    cells[mid][mid] = 1
    cells[mid-1][mid] = 1
    cells[mid+1][mid] = 1
    cells[mid][mid+1] = 1
    cells[mid][mid-1] = 1
    cells[mid-3][mid+1] = 1
    cells[mid-3][mid-1] = 1
    cells[mid+3][mid+1] = 1
    cells[mid+3][mid-1] = 1


    
if startSeed ==5:
    cells = [[0 for i in range(w/s)] for j in range(h/s)]
    cells[mid][mid] = 1
    cells[mid-1][mid] = 1
    cells[mid+1][mid] = 1
    cells[mid][mid+1] = 1
    cells[mid][mid-1] = 1
    cells[mid-3][mid+1] = 1
    cells[mid-3][mid-1] = 1
    cells[mid+3][mid+1] = 1
    cells[mid+3][mid-1] = 1
    cells[mid+4][mid-1] = 1
    cells[mid-4][mid-1] = 1
    cells[mid+4][mid+1] = 1
    cells[mid-4][mid+1] = 1
    cells[mid-5][mid] = 1
    cells[mid+5][mid] = 1
    cells[mid+5][mid+1] = 1
    cells[mid+5][mid-1] = 1
    cells[mid-5][mid-1] = 1
    cells[mid-5][mid+1] = 1
    cells[mid+1][mid+3] = 1
    cells[mid-1][mid-3] = 1
    cells[mid-1][mid+3] = 1
    cells[mid+1][mid-3] = 1
    cells[mid][mid+3] = 1
    cells[mid][mid-3] = 1

if startSeed ==6:
    cells = [[0 for i in range(w/s)] for j in range(h/s)]
    cells[mid][mid] = 1
    cells[mid-1][mid] = 1
    cells[mid+1][mid] = 1
    cells[mid][mid+1] = 1
    cells[mid][mid-1] = 1
    cells[mid-3][mid+1] = 1
    cells[mid-3][mid-1] = 1
    cells[mid+3][mid+1] = 1
    cells[mid+3][mid-1] = 1

hu = [[200 for i in range(w/s)] for j in range(h/s)]

def setup():
    size(w,h);
    frameRate(fps)
    colorMode(HSB)
    rectMode(CENTER)
    
def draw():
    background(0);
    #translate(width/2, height/2);
    stroke(0);
    smooth();
    fill(255);
    strokeWeight(1);
    global cells   

    cells_nxt = [[0 for i in range(w/s)] for j in range(h/s)]
    neighbors = [[0 for i in range(w/s)] for j in range(h/s)]

    subtrct = 150#random(300,300)

    #mouse press
    if mousePressed == 1:
        cells[mouseY/s][mouseX/s] = 1
        cells[mouseY/s-1][mouseX/s] = 1
        cells[mouseY/s+1][mouseX/s] = 1
        cells[mouseY/s][mouseX/s+1] = 1
        cells[mouseY/s][mouseX/s-1] = 1
        cells[mouseY/s-3][mouseX/s] = 1
        cells[mouseY/s+3][mouseX/s] = 1
        cells[mouseY/s][mouseX/s+3] = 1
        cells[mouseY/s][mouseX/s-3] = 1
        #cells[mouseY/s-2][mouseX/s] = 1
        #cells[mouseY/s+2][mouseX/s] = 1
        cells[mouseY/s][mouseX/s+2] = 1
        cells[mouseY/s][mouseX/s-2] = 1
        cells[mouseY/s+2][mouseX/s] = 1
        cells[mouseY/s-2][mouseX/s] = 1
        cells[mouseY/s+1][mouseX/s+1] = 1
        cells[mouseY/s+1][mouseX/s-1] = 1
        cells[mouseY/s-1][mouseX/s+1] = 1
        cells[mouseY/s-1][mouseX/s-1] = 1


    
    for ri, row in enumerate(cells):          #ri is the index num, row is the value
        for ci, val in enumerate(row):
             
            #calculate next generation    
            if ri > 1 and ri < ceil(h/s-1) and ci > 1 and ci < ceil(w/s-1):    
                neighbors[ri][ci] =  Cell(ri,ci).getNeighbors(cells)
                
                #rules for birth, death, stasis
                #death - loneliness
                if val == 1 and neighbors[ri][ci] < 2:
                    cells_nxt[ri][ci] = 0
                #death - overpopulation
                elif val == 1 and neighbors[ri][ci] > 3 and neighbors[ri][ci] !=8 and neighbors[ri][ci] !=7 and neighbors[ri][ci] !=6:
                    cells_nxt[ri][ci] = 0
                #birth
                elif val == 0 and neighbors[ri][ci] == 3:
                    cells_nxt[ri][ci] = 1
                else:
                    cells_nxt[ri][ci] = cells[ri][ci]
     
                #Determine color by the number of neighbors
                if val == 1:
                    huMax = 525

                    hu[ri][ci] = map(neighbors[ri][ci],0,8,0,huMax)
                    hu[ri+1][ci] = map(Cell(ri+1,ci).getNeighbors(cells),0,8,0,huMax)
                    hu[ri-1][ci] = map(Cell(ri-1,ci).getNeighbors(cells),0,8,0,huMax)
                    hu[ri][ci+1] = map(Cell(ri,ci+1).getNeighbors(cells),0,8,0,huMax)
                    hu[ri][ci-1] = map(Cell(ri,ci-1).getNeighbors(cells),0,8,0,huMax)
                    hu[ri+1][ci+1] = map(Cell(ri+1,ci+1).getNeighbors(cells),0,8,0,huMax)
                    hu[ri+1][ci-1] = map(Cell(ri+1,ci-1).getNeighbors(cells),0,8,0,huMax)
                    hu[ri-1][ci+1] = map(Cell(ri-1,ci+1).getNeighbors(cells),0,8,0,huMax)
                    hu[ri-1][ci-1] = map(Cell(ri-1,ci-1).getNeighbors(cells),0,8,0,huMax)
                    
                    a = (hu[ri-1][ci] + hu[ri+1][ci] + hu[ri][ci+1] + hu[ri][ci-1])/3.25
                    b = hu[ri][ci]+80
                    c = (hu[ri+1][ci+1] + hu[ri+1][ci-1] + hu[ri-1][ci+1] + hu[ri-1][ci-1])/4
                
                    if a > 200 and b > 200 and c > 200:
                        a += 80
                        c -= subtrct/1.5
                        b -= subtrct/2
                        #print(a,b,c)
                    elif a > 245:
                        b -= subtrct
                        c -= subtrct
                    elif b > 245:
                        a -= subtrct
                        c -= subtrct
                    elif c > 245:
                        a -= subtrct
                        b -= subtrct
                    if c <= 20:
                        c = 15
                    if b <= 20:
                        b = 15
                    if a <= 1:
                        a = 1
                    
                    #draw the cells                
                    fill(c, b, a)
                    rect(ci*s,ri*s,s,s)                                              
                                                                                                                                                                        
    
    #make sure it doesn't get stuck in a loop
    if (
        cells[mid-2][mid-2] == cells_nxt[mid-2][mid-2] and
        cells[mid-2][mid-1] == cells_nxt[mid-2][mid-1] and
        cells[mid-2][mid+0] == cells_nxt[mid-2][mid+0] and
        cells[mid-2][mid+1] == cells_nxt[mid-2][mid+1] and
        cells[mid-2][mid+2] == cells_nxt[mid-2][mid+2] and
        
        cells[mid-1][mid-2] == cells_nxt[mid-1][mid-2] and
        cells[mid-1][mid-1] == cells_nxt[mid-1][mid-1] and
        cells[mid-1][mid-0] == cells_nxt[mid-1][mid-0] and
        cells[mid-1][mid+1] == cells_nxt[mid-1][mid+1] and
        cells[mid-1][mid+2] == cells_nxt[mid-1][mid-2] and
        
        cells[mid+0][mid-2] == cells_nxt[mid+0][mid-2] and
        cells[mid+0][mid-1] == cells_nxt[mid+0][mid-1] and
        cells[mid+0][mid+0] == cells_nxt[mid+0][mid+0] and
        cells[mid+0][mid+1] == cells_nxt[mid+0][mid+1] and
        cells[mid+0][mid+2] == cells_nxt[mid+0][mid+2] and
        
        cells[mid+1][mid-2] == cells_nxt[mid+1][mid-2] and
        cells[mid+1][mid-1] == cells_nxt[mid+1][mid-1] and
        cells[mid+1][mid-0] == cells_nxt[mid+1][mid-0] and
        cells[mid+1][mid+1] == cells_nxt[mid+1][mid+1] and
        cells[mid+1][mid+2] == cells_nxt[mid+1][mid+2] and
        
        cells[mid+2][mid-2] == cells_nxt[mid+2][mid-2] and
        cells[mid+2][mid-1] == cells_nxt[mid+2][mid-1] and
        cells[mid+2][mid-0] == cells_nxt[mid+2][mid-0] and
        cells[mid+2][mid+1] == cells_nxt[mid+2][mid+1] and
        cells[mid+2][mid+2] == cells_nxt[mid+2][mid+2] 
        ):
            rnd = int(random(0,2))
            if rnd == 0:
                cells_nxt[mid][mid] = 1
                cells_nxt[mid-1][mid] = 1
                cells_nxt[mid+1][mid] = 1
                cells_nxt[mid][mid+1] = 1
                cells_nxt[mid][mid-1] = 1
                cells_nxt[mid-2][mid] = 1
                cells_nxt[mid+2][mid] = 1
                cells_nxt[mid][mid+2] = 1
                cells_nxt[mid][mid-2] = 1
            elif rnd == 1:
                cells_nxt[mid][mid] = 1
                cells_nxt[mid-1][mid] = 1
                cells_nxt[mid+1][mid] = 1
                cells_nxt[mid][mid+1] = 1
                cells_nxt[mid][mid-1] = 1
                cells_nxt[mid-1][mid-1] = 1
                cells_nxt[mid+1][mid+1] = 1
                cells_nxt[mid-1][mid+1] = 1
                cells_nxt[mid+1][mid-1] = 1
                cells_nxt[mid-2][mid-2] = 1
                cells_nxt[mid+2][mid+2] = 1
                cells_nxt[mid-2][mid+2] = 1
                cells_nxt[mid+2][mid-2] = 1

    #copy the next generation
    cells = copy.deepcopy(cells_nxt)
    
    #randomly add to the center,
    #but only if it will there will be a net increase in cells
    #in the next generation
    rnd = int(random(0,4))
    if rnd == 0:
        neighbors_added = [[0 for i in range(-2,3)] for j in range(-2,3)]
        neighbors_no_add = [[0 for i in range(-2,3)] for j in range(-2,3)]
        added_cells_ruled = [[0 for i in range(-2,3)] for j in range(-2,3)]
        cells_ruled = [[0 for i in range(-2,3)] for j in range(-2,3)]
        
        added_cells_next = copy.deepcopy(cells)
        added_cells_next[mid][mid] = 1
        added_cells_next[mid-1][mid] = 1
        added_cells_next[mid+1][mid] = 1
        added_cells_next[mid][mid+1] = 1
        added_cells_next[mid][mid-1] = 1
        
        num_added = 0
        num_no_add = 0
        for i in range(-4,5):
            for j in range(-4,5):
                #get neighbors and apply rules to cells with added center
                neighbors_added[i][j] =  Cell(mid+i,mid+j).getNeighbors(added_cells_next)
                #print(neighbors_added[i][j])
                if added_cells_next[mid+i][mid+j] == 1 and neighbors_added[i][j] < 2:
                    added_cells_ruled[i][j] = 0
                #death - overpopulation
                elif added_cells_next[mid+i][mid+j] == 1 and neighbors_added[i][j] > 3:      #4
                    added_cells_ruled[i][j] = 0
                #birth
                elif added_cells_next[mid+i][mid+j] == 1 and neighbors_added[i][j] == 3:
                    added_cells_ruled[i][j] = 1
                else:
                    added_cells_ruled[i][j] = added_cells_next[mid+i][mid+j]
                    added_cells_ruled[i][j] = added_cells_ruled[i][j]
                num_added += added_cells_ruled[i][j]
                
       
                #get neighbors and apply rules to cells with no added
                neighbors_no_add[i][j] =  Cell(mid+i,mid+j).getNeighbors(cells)
                if cells[mid+i][mid+j] == 1 and neighbors_no_add[i][j] < 2:
                    cells_ruled[i][j] = 0
                #death - overpopulation
                elif cells[mid+i][mid+j] == 1 and neighbors_no_add[i][j] > 3:      #4
                    cells_ruled[i][j] = 0
                #birth
                elif cells[mid+i][mid+j] == 1 and neighbors_no_add[i][j] == 3:
                    cells_ruled[i][j] = 1
                else:
                    cells_ruled[i][j] = cells[mid+i][mid+j]
                    cells_ruled[i][j] = cells_ruled[i][j]
                num_no_add += cells_ruled[i][j]
            
        if num_added >= num_no_add:
            cells[mid][mid] = 1
            cells[mid-1][mid] = 1
            cells[mid+1][mid] = 1
            cells[mid][mid+1] = 1
            cells[mid][mid-1] = 1

    #saveFrame('####.png')

class Cell: 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getNeighbors(self, group):
        numNeighbors = 0
        if self.x > 1 and self.x < ceil(h/s)-1 and self.y > 1 and self.y < ceil(w/s)-1:
            for ii in range(-1,2):
                for jj in range(-1,2):
                    numNeighbors += group[self.x+ii][self.y+jj]
        numNeighbors -= group[self.x][self.y]
        return numNeighbors 
