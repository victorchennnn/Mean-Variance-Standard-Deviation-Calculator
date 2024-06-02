import numpy as np

def calculate(list):
    if(len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    
    calculations = {}
    df = np.array(list)
    df = np.reshape(df,(3,3))

    #mean
    mean_axis1 = np.mean(df,axis=0).tolist()
    mean_axis2 = np.mean(df,axis=1).tolist()
    mean_flattened = np.mean(df)

    calculations["mean"] = [mean_axis1,mean_axis2,mean_flattened]

    #variance
    var_axis1 = np.var(df,axis=0).tolist()
    var_axis2 = np.var(df,axis=1).tolist()
    var_flattened = np.var(df)

    calculations["variance"] = [var_axis1,var_axis2,var_flattened]

    #standard deviation
    std_axis1 = np.std(df,axis=0).tolist()
    std_axis2 = np.std(df,axis=1).tolist()
    std_flattened = np.std(df)

    calculations["standard deviation"] = [std_axis1,std_axis2,std_flattened]

    #max
    max_axis1 = np.max(df,axis=0).tolist()
    max_axis2 = np.max(df,axis=1).tolist()
    max_flattened = np.max(df)

    calculations["max"] = [max_axis1,max_axis2,max_flattened]

    #min
    min_axis1 = np.min(df,axis=0).tolist()
    min_axis2 = np.min(df,axis=1).tolist()
    min_flattened = np.min(df)

    calculations["min"] = [min_axis1,min_axis2,min_flattened]

    #sum
    sum_axis1 = np.sum(df,axis=0).tolist()
    sum_axis2 = np.sum(df,axis=1).tolist()
    sum_flattened = np.sum(df)

    calculations["sum"] = [sum_axis1,sum_axis2,sum_flattened]

    return calculations
