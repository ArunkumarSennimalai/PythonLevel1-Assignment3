from listpackage import popElement,search,binarysearch
        
if __name__ =="__main__":
    try:
       list1 = [1,2,'abcd',5,7,'xyz',3.4,True,False,2.3,6.5,'a']
       list2 = [2,4,6,7,9,12,13,15,17,20,23,25]
       print search(list1,"abcd")
       print binarysearch(list2,7)
       popElement(list1)
    except Exception as e:
        print e
