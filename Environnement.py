class Environnement:
    def __init__(self,max_x,max_y)
        self.max_x= max_x
        self.max_y=max_y


    def getPosition(self):
        return self.max_x, self.max_y


    def afficherEnv(self):
        print("Environnement de {self.max_x} longueur et de {self.max_y} largeur")
        
