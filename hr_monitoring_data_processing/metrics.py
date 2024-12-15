import statistics as stat

def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
     
    '''Rolling Average 

[1, 3, 4, 2, 8, 10 ,12]

N = 2 (WINDOW SIZE EVERY 2 ELEMENTS)


This outputs the average from every 2
So average of 

[1, 3], [4, 2], [8, 10], 12
[2, 3, 9, 12]'''
      
    maximum = []

    if len(data) == 0 or n <= 0:
        return []

    for num in range(0, len(data), n):
         window = data[num:num + n]
         maximum.append(max(window))
    return maximum

def window_average(data: list, n: int) -> list:
    """
    Calculate average value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of averages from each window 
    """
  
    average = []

    if len(data) == 0 or n <= 0:
        return []

    for num in range(0, len(data), n):
         window = data[num:num + n]
         average.append(sum(window) / len(window))
    return average
     
       
def window_stddev(data: list, n: int) -> list:
    """
    Calculate standard deviation value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[float]: list of standard deviation from each window 
    """
    
    standard_dev = []


    if len(data) == 0 or n <= 0:
        return []

    for num in range(0, len(data), n):
         window = data[num:num + n]
         if len(window) > 1:
             standard = stat.stdev(window)
             string = f"{standard:.02f}"
             standard_dev.append(float(string))
    return standard_dev