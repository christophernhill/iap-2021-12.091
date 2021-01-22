# iap-2021-12.091

# Directory of MPI example for 1d diffusion equation.

Files: 

 - __diffusion1d.ipynb__
 
    A simple serial example of 1d diffusion equation for starting creating an
    MPI equivalent. Creation of MPI counterpart is shown in the files step1.py - 
    step6.py.
 
 - __step1.py__
 
    Illustrates using mpi4py Python package for MPI, and creating multiple
    MPI ranks running on several processes.
 
 - __step2.py__
 
    Adds code that illustrates basic message sending between ranks using
    MPI. 


 - __step3.py__
 
    Introduces code that divides the indices of a global vector into
    local blocks of indices split over ranks with halo.
 
 - __step4.py__
 
   Introduces send and receive of halo region for a divided vector. 
 
 - __step5.py__
 
  Initializes a distributed array based on global spatial coordinate that each MPI 
  rank is working on.
 
 - __step6.py__

 Add in time-stepping loop that computes time derivatives and updates halo points at
 each time step. 
 
# To run on TXE1

  - To run serial code in __diffusion1d.ipynb__ 
  
    Runs within notebook after installing python celluloid package.
    
    For now, to install celluloid do this once.
    1. Open terminal from within notebook
    2. from terminal login to front end node e.g. `ssh login-2`
    3. on login node run the following two commands
          ```
             module load anaconda/2020b
             pip install --user celluloid
          ```
          
  
   
