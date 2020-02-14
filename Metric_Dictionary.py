def dictionary_of_metrics(items):
    """Takes a list of items and returns a dictionary of summary statistics"""
    n   = len(items)
    Ave = round(np.mean(items),2)
    Med = round(np.median(items),2)
    Var = round((sum((items-np.mean(items))**2))/(n-1),2)
    Std = round(((sum((items-np.mean(items))**2))/(n-1))**(1/2),2)
    Min = round(min(items),2)
    Max = round(max(items),2)
    
    return {'mean':Ave,'median':Med,'var':Var,'std':Std,'min':Min,'max':Max}
