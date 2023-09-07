import numpy as np
import matplotlib.pyplot as plt
milli = 10**(-3)

mu = 4*np.pi * (10**(-7)) #/ milli

I = 1
R = 9.7
V = I*R
N = 368 #number of turns
print("voltage: ", V)
#V = I*R

a = 45*milli  #radius
c = (45*milli/2) #distance between /2
def noah_field(x):
    
    
    #the field at x away from the coil
    term1 = 1/ ((a**2 + (c-x)**2)**(3/2))
    term2 = 1/ ((a**2 + (c+x)**2)**(3/2))

    B = ((mu * N * I * a**2)/2 ) * (term1 + term2)
    return B
print("field at center of one coil = ", noah_field(a)*1000)
print("field between coils = ", noah_field(0)*1000)
x = np.linspace(-a,a, 20)
field = noah_field(x)
plt.figure()
plt.plot(x, noah_field(x))
plt.show()