class FileOperations:
    def readFile(self,path):
        try:
            f = open(path,"r")
            f.write("Hello") #IOError
            try:
                print int(f.read(5)) #value error
            except ValueError:
                print "Can't convert values to expected datatype"
        except IOError:
            print "InputOutputException Occurred"
        finally:
            f.close()
            
if __name__ =="__main__":
    try:
       path = "C:\Users\priya\Desktop\samplefile.txt"
       FileOperations().readFile(path)
    except Exception as e:
            print e
