# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import matplotlib.pyplot as plt
import numpy as np
from utilities import FileReader
import math

def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file() 
    time_list=[]
    first_stamp=values[0][-1]

    if "laser" in filename:
        # Choose which laser scan to plot
        scan_index = 10
        
        x_list = []
        y_list = []
        theta = 0
        theta_increment = 0.5*math.pi/180
        for scan_range in values[scan_index][:-1]:
            if scan_range != np.inf:
                x_list.append(scan_range*math.cos(theta))
                y_list.append(scan_range*math.sin(theta))
            theta += theta_increment
    
        plt.scatter(x_list, y_list)
    else:
        for val in values:
            time_list.append(val[-1] - first_stamp)

        for i in range(0, len(headers) - 1):
            plt.plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")

    # change as necessary to match data
    plt.title("Line IMU Readings")
    plt.ylabel("IMU Readings")
    plt.xlabel("Time")

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
