from robot import Robot


#CREATION ROBOT (position 0,0 et regarde vers le haut)
robot1 = Robot(0,0,1)


#AVANCER
print("position avant" ,robot1.getPos())
for i in range(0,10):
    robot1.avancer()
    print("position apres" ,i,robot1.getPos())


#RECULER
print("position avant" ,robot1.getPos())
for i in range(0,10):
    robot1.reculer()
    print("position apres" ,i,robot1.getPos())
   

#TOURNER
print("direction de base: ",robot1.getDirr())
robot1.tourner("d")
print("apres tourner a doite: ",robot1.getDirr())
robot1.tourner("g")
print("apres tourner a gauche: ",robot1.getDirr())
robot1.tourner("mauvais_argument")
robot1.tourner(5)
