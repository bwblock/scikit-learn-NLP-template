def studentReg(ages_train, net_worths_train):

    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit (ages_train, net_worths_train)



    return reg