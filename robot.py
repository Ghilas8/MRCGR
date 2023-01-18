class Robot:
	def __init__(self,posx, posy, dirr)
		self.posx = posx                                    #position du robot sur l'axe des abscisse 
		self.posy = posy                                    #position du robot sur l'axe des abscisse 
		self.dir  = dirr                                    #direction du robot (1 pour haut, 2 pour droite, 3 pour bas, 4 pour gauche)
	
	def getPos(self):                                       #retourne la position
		return self.posx, self.posy
		
	def getDir(self):                                       #retourne la direction
		return self.dirr
		
	def avancer(self):                                      #avance le robot de 1 (en fonction de sa direction)
	
	def reculer(self):                                      #avance le robot de 1 (en fonction de sa direction)
	
	def tourner(self, direction):                           #tourne le robot selon une direction ("g" pour gauche, "d" pour droite)
	
	def collision(self, tabPoints):                         #verifie si le robot fait une collision avec un objet grace à un tableau de points
	                                                        #regarde si position du robot et dans le tableau de points
		
	
