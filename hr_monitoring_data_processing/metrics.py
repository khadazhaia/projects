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
    for wind in range(1):
        wind = data[::n]
        maximum.append(((wind)))    
    return maximum
        
print(window_max([1, 2, 3, 4, 5, 6, 7], 4))

... 


def window_average(data: list, n: int) -> list:
    pass


def window_stddev(data: list, n: int) -> list:
    pass
