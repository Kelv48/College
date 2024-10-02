import tkinter as tk
from random import randint
import time
from datetime import datetime
from math import sqrt

def mouse_function(event):
    randomX = randint(0, 300)
    randomY = randint(0, 300)
    myCanvas.create_oval(randomX, randomY, event.x + 20, event.y + 20, fill='red')
    check(event, randomX, randomY)
    
    

def check(event, randomX, randomY):
    xCent = randomX + (event.x - randomX)/2   
    yCent = randomY + (event.y - randomY)/2
    radius = (event.x - randomX)/2
    distance = sqrt( (event.x - randomX)^2 + (event.y - randomY)^2 )
    print(distance)


    


time1 = datetime.now()  
root = tk.Tk()
myCanvas = tk.Canvas(root, bg="white", height=300, width=300)
myCanvas.bind("<Button-1>", mouse_function)

print(time1)
myCanvas.pack()
root.mainloop()






