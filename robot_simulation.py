# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:47:27 2019

@author: suilven
"""
#This Program is a better version of Robot_Image

#Sim props:Height Width Speed Radius
#Robot
#see robot_image.py

#This program will eventually:
#1.Make image of robot
#2.Drive with 2 wheels
#3.Make accurate simulation of echolocation
#4.Have AI inputed into it
#5.Teach AI how to use echolocation so our
#robot can use echolocation to manouvere
#around our house. 

from tkinter import *




def move_robot(event):
    robpos=robprops["robotpos"]
    robot_id=robprops["robot_id"]
    ROBOT_SPD=robprops["robot_spd"]
    if event.keysym == 's':
        c.move(robot_id, 0, ROBOT_SPD)
        robpos[0]=robpos[0]+ROBOT_SPD
        
#        c.move(robot_id2, 0, ROBOT_SPD)   
    elif event.keysym == 'w':
        c.move(robot_id, 0, -ROBOT_SPD)
        robpos[0]=robpos[0]-ROBOT_SPD

#        c.move(robot_id2, 0, ROBOT_SPD)    
    elif event.keysym == 'a':
       c.move(robot_id, -ROBOT_SPD, 0)
       robpos[1]=robpos[1]-ROBOT_SPD

#       c.move(robot_id2, 0, ROBOT_SPD)    
    elif event.keysym == 'd':
       c.move(robot_id, ROBOT_SPD,0)
       robpos[1]=robpos[1]+ROBOT_SPD

    #fire a bullet
    elif event.keysym == 'f':
        firebullet(robprops)
#       c.move(robot_id2, 0, ROBOT_SPD)    
    #move the robot
    
def initialisewindow():
    HEIGHT=500
    WIDTH=800
    TITLE='Robot Simulation'    
    window=Tk()
    window.title(TITLE)
    c = Canvas(window, height=HEIGHT, width=WIDTH)
    c.pack()    
    windowprops={"height":HEIGHT,"width":WIDTH,"window":window,"canvas":c}    
    #this is a list 
    return windowprops

def initialissim():
    simprops={}
    #this is a list    
    return simprops


def initialiserobot(c):
    ROBOT_SPD = 10
    X=50
    Y=50
    
    robpos={}
    robpos[0]=X
    robpos[1]=Y
    
    robot_id = c.create_polygon(180, 75, 220, 75, 200, 20, fill='red')
    robprops={"robotpos":robpos,"robot_id":robot_id,"robot_spd":ROBOT_SPD}
    return robprops
  
def initialisebullet(c, robprops):
    BULLET_SPD = 15
    r=1
    robpos=robprops["robotpos"]
    bullet_id=c.create_oval(robpos[0]-r,robpos[1]-r,robpos[0]+r,robpos[1]+r)
    bulletprops={"bullet_id":bullet_id}
    return bulletprops
        
        
def firebullet(robprops):
    #robprops={"robotid":robot_id,"robotspeed":ROBOT_SPD,"robotpos":robpos}
    r=1 #what is r
    robpos=robprops["robotpos"]
    #return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    print("fire")
    print(robpos)
    #this is a list
    return robprops



#MAIN ROUTIN STARTS HERE
    
winprops=initialisewindow()
window=winprops["window"] 
c=winprops["canvas"]

robprops=initialiserobot(c)
bulletprops=initialisebullet(c, robprops)



ROBOT_R = 15
MID_X = winprops["width"] / 2
MID_Y = winprops["height"] /2
c.move(robprops["robot_id"], MID_X, MID_Y)
#c.move(robot_id2, MID_X, MID_Y)



  
c.bind_all('<Key>',move_robot)
window.mainloop(0)
