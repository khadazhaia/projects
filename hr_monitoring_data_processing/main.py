"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    data = []

    # open file and read into the `data` list
    path = open(filename)
    for line in path:
        data.append(line)
    path.close()

    # filter out all non-digits and outliers
    data = filter_nondigits(data)
    data  = filter_outliers(data)

    # calc max, average and standard dev
    rolling_max = window_max(data, 6)
    rolling_average = window_average(data, 6)
    rolling_stdev = window_stddev(data, 6)

    # save the plots
    plt.plot(rolling_max)
    plt.savefig("images/maximums.png", dpi=300, bbox_inches="tight")
    plt.clf() 

    plt.plot(rolling_average)
    plt.savefig("images/averages.png", dpi=300, bbox_inches="tight")
    plt.clf() 
  
    plt.plot(rolling_stdev)
    plt.savefig("images/stdevs.png", dpi=300, bbox_inches="tight")
    plt.clf() 

    # return all 3 lists
    return rolling_max, rolling_average, rolling_stdev

if __name__ == "__main__":
    run("data/data1.txt")
 