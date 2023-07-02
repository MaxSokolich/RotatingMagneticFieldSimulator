#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:07:19 2022

@author: bizzarohd
"""
"""
NOTES: my spoherical coordinate system is set up correctly. with the red arrow being the axis of rotation

but the magnetic vector field does not always follow the axis of rotation for certain gammas and alphas

"""
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time as time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.colors as colors
plt.style.use('dark_background')

class Helmholtz_Simulator:
    def __init__(self, alpha, gamma, freq, memory):
        self.start = time.time()


        self.diagram = plt.imread("Diagram.png")
        #define lists to store sineusoid in
        self.t_list = []
        self.Ix_List = []
        self.Iy_List = []
        self.Iz_List = []
        self.memory = memory

        #rolling parameters
        self.A = 1 #amplitude of rotating magetnic field
        self.alpha = alpha* (np.pi/180)   # yaw angle converted to radians
        self.gamma = gamma * (np.pi/180) # pitch angle converted to radians
        self.omega = 2*np.pi* float(freq)  #angular velocity of rotating field defined from input from Rotating Frequency Entry
        self.period = (2*np.pi)/self.omega  #time it takes for one cycle


        # Create figure for plotting
        self.fig = plt.figure(figsize=(14,4))
        self.fig.suptitle("alpha = {}     gamma = {}     freq = {}     ".format(alpha,gamma,freq))
        
        
        self.ax = self.fig.add_subplot(141, projection='3d')  #3d field sim
        self.ax.view_init(elev=30, azim=45)
       
        self.ax1 = self.fig.add_subplot(142, projection='3d')#self.fig.add_subplot(132)  #2d sine sim
        self.ax1.view_init(elev=30, azim=45)

        self.ax2 = self.fig.add_subplot(143)  #2d sine sim
        self.ax3 = self.fig.add_subplot(144)  #2d diagram image
        


        #params for field
        self.milli = 10**(-6)
        self.mu = 4*np.pi * (10**(-7)) / self.milli
    


        #define 3D grid
        grid_res = 8
        min_x,min_y,min_z = -25, -25,-25 #mm
        max_x, max_y, max_z = 25, 25,25

        X = np.arange(min_x, max_x, grid_res)
        Y = np.arange(min_y, max_y, grid_res)
        Z = np.arange(min_y, max_y, grid_res)
        self.x,self.y,self.z = np.meshgrid(X, Y, Z)

    #helmholtz X field equation
    def xb_field(self,x, Ix):
        a = 54 #radius
        c = (84/2) #distance between /2
        N = 260 #number of turns
        #the field at x away from the coil
        term1 = 1/ (a**2 + (c-x)**2)**(3/2)
        term2 = 1/ (a**2 + (c+x)**2)**(3/2)
        B = ((self.mu * N * Ix * a**2)/2 ) * (term1 + term2)
        return B

    #helmholtz Y field equation
    def yb_field(self,y, Iy):
        a = 35 #radius
        c = (66/2) #distance between /2
        N = 368 #number of turns
        #the field at x away from the coil
        term1 = 1/ ((a**2 + (c-y)**2)**(3/2))
        term2 = 1/ ((a**2 + (c+y)**2)**(3/2))
        B = ((self.mu * N * Iy * a**2)/2 ) * (term1 + term2)
        return B

    #helmholtz Z field equation
    def zb_field(self, z, Iz):
        a = 26 #radius
        c = (26/2) #distance between /2
        N = 368 #number of turns
        #the field at x away from the coil
        term1 = 1/ (a**2 + (c-z)**2)**(3/2)
        term2 = 1/ (a**2 + (c+z)**2)**(3/2)
        B = ((self.mu * N * Iz * a**2)/2 ) * (term1 + term2)
        return B

    # This function is called periodically from FuncAnimation

    def animate(self,i):
        tp = time.time() - self.start
        Ix = self.A * ( (np.cos(self.gamma) * np.cos(self.alpha) * np.cos(self.omega*tp)) + (np.sin(self.alpha) * np.sin(self.omega*tp)))
        Iy = self.A * (-(np.cos(self.gamma) * np.sin(self.alpha) * np.cos(self.omega*tp)) + (np.cos(self.alpha) * np.sin(self.omega*tp)))
        Iz = self.A * np.sin(self.gamma) * np.cos(self.omega*tp)

        #feed into helmhotz simulator
        BTotal_X = self.zb_field(self.x, Ix)
        BTotal_Y = self.zb_field(self.y, Iy)
        BTotal_Z = self.zb_field(self.z, Iz)

        #update Bfield lists for sinusoids
        self.t_list.append(tp)
        self.Ix_List.append(Ix)
        self.Iy_List.append(Iy)
        self.Iz_List.append(Iz)

        # Limit x and y lists to 20 items
        t_list = self.t_list[-self.memory:]
        Ix_List = self.Ix_List[-self.memory:]
        Iy_List = self.Iy_List[-self.memory:]
        Iz_List = self.Iz_List[-self.memory:]


        # Draw Bx,By,Bz field

        self.ax.clear()
        self.show_axis_rotation(self.ax, 50)
        speed = np.sqrt((BTotal_X)**2+(BTotal_Y)**2+(BTotal_Z)**2).flatten()
        self.ax.quiver(self.x,self.y,self.z,BTotal_X,BTotal_Y,BTotal_Z, color='black',length=1, norm = colors.LogNorm(vmin=speed.min(), vmax=speed.max() ))#,density = 2)#norm = colors.LogNorm(vmin=speed.min(), vmax=speed.max() ))
        self.ax.set_xlabel('x (mm)') 
        self.ax.set_ylabel('y (mm)') 
        self.ax.set_zlabel('z (mm)') 
        self.ax.set_title("Bvectorfield = [Bx, By, Bz]\n and Axis or Rotation") 


        # Draw x and y lists
        self.ax2.clear()
        self.ax2.plot(t_list, Ix_List, label = "Ix (A)", color = "red")
        self.ax2.plot(t_list, Iy_List, label = "Iy (A)", color = "yellow")
        self.ax2.plot(t_list, Iz_List, label = "Iz (A)", color = "blue")
        self.ax2.legend(loc='upper right')
        self.ax2.set_title("signals") 

        #plot IX,IY, IZ in 3D
        self.ax1.clear()    
        self.show_axis_rotation(self.ax1, 1)
        self.ax1.plot(Ix_List, Iy_List, Iz_List, label = "Iz (A)", color = "blue")
        self.ax1.set_xlabel('Ix (A)') 
        self.ax1.set_ylabel('Iy (A)') 
        self.ax1.set_zlabel('Iz (A)') 

     
        
    def show_axis_rotation(self, ax, length):
        #plot rotation axis
        x = 1 * np.sin(self.gamma) * np.cos(self.alpha)
        y = 1 * np.sin(self.gamma) * np.sin(self.alpha)  #need negative to match b field equations above?
        z = 1 * np.cos(self.gamma)
        ax.quiver(0,0,0,x,y,z,color='red',length=length)


    def run(self):
        # Set up plot to call animate() function periodically
        anim = animation.FuncAnimation(self.fig, self.animate, interval=1, blit = False)
        self.ax3.imshow(self.diagram)
        plt.show()


if __name__ == "__main__":
    alpha = 90
    gamma = 20
    freq = .5
    memory = 15  # for sinuoisd, so its only plot the last 15 points in the list
    sim = Helmholtz_Simulator(alpha, gamma, freq, memory)
    sim.run()