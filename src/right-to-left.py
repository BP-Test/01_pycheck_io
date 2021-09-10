### Combine above two
def left_join(phrases: list) -> str:
    """
    join into a string seperated by ',' and then replace all 'right' to 'left' 
    
    """
    comma = ','.join(phrases)
    replace = comma.replace('right','left')
    return replace