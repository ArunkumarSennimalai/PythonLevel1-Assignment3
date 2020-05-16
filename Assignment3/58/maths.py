from calc import add,subtract,floordiv,modulus,squareroot

if __name__ =="__main__":
    try:
        val1 = input('Enter Value1: ')
        val2 = input('Enter Value2: ')

        sumVal = add(val1,val2)
        subVal = subtract(val1,val2)
        floordivVal = floordiv(val1,val2)
        sqrtval = squareroot(val1)
        modVal = modulus(val1,val2)
        print(sumVal,subVal,floordivVal,sqrtval,modVal),

    except ArithmeticError:
        print "Arithmetic Exception occurred"
    except Exception as e:
        print e
