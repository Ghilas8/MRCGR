from robot import Robot
from environnement import Environnement

#creation monde
print("Creation du monde")
monde = Environnement(100,100)  
monde.afficherEnv()
print("\n")
#creation robots
print("Ajout du robot")
robot1 = Robot(25,-3,3)
robot2 = Robot(150,67,2)
robot3 = Robot(96,13,1)

#ajout robots
monde.add(robot1)
monde.add(robot2)
monde.add(robot3)
print("\n")

#update monde
print("Update du monde")
print("le robot se trouve en ",robot3.getPos()," et est dirigé vers ",robot3.getDirr())
for i in range(0,3):
    robot3.avancer()
    monde.update(robot3)
    
robot3.tourner('d')
monde.update(robot3)

for i in range(0,5):
    robot3.avancer()
    monde.update(robot3)