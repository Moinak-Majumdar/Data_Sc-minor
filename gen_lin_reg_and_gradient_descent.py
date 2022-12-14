import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# hl3 functons for calulation   
# to calculate x - x_mean and y - y_mean
def val_minus_mean(set, set_mean) :
    res = [] 
    for elm in set :
        res.append(round(elm - set_mean, 2))
    
    return res

# to get square of list
def square_of_list(list) :
    l = []
    for elm in list :
        l.append(round(elm ** 2, 2))

    return l

# to get product if two list 
def product_of_list (l1, l2) :
    res = []
    for i in range(0, len(l1)) :
        res.append(round(l1[i] * l2[i], 2))

    return res
# to get l1 - l2
def difference_of_list (l1, l2) :
    res = []
    for i in range(0, len(l1)) :
        res.append(round(l1[i] - l2[i], 2))

    return res

def lin_equ (m, c, x_list) :
    l = []
    for elm in x_list :
        mx = m * elm
        total = mx + c 
        l.append(round(total, 2))

    return l
# cost function
def gen_cost (theta, x_list, y_list) :
    print()
    y_mean = np.mean(y_list)
    x_mean = np.mean(x_list)
    c = round(y_mean - theta * x_mean, 2)
    yPredict = lin_equ(theta, c, x_list)
    error = difference_of_list(y_list, yPredict)
    error_square = square_of_list(error)
    n = 2 * len(y_list)
    rss = round(np.sum(error_square), 2)
    cost = round(rss / n, 2)

    dataSet = {
        'x' : x_list,
        'y' : y_list,
        'Y-Predict' : yPredict,
        'error' : error,
        'error square' : error_square
    }
    dataSet2 = {
        'THETA' : theta,
        'COST' : cost,
        'RSS' :rss,
    }
    print(pd.DataFrame(dataSet))
    print(dataSet2)
    
    return cost

def gen_gradient_descent (theta, alfa, cost) :
    d =  cost / theta
    alfa_d = d * alfa
    return theta - alfa_d

def calculate_final (slope, x_list, y_list, cost) :
    slopeList = []
    costList = []
    alfa = len(x_list)
    gradient_descent = gen_gradient_descent(slope, alfa, cost)
    curr_slope = gradient_descent
    curr_cost = cost

    while (curr_slope <= 2*slope) :
        curr_cost = gen_cost(curr_slope, x_list, y_list)
        costList.append(curr_cost)
        slopeList.append(round(curr_slope,2))
        curr_slope += gradient_descent
        curr_slope = round(curr_slope,3)

    return {
        'slopeList' : slopeList,
        'costList' : costList,
    }

#hl6 input data set   
x=[1,2,3,4,5]
y=[7,14,15,18,19]

x_mean = np.mean(x)
y_mean = np.mean(y)

x_minus_x_mean = val_minus_mean(x, x_mean)
y_minus_y_mean = val_minus_mean(y, y_mean)

product_of_two = product_of_list(x_minus_x_mean, y_minus_y_mean)

x_minus_x_mean_square = square_of_list(x_minus_x_mean)

# hl3 calculate slope and error from input set 
beta1 = np.sum(product_of_two) / np.sum(x_minus_x_mean_square)
beta0 = round(y_mean - (beta1 * x_mean), 3)

print('Linear equ is (y-cap) : '+str(beta1)+'x + '+str(beta0))

y_predict_initial = lin_equ(beta1, beta0, x)

error_initial = difference_of_list(y, y_predict_initial)

rss_initial = np.sum(square_of_list(error_initial))

cost_function_initial = gen_cost(beta1, x, y)


# hl4 gradient_descent  
gradient_descent_list = calculate_final(beta1, x, y, cost_function_initial)

slopeList=gradient_descent_list['slopeList']
costList=gradient_descent_list['costList']
print("\n\nslopeList : " +str(slopeList))
print("costList : " +str(costList))
plt.scatter(slopeList,costList, color='green')
plt.scatter(beta1,cost_function_initial, color='red')
plt.plot(slopeList,costList)
plt.suptitle('red is dot from equ and others are gradient descent',fontsize=14, fontweight='bold')
plt.title('Red : ('+str(beta1)+','+str(cost_function_initial)+')')
plt.xlabel('slope : '+str(slopeList), fontsize=12)
plt.ylabel('cost : '+str(costList), fontsize=12)
plt.show()
