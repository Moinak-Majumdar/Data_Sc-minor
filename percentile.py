# linear search function
def linear_search (arr, data) :
    count = 0
    for elm in arr :
        if(data == elm) :
            return count
        else : 
            count += 1
    return -1
# count elements in list
def len_of_arr(arr) :
    count = 0
    for elm in arr :
        count += 1
    return count

no_of_input = int(input('Enter no of data to be collected : '))

data_set =[]
for elm in range(0, no_of_input) :
    data = int(input('Enter data for index '+str(elm+1)+' : '))
    data_set.append(data)

val = int(input('\nEnter value to find percentile : '))
index = linear_search(data_set, val)
if(index == -1) :
    print('Value %d is not present in data set.' %val)
else :
    len = len_of_arr(data_set)
    n = index + 1
    m = n / len
    p = m * 100
    print('\nPercentile of '+str(val)+' is : %d'%p)