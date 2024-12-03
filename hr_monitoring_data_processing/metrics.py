def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """

    maximums = []
    max = 0
    for num in range(n):
        for num in data:
           if num > max:
               max = num  
           maximums.append(max)     
        return maximums
        
print(window_max([1, 2, 3, 4, 5, 6, 7], 1))

... 


def window_average(data: list, n: int) -> list:
    pass


def window_stddev(data: list, n: int) -> list:
    pass
