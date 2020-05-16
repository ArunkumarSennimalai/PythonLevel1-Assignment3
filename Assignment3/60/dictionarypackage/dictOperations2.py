def concatenateDict(tempdict1,tempdict2):
    tempdict1.update(tempdict2)

def updateDictSalary(tempdict1,Salary,percentageIncrease):
    tempdict1['Salary'] = int(tempdict1['Salary']*(1+(percentageIncrease/100.0)))

def updateDict(tempdict1,key,value):
    tempdict1[key] = value

def printDict(tempdict1):
    for key,values in tempdict1.items():
        print key,"=",values
    #delete 'Age'
    
def deleteElement(tempdict1,key):
    del(tempdict1[key])
