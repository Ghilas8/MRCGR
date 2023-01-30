from tkinter import *
from robot import Robot
from obstacle import Obstacle
from environnement import Environnement
import time
import random


Largeur =400
Hauteur= 200

root=Tk()
canvas = Canvas(root,width=Largeur,height=Largeur,background ="white")
canvas.pack(fill="both",expand=True)


x= random.uniform(0.0,400.0)
y= random.uniform(0.0,200.0)
print(x,y)

robot1 = Robot(0,0,15)
rbt = canvas.create_oval(robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20,width=2,fill="red") 


def action_depl():	
	dx=random.uniform(0.0,10.0)
	dy=random.uniform(0.0,10.0)
	vecteur= (dx,dy)
	robot1.deplacement(vecteur)
	canvas.coords(rbt,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)	
	canvas.after(75,action_depl)
	return

def action_rot():
	robot1.rotation(random.uniform(0.0,360.0))
	canvas.coords(rbt,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)	
	canvas.after(50,action_rot)
	return


def act():
	while(True):
		action_rot()
		action_depl()
		return
	
	
bouton_couleur = Button(root,text="Deplacement",width=20, command=action_depl)
bouton_couleur.pack(pady=10)

bouton_3 = Button(root,text="rotation",width=20, command=act)
bouton_3.pack(side=BOTTOM, pady=10)


bouton_4 = Button(root,text="quitte",width=20, command=root.quit)
bouton_4.pack(side=BOTTOM, pady=10)


root.mainloop()

