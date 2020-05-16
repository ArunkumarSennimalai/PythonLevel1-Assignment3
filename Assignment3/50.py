class FileOperations:
    def fileread(self,path):
        f = open(path,'r')
        while True:
            c = f.read(10)
            if not c:
                break
            print c
            print "Current Position=",f.tell(),"\n"

        f.close()

    def read_N_charsOnly(self,path,n):
        f = open(path,'r')
        print f.read(100)
        f.seek(0,0)

    def printFromNthLine(self,path,lineno):
        f = open(path,'r')
        for line in range(lineno-1):
            f.readline()
        print f.read()


if __name__ =="__main__":
    try:
        obj1 = FileOperations()
        
        obj1.fileread("C:\Users\priya\Desktop\samplefile.txt")
        obj1.read_N_charsOnly("C:\Users\priya\Desktop\samplefile.txt",100)
        obj1.printFromNthLine("C:\Users\priya\Desktop\samplefile.txt",5)
        
    except IOError:
        print "Please check the file path"
    except Exception as e:
        print e
