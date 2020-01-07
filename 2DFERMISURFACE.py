import numpy as np
import matplotlib.pyplot as plt
import pylab

def dispersion_relation(kx,ky):
    tx=1
    ty=1
    ax=1
    ay=1

    return (-2*(tx)*(np.cos(kx*ax)))-(2*(ty)*(np.cos(ky*ay)))
kmax=3
N=500

energies=np.zeros((N,N))
kxlist=np.linspace(-kmax,kmax,N)
kylist=np.linspace(-kmax,kmax,N)
   
for i in range(N):
    for j in range(N):
        energies[i,j]=dispersion_relation(kxlist[i],kylist[j])


plt.imshow(energies)
plt.hot()
cbar=plt.colorbar()
cbar.set_label('Energy')
plt.xlabel('kx')
plt.ylabel('ky')
pylab.show()        
            
