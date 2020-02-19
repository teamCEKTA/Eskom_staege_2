def five_num_summary(items):
    """Takes a list of items and returns a dictionary of five number summary"""
    percentile = np.percentile(items, [0,25,50,75,100]) #A list of percentiles
    minimum = round(percentile[0],2)
    quartile_1 = round(percentile[1],2)
    median = round(percentile[2],2)
    quartile_3 = round(percentile[3],2)
    maximmu = round(percentile[4],2)
    
    return {'max':maximmu,'median':median,'min':minimum,'q1':quartile_1,'q3':quartile_3}
