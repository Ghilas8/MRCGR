class Environnement:
    def __init__(self,max_x,max_y):
        self.max_x= max_x 
        self.max_y=max_y  


    def getPos(self):
        return (self.max_x, self.max_y)


    def afficherEnv(self):
        rx , ry = self.getPos()
        print("Environnement de", rx," longueur et de ", ry," largeur")
    
    def add(self,robot):
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)): #comparaison de la position du robot avec les limites du mondes
            print("Erreur : Les positions du robots sont en dehors du monde. Il n'a pas pu etre place")
            return
            
            
        print("Le robot a été placé dans le monde en ",robot.getPos()," et est dirigé vers ",robot.getDirr())
        
    def update(self,robot):
        rx , ry = robot.getPos()
        if((rx < 0) or (rx > self.max_x) or (ry < 0) or (ry > self.max_y)):
            print("Erreur : Le robot se trouve en dehors du monde")
            return
        print("Le robot se trouve désormais en ",robot.getPos()," et est dirigé vers ",robot.getDirr())
        
        
