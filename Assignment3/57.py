class FileOperations:
    def fileread(self,path):
        f = open(path,'r')
        print f.read()
        f.close()

if __name__ =="__main__":
    try:
        obj1 = FileOperations()        
        obj1.fileread("C:\Users\Abcd\Desktop\samplefile.txt") #IOError
        a = int('abcd') #ValueError
        b = "df"+34.56 #TypeError
        c += 10 #NameError
        d = 54%0 #ArithmeticError
    except IOError:
        print "Please check the file path"
    except TypeError:
        print "Inappropriate type"
    except ValueError:
        print "Can't convert values to expected datatype"
    except NameError:
        print "Name you specified doesn't exist"
    except ArithmeticError:
        print "Arithmetic Exception occurred"
    except Exception as e:
        print e
