import matplotlib.pyplot as plt
from utilities import FileReader

def plot_errors(filename):
    headers, values=FileReader(filename).read_file()

    # Timestamp List
    time_list=[]
    first_stamp=values[0][-1]
    for val in values:
        time_list.append(val[-1] - first_stamp)
    
    fig, axes = plt.subplots(1,2, figsize=(14,6))

    x_labels = []
    y_labels = []
    label_units = []
    title_prefix = ""
    if filename == "linear.csv":
        title_prefix = "Linear Error: "
        label_units = ["[m]", "[m/s]", ""]
        x_labels = ["e [m]", "Time [ns]"]
        y_labels = ["e_dot [m/s]", "Errors"]
    elif filename == "angular.csv":
        title_prefix = "Angular Error: "
        label_units = ["[m]", "[m/s]", ""]
        x_labels = ["e [m]", "Time [ns]"]
        y_labels = ["e_dot [m/s]", "Errors"]
    elif filename == "robot_pose.csv":
        title_prefix = "Robot Pose: "
        label_units = ["[m]", "[m]", "[rad]"]
        x_labels = ["x [m]", "Time [ns]"]
        y_labels = ["y [m/s]", "Pose Measurements"]

    axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    axes[0].set_title(title_prefix + "State Space")
    axes[0].set_xlabel(x_labels[0])
    axes[0].set_ylabel(y_labels[0])
    axes[0].grid()

    axes[1].set_title(title_prefix + "Each Individual State")
    axes[1].set_xlabel(x_labels[1])
    axes[1].set_ylabel(y_labels[1])
    for i in range(0, len(headers) - 1):
        axes[1].plot(time_list, [lin[i] for lin in values], label = headers[i] + " " + label_units[i])

    axes[1].legend()
    axes[1].grid()

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



