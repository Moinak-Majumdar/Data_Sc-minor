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

print('\n\nPlease enter following conditions to find result.\n')
# table for outLook
outLook = input('\n OutLook : ')
outLookY = conditionalProbability('outLook', outLook, 'play', 'yes', posCount)
outLookN = conditionalProbability('outLook', outLook, 'play', 'no', negCount)

# table for temperature
temperature = input('\n Temperature : ')
temperatureY = conditionalProbability('temperature', temperature, 'play', 'yes', posCount)
temperatureN = conditionalProbability('temperature', temperature, 'play', 'no', negCount)

# table for humidity
humidity = input('\n Humidity : ')
humidityY = conditionalProbability('humidity', humidity, 'play', 'yes', posCount)
humidityN = conditionalProbability('humidity', humidity, 'play', 'no', negCount)

# table for wind
wind = input('\n Wind : ')
windY = conditionalProbability('wind', wind, 'play', 'yes', posCount)
windN = conditionalProbability('wind', wind, 'play', 'no', negCount)

vnbN = PofNegCount * outLookN * temperatureN * humidityN * windN
vnbY = PofPosCount * outLookY * temperatureY * humidityY * windY

if(vnbY > vnbN) :
    print('\n Under this condition it is playable !!\n')
else :
    print('\n Under this condition it is Not Playable !!\n')