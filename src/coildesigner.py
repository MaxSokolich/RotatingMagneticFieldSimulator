import numpy as np
import matplotlib.pyplot as plt
# https://www.accelinstruments.com/Magnetic/Magnetic-field-calculator.html
milli = (10 **(-3))
dwire_bare = .5105 *milli
dwire = dwire_bare+.00005   #diameter of wire in meters

t = 14*milli #thickness of coil in meters
#h = 10*milli #height of coil in meters
Nt = 480
inner_coil_diameter = 90 * milli #inner diameter of coil in meters
I = 2


#height_turns = int(h/dwire)
thickness_turns = int(t/dwire)

height_turns = int(Nt/thickness_turns)
h = dwire*height_turns

#Nt = height_turns * thickness_turns #theorteical number of turns

total_wire_length = 0 #total length of wire (sum of all perimeters) in meters
for i in range(0,height_turns):
    pi = np.pi*(inner_coil_diameter+i*dwire) * thickness_turns
    total_wire_length +=pi


area = np.pi * (dwire_bare/2)**2
ro = 1.68 * (10**(-8)) #resistivity of copper

resistance = (ro/area) * total_wire_length
print("theoretical number of turns = ", Nt)
print("coil thickness in mm = ", t*1000)
print("inner coil diameter in mm = ", inner_coil_diameter*1000)
print("height turns = ", height_turns)
print("thickness turns = ", thickness_turns)

print("\ncoil height in mm = ", h*1000)
print("total length need is in feet: ", total_wire_length*3.28)
print("total length need is in meters: ", total_wire_length)

print("expected ressistance in ohms = ", resistance)



mu = 4*np.pi * (10**(-7)) #/ milli


a = (inner_coil_diameter+h)/2 #radius
c = 50 *milli#a/2 #distance between /2
V = I*resistance
print("voltage =  ", V)
print("current = ", I)
#V = I*R

def noah_field(x):
  
    
    #the field at x away from the coil
    term1 = 1/ ((a**2 + (c-x)**2)**(3/2))
    term2 = 1/ ((a**2 + (c+x)**2)**(3/2))

    B = ((mu * Nt * I * a**2)/2 ) * (term1 + term2)
    return B
print("\nfield at center of one coil = ", noah_field(a)*1000)
print("field between coils = ", noah_field(0)*1000)
x = np.linspace(-a,a, 20)
field = noah_field(x)
plt.figure()
plt.plot(x, noah_field(x))
plt.show()