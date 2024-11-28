def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    new_data = []
    for line in data:
        line = line.strip()
        if line.isdigit():
            new_data.append(int(line))
    return new_data
        

def filter_outliers(data: list) -> list:
    pass
        

    
