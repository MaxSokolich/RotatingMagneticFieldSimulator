# RotatingMagneticFieldSimulator
the simulator takes generates the current inputs Ix, Iy,Iz to the 3 axis helmholtz coils, then outputs the correct Bfield using the equations from this website: https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_(Tatum)/06%3A_The_Magnetic_Effect_of_an_Electric_Current/6.07%3A_Helmholtz_Coils

I have functions to genreate the magnetic field based on each of our coils and there attributes (number of turns, radius, distance etc) b

spoherical coordinate system is set up correctly. with the red arrow being the axis of rotation

# USAGE

run "python3 main.py" in terminal. you can change:

Bx = 0     #constant Bz field
By = .9    #constant By field
Bz = .9    #constant Bz field
alpha = 90  # polar angle measure from the positive z axis
gamma = 90  # azimuthal angle measure from the positive z axis
psi = 90   # cone angle measure from the axis of rotation
freq = .5  

in the main file to visualize the outputing magnetic field.




<img width="1385" alt="Window" src="https://github.com/MaxSokolich/RotatingMagneticFieldSimulator/assets/50302377/636cd454-fb44-4ec8-96c4-cfa9223661a9">
