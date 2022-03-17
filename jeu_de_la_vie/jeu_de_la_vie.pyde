
class block : 
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.etat = 0
        self.voisins = []
        
        
    def display(self):
        rect(self.x*self.w,self.y*self.h,self.w,self.h)
    
    def initVoisin(self,grid):
 
        if self.x != 0 :
            self.voisins.append(grid[self.y][self.x-1])
        if self.x != 0 and self.y != 0 :
            self.voisins.append(grid[self.y-1][self.x-1])
            
        if self.y != 0 :
            self.voisins.append(grid[self.y-1][self.x])
        if self.x != len(grid[0])-1 and self.y != 0 :
            self.voisins.append(grid[self.y-1][self.x+1])
            
        if self.x != len(grid[0])-1 :
            self.voisins.append(grid[self.y][self.x+1])
        if self.x != len(grid[0])-1 and self.y != len(grid)-1 :
            self.voisins.append(grid[self.y+1][self.x+1])
            
        if self.y != len(grid)-1 :
            self.voisins.append(grid[self.y+1][self.x])
        if self.x != 0 and self.y != len(grid)-1 :
            self.voisins.append(grid[self.y+1][self.x-1])
        # print("----------------------------------------------------")
        
        # for v in self.voisins:
        #     print(v.x,v.y)
        
    def update(self) : 
        
        indiceV = 0
        for v in self.voisins :
            indiceV += v.etat
        print(indiceV)
        
        if indiceV == 3 :
            return 1
        elif indiceV == 2 :
            return self.etat
        else:
            return 0 
        
        
        

grille = []
time = 0
nbw = 30
nbh = 30
vw = 20
vh = 20
sizew = nbw*vw
sizeh = nbh*vh
def setup():
    global nbw,nbh,vw,vh,sizew, sizeh
    background(255)
    global grille
    size(sizew,sizeh)
    fill(0)
    
    for fy in range(nbh):
        grille.append([])
        for fx in range(nbw):
            grille[fy].append(block(fx,fy,vw,vh))
  
    for fy in range(nbh):
        for fx in range(nbw):  
            grille[fy][fx].initVoisin(grille)
            
    
def draw():
    global nbw,nbh,vw,vh, grille, time
    background(255)
    MouseAndKey()
    fill(0)
    for i in grille :
        for j in i:
            if j.etat == 1 :
                j.display()
    time += 1
    
def MouseAndKey():
    global nbw,nbh,vw,vh, grille, time
    if mousePressed : 
        # time = 0
        # if grille[floor(mouseY/vh)][floor(mouseX/vw)].etat == 1 : 
        #     grille[floor(mouseY/vh)][floor(mouseX/vw)].etat = 0 
        # else :
            grille[floor(mouseY/vh)][floor(mouseX/vw)].etat = 1 
        
    if keyPressed :
        if key == 'r':
            for fy in range(nbh):
                for fx in range(nbw):
                    grille[fy][fx].etat = 0 
        if key == "d":
            for fy in range(nbh):
                for fx in range(nbw):
                    fill(255)
                    rect(fx*vw,fy*vh,vw,vh)
        if key == ENTER :
           # time = 0
            currentGrid = []
            for fy in range(nbh):
                currentGrid.append([])
                for fx in range(nbw):  
                    currentGrid[fy].append(grille[fy][fx].update())
                    
            for fy in range(nbh):
                for fx in range(nbw):  
                    grille[fy][fx].etat = currentGrid[fy][fx]
