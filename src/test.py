import os , sys

#sys.path.insert(1, '/home/snr/planner_ws/snr_waypoint_planner/src/')
import numpy as np 
import matplotlib.pyplot as plt
from math import atan2, cos, sin

import numpy as np
import math
from trajectory_creation import jtraj, mstraj
from collections import namedtuple

def main():

    #positions  
    a = [0, 20, 20, 0,0] # for testing! | creates rectangle
    b = [0, 0, 20, 20,0] # for testing!  | creates rectangle 
    
    x = np.array(a)
    y = np.array(b) 

    ctr = np.vstack((x,y)).T #stack x and y points 
    ctr[:,0] = x 
    ctr[:,1] = y
    
    
    out =mstraj.mstraj(ctr, dt=0.1, tacc=20, qdmax=1.0) # mstraj(path, dt=0.1, tacc=10, qdmax=2.5) # extra=True)
    print(out.q)
    
    plt.figure()
    plt.plot(out.t, out.q)
    plt.grid(True)
    plt.xlabel('time')
    plt.legend(('$q_0$', '$q_1$'))
    plt.plot(a,b, 'bo') #  out.viapoints,
    
    plt.figure()
    plt.plot(out.q[:,0], out.q[:,1])
    
    plt.plot(a,b,'ro')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.show() 

    

if __name__ == "__main__":
    main() 