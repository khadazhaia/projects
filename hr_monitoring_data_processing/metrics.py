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
    

    window_size = n    
    maximum = []

    if len(data) == 0 or window_size <= 0:
        return []

    for num in range(0, len(data), window_size):
         window = data[num:num + window_size]
         maximum.append(max(window))
    return maximum

def window_average(data: list, n: int) -> list:
    pass

       
def window_stddev(data: list, n: int) -> list:
    pass
