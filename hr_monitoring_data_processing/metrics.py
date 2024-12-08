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
    
#  Breakdown of the formula:
# SMAj: Represents the Simple Moving Average at position "j" in the data series.
# (1/k): This part simply divides the sum by the number of data points considered ("k") to calculate the average.
# ∑ (i=j-1 to j+k-1) ai:
# ∑: This symbol represents the "summation" operation, meaning we are adding up a series of values.
# i=j-1 to j+k-1: This indicates that we are summing up values from position "j-1" (one point before "j") to "j+k-1" (k points after "j"), effectively including "k" data points centered around "j".
# ai: Represents the value at position "i" in the data series
    
    window_size = n    
    maximum = []
    for num in range(0, len(data), window_size):
         window = data[num:num + window_size]
         maximum.append(max(window))
    return maximum
    
... 


def window_average(data: list, n: int) -> list:
    pass


def window_stddev(data: list, n: int) -> list:
    pass
