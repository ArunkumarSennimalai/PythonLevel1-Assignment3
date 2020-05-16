import math
class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2
    def sqrt(self,num1):
        return math.sqrt(num1)
        
class StringOperation:
    def listofSubstr(self,tempstr1,delimiter):
        return tempstr1.split(delimiter)

if __name__ == '__main__':
    try:
        num1 = int(input("Enter number1"))
        num2 = int(input("Enter number2"))
        
        obj1 = Calculator()
        sumvalue =  obj1.add(num1,num2)
        print "add of two numbers is",sumvalue
        difference = obj1.sub(num1,num2)
        print "sub of two numbers is",difference
        product = obj1.mul(num1,num2)
        print "mul of two numbers is",product
        div = obj1.div(num1,num2)
        print "div of two numbers is",div
        squareroot = obj1.sqrt(num1)
        print "Square root of",num1,"is",squareroot
        
        str1 = "Pack: My: Box: With: Good: Food"
        delimiter = ':'
        list1 = StringOperation().listofSubstr(str1,delimiter)
        print list1
    except ValueError:
        print "Enter only int values"
    except Exception as e:
        print e
