# hl2 this is naive base classification model for the following data set.
import pandas as pd

dataSet = pd.read_excel('NaiveBayes.xlsx').to_dict(orient='records')
print('\nTrained data set :\n')
print(pd.DataFrame(dataSet))


#hl7 goal is to find is it playable on condition like (outlook = sunny, temperature = cool, humidity = high, wind = strong) 

dataCount = len(dataSet);

def count(elm, val) :
    res=0
    for curr in dataSet :
        if(curr[elm] == val) :
            res = res+1
    return res

posCount = count('play', 'yes')
negCount = count('play', 'no')

PofPosCount = posCount/dataCount
PofNegCount = negCount/dataCount

def conditionalProbability(elm, val, conElm, conVal, conCount) :
    count = 0
    for curr in dataSet :
        if(curr[elm] == val and curr[conElm] == conVal) :
            count = count+1
    prob = count / conCount
    return prob

# set of all possible value belongs to data set
outLookSet = []
temperatureSet = []
humiditySet = []
windSet=[]
for curr in dataSet :
    if(outLookSet.count(curr["outLook"]) == 0) :
        outLookSet.append(curr['outLook'])
    if(temperatureSet.count(curr["temperature"]) == 0) :
        temperatureSet.append(curr['temperature'])
    if(humiditySet.count(curr["humidity"]) == 0) :
        humiditySet.append(curr['humidity'])
    if(windSet.count(curr["wind"]) == 0) :
        windSet.append(curr['wind'])


# taking op from user and validating
print('\n\nPlease enter following conditions to find result.\n')

outLook = input('\nOutLook : ')
while(1) :
    if(outLookSet.count(outLook) == 0) :
        print("\nInvalid value for outLook, please enter one from data set : ")
        print(outLookSet)
        outLook = input('\nOutLook : ')
    else :
        break

temperature = input('\nTemperature : ')
while(1) :
    if(temperatureSet.count(temperature) == 0) :
        print("\nInvalid value for temperature, please enter one from data set : ")
        print(temperatureSet)
        temperature = input('\nTemperature : ')
    else :
        break

humidity = input('\nHumidity : ')
while(1) :
    if(humiditySet.count(humidity) == 0) :
        print("\nInvalid value for humidity, please enter one from data set : ")
        print(humiditySet)
        humidity = input('\nHumidity : ')
    else :
        break

wind = input('\nWind : ')
while(1) :
    if(windSet.count(wind) == 0) :
        print("\nInvalid value for wind, please enter one from data set : ")
        print(windSet)
        wind = input('\nWind : ')
    else :
        break

# table for outLook
outLookY = conditionalProbability('outLook', outLook, 'play', 'yes', posCount)
outLookN = conditionalProbability('outLook', outLook, 'play', 'no', negCount)

# table for temperature
temperatureY = conditionalProbability('temperature', temperature, 'play', 'yes', posCount)
temperatureN = conditionalProbability('temperature', temperature, 'play', 'no', negCount)

# table for humidity
humidityY = conditionalProbability('humidity', humidity, 'play', 'yes', posCount)
humidityN = conditionalProbability('humidity', humidity, 'play', 'no', negCount)

# table for wind
windY = conditionalProbability('wind', wind, 'play', 'yes', posCount)
windN = conditionalProbability('wind', wind, 'play', 'no', negCount)

vnbN = PofNegCount * outLookN * temperatureN * humidityN * windN
vnbP = PofPosCount * outLookY * temperatureY * humidityY * windY

if(vnbP > vnbN) :
    print('\n Under this condition it is playable !!\n')
else :
    print('\n Under this condition it is Not Playable !!\n')