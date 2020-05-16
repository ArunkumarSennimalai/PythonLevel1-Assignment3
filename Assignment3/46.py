class operationOnNumbers:
    def biggest(self,a=22,b=54,c=100,d=16):
        if a>b and a>c and a>d:
            return a
        elif b>c and b>d:
            return b
        elif c>d:
            return c
        return d

if __name__ == '__main__':
    try:
        num1 = int(input("Enter number1"))
        num2 = int(input("Enter number2"))
        num3 = int(input("Enter number3"))
        num4 = int(input("Enter number4"))

        obj1 = operationOnNumbers()
        #a - required arguments
        maxnum = obj1.biggest(num1,num2,num3,num4)
        print maxnum
        #b - default arguments
        maxnum = obj1.biggest()
        print maxnum
    except ValueError:
        print "Enter only int values"
    except Exception as e:
        print e
