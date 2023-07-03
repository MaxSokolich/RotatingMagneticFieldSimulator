import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.colors as colors
import plotly.graph_objs as go


milli = 10**(-6)
Ix = 1 #current
Iy = .4
Iz = .2
mu = 4*np.pi * (10**(-7)) / milli
def xb_field(x):
    a = 54 #radius
    c = (84/2) #distance between /2
    N = 260 #number of turns
    #the field at x away from the coil
    term1 = 1/ (a**2 + (c-x)**2)**(3/2)
    term2 = 1/ (a**2 + (c+x)**2)**(3/2)
    B = ((mu * N * Ix * a**2)/2 ) * (term1 + term2)
    return B

def yb_field(y):
    a = 35 #radius
    c = (66/2) #distance between /2
    N = 368 #number of turns
    #the field at x away from the coil
    term1 = 1/ ((a**2 + (c-y)**2)**(3/2))
    term2 = 1/ ((a**2 + (c+y)**2)**(3/2))
    B = ((mu * N * Iy * a**2)/2 ) * (term1 + term2)
    return B

def zb_field(z):
    a = 26 #radius
    c = (26/2) #distance between /2
    N = 368 #number of turns
    #the field at x away from the coil
    term1 = 1/ (a**2 + (c-z)**2)**(3/2)
    term2 = 1/ (a**2 + (c+z)**2)**(3/2)
    B = ((mu * N * Iz * a**2)/2 ) * (term1 + term2)
    return B


print("field = {}mT".format(xb_field(35)))



#form grid
grid_res = 25
min_x,min_y,min_z = -100, -100,-100 #mm
max_x, max_y, max_z = 100, 100,100

X = np.arange(min_x, max_x, grid_res)
Y = np.arange(min_y, max_y, grid_res)
Z = np.arange(min_y, max_y, grid_res)
x,y,z = np.meshgrid(X, Y, Z)

BTotal_X = xb_field(x)
BTotal_Y = yb_field(y)
BTotal_Z = zb_field(z)

speed = np.sqrt((BTotal_X)**2+(BTotal_Y)**2+(BTotal_Z)**2).flatten()
print(speed.shape)
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 


qq = ax.quiver(x,y,z,BTotal_X,BTotal_Y,BTotal_Z, speed, cmap='coolwarm',length=5, norm = colors.LogNorm(vmin=speed.min(), vmax=speed.max() ))#,density = 2)#norm = colors.LogNorm(vmin=speed.min(), vmax=speed.max() ))
plt.colorbar(qq, cmap=plt.cm.jet)
ax.set_xlabel('X') 
ax.set_ylabel('Y') 
ax.set_zlabel('Z') 
ax.set_title('3D Streamplot') 

plt.show()