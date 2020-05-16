def biggestDict(dict1,dict2,dict3):
    biggestDict = dict2
    if cmp(dict1,dict2):
        biggestDict = dict1
    if cmp(dict3,biggestDict):
        biggestDict = dict3
    return biggestDict

def addToDict(tempdict,key,val):
    tempdict[key] = val #dict2['l'] = 12
    
def addDictToAnotherDict(tempdict1,tempdict2):
    tempdict1.update(tempdict2) #dict1.update({'j':10,'k':11})

def findLength(tempdict):
    return len(tempdict)
    
def convertToStringAndConcatenate(dict1,dict2,dict3):
    return str(dict1) + str(dict2) + json.dumps(dict3) #str(dict3)
