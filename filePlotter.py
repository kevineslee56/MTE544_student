# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
import numpy as np
from utilities import FileReader
import re
import math

def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file() 
    time_list=[]
    first_stamp=values[0][-1]

    if "laser" in filename:
        # # Choose which laser scan to plot
        scan_index = 10
        
        # Method 1: Headers "x" and "y" (to be removed after Lab1)
        # assumption: each scan contains 720 entries
        # x_list = [values[i][0] for i in range(720*scan_index, 720*(scan_index+1), 1) if values[i][0] != np.inf]
        # y_list = [values[i][1] for i in range(720*scan_index, 720*(scan_index+1), 1) if values[i][1] != np.inf]

        # Method 2: Headers "ranges" (to be removed after Lab1)
        x_list = []
        y_list = []
        theta = 0
        theta_increment = 0.5*math.pi/180
        for range in values[scan_index][:-1]:
            if range != np.inf:
                x_list.append(range*math.cos(theta))
                y_list.append(range*math.sin(theta))
                print(range*math.cos(theta))
            theta += theta_increment
    
        plt.scatter(x_list, y_list)

        # Method 3: Headers "x_list" and "y_list" (to be kept after Lab1)
        # x_list = values[scan_index][0]
        # y_list = values[scan_index][1]
        # plt.scatter(x_list, y_list)
    else:
        for val in values:
            time_list.append(val[-1] - first_stamp)

        for i in range(0, len(headers) - 1):
            plt.plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")
        
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.legend()
    plt.grid()
    plt.show()
    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename)
