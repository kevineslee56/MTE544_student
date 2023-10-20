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

    label_units = []
    title_prefix = ""
    if filename == "linear.csv":
        title_prefix = "Linear Error: "
        label_units.append(["[m]", "[m/s]"])
        label_units.append(["[m]", "[m/s]", ""])
    elif filename == "angular.csv":
        title_prefix = "Angular Error: "
        label_units.append(["[m]", "[m/s]"])
        label_units.append(["[m]", "[m/s]", ""])
    elif filename == "robot_pose.csv":
        title_prefix = "Robot Pose: "
        label_units.append(["[m]", "[m]"])
        label_units.append(["[m]", "[m]", "[rad]"])

    axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    axes[0].set_title(title_prefix + "State Space")
    axes[0].grid()

    axes[1].set_title(title_prefix + "Each Individual State")
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



