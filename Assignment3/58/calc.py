def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  return x / y
def floordiv(x,y):
    return x // y
def squareroot(x):
  return x ** 0.5
def modulus(x,y):
    return x % y
def isPrime(num):
    i=2
    while((i*i)<=num):
        if(num%i==0):
            return False
        i += 1
    return True

def fib(x):
    a,b=0,1
    while(x>0):
        print (a),
        c = a+b
        a=b
        b=c
        x-=1

