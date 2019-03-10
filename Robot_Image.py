#
"""
Created on Tue Sep 12 18:13:36 2017

@author: louis griffiths
"""

#This program will draw an alien

from tkinter import *

HEIGHT=500
WIDTH=800





def move_robot(event):
    if event.keysym == 's':
        c.move(robot_id, 0, ROBOT_SPD)
#        c.move(robot_id2, 0, ROBOT_SPD)   
    elif event.keysym == 'w':
        c.move(robot_id, 0, -ROBOT_SPD)
#        c.move(robot_id2, 0, ROBOT_SPD)    
    elif event.keysym == 'a':
       c.move(robot_id, -ROBOT_SPD, 0)
#       c.move(robot_id2, 0, ROBOT_SPD)    
    elif event.keysym == 'd':
       c.move(robot_id, ROBOT_SPD,0)
#       c.move(robot_id2, 0, ROBOT_SPD)





window=Tk()
window.title('robot')

c = Canvas(window, height=HEIGHT, width=WIDTH)
c.pack()

#body = c.create_polygon(100, 150, 300, 250, fill='red')

robot_id = c.create_polygon(180, 75, 220, 75, 200, 20, fill='red')
ROBOT_R = 15
MID_X = WIDTH / 2
MID_Y = WIDTH /2
c.move(robot_id, MID_X, MID_Y)
#c.move(robot_id2, MID_X, MID_Y)

ROBOT_SPD = 10

    
c.bind_all('<Key>',move_robot)
window.mainloop(0)




#you can change the colours by changing fill='blue'or whatever the colour is 
#this was from a book by carrel vordeman 
#this program dosn't work till finished  





