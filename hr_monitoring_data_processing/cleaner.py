def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """

    # Intialize an empty list 
    new_data = []

    # Error handling
    if len(data) == 0:
        return data

    # Iterate over the data and append only integers to the initialized list 
    for line in data:
        line = line.strip()
        if line.isdigit():
            new_data.append(int(line))
    return new_data
        

def filter_outliers(data: list) -> list:
    """ Filter out integers that are greater than 30 & less than 250
    
    Args: 
        data (list[int]): list of integers representing heart rate samples.
            Might contain outliers or missing data
    
    Returns:
         list[int]: list of integers between 30 & 250
    """

    # Intialize an empty list 
    new_data = []

    # Error handling
    if len(data) == 0:
        return data 
    
    # Iterate over the data and append any integers between 30 & 250 to the initialized list
    for num in data:
        if num > 30 and num < 250:
            new_data.append(num)     
    return new_data
        

    
