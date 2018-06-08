# Pantographe
Strain Gradient Theory Simulation

## Description 
This folder uses periodic pantographe structure to verify the bending strain gradient theory, see more details in  <https://onlinelibrary.wiley.com/doi/10.1002/9781119005247.ch6>, and Arthur Lebee is the professor supervised me for this research intern.

In this project, we verify the strain gradient thoery using the pantographe structure and analyze related local deformation and global deformation based on python scripting and provided a sysmatical method to calculate the equivalent matrix C, D, F, G, H.

The geometric structure and mesh setting is done in file Pantographe.py without any manipulation of GUI.

## Implementation
run the `main.py` in Abaqus to see more details.
See `Laminate.py` and `Pantographe.py` for two choice of cell geometry for verification.
See `DLOAD_SIGINI.for` for the Abaqus Subroutine implementation (Fortran scripting) where prestress and specified forces at each intergration points are established.
See `Calcul_complet.py` for the second round verification by using complete structure instead of cell strcuture (Laminate or Pantograph)
