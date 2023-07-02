# RotatingMagneticFieldSimulator

NOTES: my spoherical coordinate system IS set up correctly. with the red arrow being the axis of rotation

disregard the diagram for now, the equations are all messed up in the first place.


7/6 2:00pm
but the magnetic vector field does not always follow the axis of rotation for certain gammas and alphas

right hand rule only works for one axis

wanything in the y direction seems to be working well

x -- right hand rule is flipped....    think i got it-----> the entire Iy expression needs to be negative.

7/7 4:30 pm
but this flips the Y right hand rule.... 

7/6 6:00 pm
there are some serious issues with the rotating magnetic field equations.  I can get it to work for some combinations of alpha and gamma but then it wont work for other ones.

For example, if you let gamma = 0, you would expect the output field to just spin like weve seen. but this is not always the case and is completely dependent on alpha. 

similarly, alpha = 45, and gamma = 45 show very odd behavior.

To change these values, scroll down to the bottom of the file and underneath "if name == main" is where the class is called.
also in the animate function, un comment line 108 if you want the self.alpha value to be overidden by the animate loop variable "i". this will update self.alpha with i which is in range(360) on line 77.


"""


<img width="1385" alt="Window" src="https://github.com/MaxSokolich/RotatingMagneticFieldSimulator/assets/50302377/636cd454-fb44-4ec8-96c4-cfa9223661a9">
