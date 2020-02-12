def five_num_summary(items):
    
    percentile = np.percentile(items, [0,25,50,75,100]) #A list of percentiles
    Min = round(percentile[0],2)
    Q1  = round(percentile[1],2)
    Med = round(percentile[2],2)
    Q3  = round(percentile[3],2)
    Max = round(percentile[4],2)
    
    return {'max':Max,'median':Med,'min':Min,'q1':Q1,'q3':Q3}