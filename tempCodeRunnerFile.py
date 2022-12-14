dataSet = {
        'x' : x_list,
        'y' : y_list,
        'Y-Predict' : yPredict,
        'error' : error,
    }
    dataSet2 = {
        'RSS' : rss,
        'COST' : cost,
        'THETA' : theta
    }
    print(dataSet2)
    print(pd.DataFrame(dataSet))