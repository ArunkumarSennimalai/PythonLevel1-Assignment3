class ArithmeticOperations:
    def div(self,num1,num2):
        try:
            return num1/num2
        except ArithmeticError:
            print "Arithemtic Exception occurred"
        
if __name__ =="__main__":
    try:
        ArithmeticOperations().div(12,0)
        result += 10
    except NameError:
        print "Name does not exists"
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as e:
        print e
    else:
        print "Executed error free"
    finally:
        print "End of the program"
