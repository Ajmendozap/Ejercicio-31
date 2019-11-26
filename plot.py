import numpy as np
import matplotlib.pyplot as plt



def grafica(datafile, plotfile, plotlabel):
    data = np.loadtxt(datafile)
    
    
    plt.figure(figsize=(14,4))

    x = np.linspace(-1,1,n_x)
    delta_t = 1.0/n_t
    for i in range(n_t):
        if i%(n_t//9) == 0:
            plt.plot(x, data[i,:], alpha=(i+1)/n_t, color='black', label="t={:.02f}".format(i*delta_t))
    plt.legend(loc=1)
    plt.xlabel("Posicion")
    plt.ylabel("$\psi$")
            


    plt.savefig(plotfile, bbox_inches='tight')

grafica("evolve_10.dat", "evolve_10.png", "$N_x=10$ ,  $N_{tc}$")


