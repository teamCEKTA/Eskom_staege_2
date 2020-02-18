def dictionary_of_metrics(items):
    """Takes a list of items and returns a dictionary of summary statistics"""
    n   = len(items)
    average = round(np.mean(items),2)
    median = round(np.median(items),2)
    variance = round((sum((items-np.mean(items))**2))/(n-1),2)
    standard_dev = round(((sum((items-np.mean(items))**2))/(n-1))**(1/2),2)
    minimum = round(min(items),2)
    maximum = round(max(items),2)
    
    return {'mean':average,'median':median,'var':variance,'std':standard_dev,'min':minimum,'max':maximum}
