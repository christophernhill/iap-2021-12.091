#
#  Simple serial code that does 
#
#  d phi / dt = d/dx k d/dx phi
#
#  in 1d
#
import numpy as np

Lx=1.
nx=1000 
dx=Lx/nx
hw=1

phi_arr=np.zeros(nx+2)
kappa_arr=np.zeros(nx+2)
