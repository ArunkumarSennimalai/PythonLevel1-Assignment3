class TupleOperation:
    def extendTuple(self,temptuple1,templist1):
        return temptuple1  + tuple(templist1)

if __name__ == "__main__":
    try:
        tuple1 = (1,2,3,4,5)
        list1 = [6,7,8,9]
        tuple1 = TupleOperation().extendTuple(tuple1,list1)
        print tuple1
    except Exception as e:
        print e
