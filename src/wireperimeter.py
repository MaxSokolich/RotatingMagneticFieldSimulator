import numpy as np
# https://www.accelinstruments.com/Magnetic/Magnetic-field-calculator.html
milli = (10 **(-3))

t = 19*milli #thickness of coil in meters. in other words how long is the iron or air core. from flat face to flat face
h = 7*milli #height of coil in meters
inner_coil_diameter = 5 *milli #inner diameter of coil in meters. this is the diameter of the iron core rod, or air core
outer_coildiameter = inner_coil_diameter +h*2

dwire_bare = .45 *milli
dwire = dwire_bare+.00005 
area = np.pi * (dwire_bare/2)**2
ro = 1.68 * (10**(-8)) #resistivity of copper


height_turns = int(h/dwire)
thickness_turns = int(t/dwire)
Nt = height_turns * thickness_turns #theorteical number of turns

total_wire_length = 0 #total length of wire (sum of all perimeters) in meters
for i in range(0,height_turns):
    pi = np.pi*(inner_coil_diameter+i*dwire) * thickness_turns
    total_wire_length +=pi

resistance = (ro/area) * total_wire_length
print("coil height in mm = ", h*1000)
print("coil thickness in mm = ", t*1000)
print("inner coil diameter in mm = ", inner_coil_diameter*1000)
print("outer coil diameter in mm = ", outer_coildiameter*1000)
print("height turns = ", height_turns)
print("thickness turns = ", thickness_turns)
print("theoretical number of turns = ", Nt)
print("total length need is in feet: ", total_wire_length*3.28)
print("total length need is in meters: ", total_wire_length)

print("expected ressistance in ohms = ", resistance)