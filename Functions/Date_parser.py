def date_parser(dates):
    """takes a list of datetime strings and converts it into a list of strings with only the date."""
    return([item.split()[0] for item in dates])
    pass