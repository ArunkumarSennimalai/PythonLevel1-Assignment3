from dictionarypackage import biggestDict,findLength,concatenateDict,updateDict,printDict
if __name__ == "__main__":
    try:
        dict1 ={'Name':'Ramakrishna','Age':25}
        dict2={'EmpId':1234,'Salary':5000} 
        dict3 = {'g':7,'h':8,'i':9}
        
        #finding biggest dict
        biggest = biggestDict(dict1,dict2,dict3)
        print "biggest dict is ", biggest
        
    
        #printing length
        dict1_len = findLength(dict1)
        print "length of",dict1,"is",dict1_len
        dict2_len = findLength(dict2)
        print "length of",dict2,"is",dict2_len
        dict3_len = findLength(dict3)
        print "length of",dict3,"is",dict3_len
        
        
        #concatenate
        concatenateDict(dict1,dict2)
        print dict1
        
        #updateage to 26
        updateDict(dict1,'Age',26)
        print dict1
        
        #print elements in dict
        printDict(dict1)
       
    except Exception as e:
        print(e)


