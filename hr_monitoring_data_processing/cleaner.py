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
        if line.isdigit:
            new_data.append(int(line.strip())) 
    return new_data
        
in_data = ["1\n", "\n", "3\n", "4\n", "5\n", "\n", "7\n"]
print(filter_nondigits(in_data))

def filter_outliers(data: list) -> list:
    pass
        

    
