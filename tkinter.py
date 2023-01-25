from tkinter import *
from robot import Robot
from obstacle import Obstacle
from environnement import Environnement



Largeur =400
Hauteur= 200

root=Tk()
canvas = Canvas(root,width=Largeur,height=Largeur,background ="white")
canvas.pack(fill="both",expand=True)


robot1 = Robot(0,0,1)
rect = canvas.create_rectangle(robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20,width=2,fill="red") 


def action_depl():	
	canvas.coords(rect,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)	
	robot1.avancer()
	canvas.after(50,robot1.avancer())
	return
def action_tournadroite():
	canvas.coords(rect,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)	
	robot1.tourner("d")
	canvas.after(50,robot1.tourner())
	return
def action_tournagauche():
	canvas.coords(rect,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)	
	robot1.tourner("g")
	canvas.after(50,robot1.tourner())
	return


def testact():
	bouton_couleur.invoke()
		
	return	
	
	
bouton_couleur = Button(root,text="Deplacement",width=20, command=action_depl)
bouton_couleur.pack(pady=10)

bouton_1 = Button(root,text="Deplacement x10",width=20, command=testact)
bouton_1.pack(pady=10)

bouton_2 = Button(root,text="tourne a droite",width=20, command=action_tournadroite)
bouton_2.pack(pady=10)

bouton_3 = Button(root,text="tourne a gauche",width=20, command=action_tournagauche)
bouton_3.pack(pady=10)

bouton_4 = Button(root,text="quitte",width=20, command=root.quit)
bouton_4.pack(side=BOTTOM, pady=10)


root.mainloop()

