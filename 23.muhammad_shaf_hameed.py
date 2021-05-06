import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
import math as m
gravitational_acceleration=9.8
def graphA():
    velocity=velocityvalue.get()
    theta=thetavalue.get()
    thetachange = np.arange(m.pi/6, m.pi/2, m.pi/36)
    t = ((2 * velocity) * np.sin(thetachange)) / gravitational_acceleration
    degree=(thetachange*180)/m.pi
    print(t)
    plt.plot(degree,t,label=r'$ t = \frac{ \mathcal{2v}\sin(\theta)}{g}$')
    plt.title('projectile graph')
    plt.xlabel('angle' r'$ (\theta)$')
    plt.ylabel('time of projectile (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


    
    
def tkinter():
    global thetavalue
    global velocityvalue
    
    
    root = Tk()
    root.title('PROJECTILE MOTION')
    photo = PhotoImage(file = "2.png")
    w = Label(root, image=photo)
    w.pack()
    
    label1=Label(root,text='ENTER THETA VALUE::' ,bg='#33FF93')
    label1.pack()

    thetavalue = IntVar()
    ent = Entry(root,textvariable=thetavalue)
    ent.pack()
    

    label2=Label(root,text='ENTER VELOCITY VALUE:',bg='#33FF93')
    label2.pack()

    velocityvalue = IntVar()
    ent2=Entry(root,textvariable=velocityvalue)
    ent2.pack()

    

    button = Button(root,bg="#FF5833",fg="#ecf0f1",font=("cala"),text="RELATION WITHRESPECT TO THETA",justify="center", command=graphA)
    button.pack()
    
   
    
    root.mainloop()

tkinter()

