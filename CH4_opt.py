# CH4 optimization
from ase.build import molecule
from ase import Atoms
from gpaw import GPAW
import os
from gpaw.tddft import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ase.optimize import QuasiNewton
# set directory
dir='/home/user4/Documents/Ali/opt'
if not os.path.exists(dir):
    os.makedirs(dir)
os.chdir(dir)
from ase.io import write
d=1.10   # guess bond length
# guess a structure
atoms=Atoms('CH4', positions=[[0.5*np.sqrt(2)*d,0,0],[0,0,d],[0.5*np.sqrt(2)*d,0,-d],[0,d,0.1*np.sqrt(2)*d],[0,-d,0.1*np.sqrt(2)*d]],pbc=False) # periodic boundary condition
# vaccum from center
atoms.center(vacuum=4.0)
# write as a cif file
write('CH4.cif',atoms)
# you can write cif or espresso-in
calc=GPAW(h=0.10, xc='PBE', txt='CH4_relax.txt')   # define calculator
atoms.calc=calc
# optimize
from ase.optimize import QuasiNewton
opt=QuasiNewton(atoms,trajectory='CH4.traj')
opt.run(fmax=0.01)    # calculate untill all atomix forces are below 0.01 ev per A
