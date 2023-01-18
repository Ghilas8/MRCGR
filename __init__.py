from robot import Robot




#AVANCER

robot1 = Robot(0,0,1)
print("position avant" ,robot1.getPos())
for i in range(0,10):
    robot1.avancer()
    print("position apres" ,i,robot1.getPos())


#RECULER

print("position avant" ,robot1.getPos())
for i in range(0,10):
    robot1.reculer()
    print("position apres" ,i,robot1.getPos())
