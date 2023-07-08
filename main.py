from src.HelmholtzRotating import Helmholtz_Simulator

if __name__ == "__main__":
    Bx = 0     #constant Bz field
    By = .9    #constant By field
    Bz = .9    #constant Bz field
    alpha = 90  # polar angle measure from the positive z axis
    gamma = 90  # azimuthal angle measure from the positive z axis
    psi = 90   # cone angle measure from the axis of rotation
    freq = .5  

    

    memory = 15  # for sinuoisd, so its only plot the last 15 points in the list
    
    sim = Helmholtz_Simulator(alpha, gamma,psi, freq, memory, Bx, By, Bz)
    sim.run()