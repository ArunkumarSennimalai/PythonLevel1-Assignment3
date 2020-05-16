class FileOperations:
    def fileReverseLines(self,path):
        f = open(path,'r+')
        k = reversed(f.readlines())
        f.seek(0,0)
        for i in k:
            f.write(i)
    def fileReverseContent(self,path):
        f = open(path,'r+')
        k = reversed(f.readlines())
        f.seek(0,0)
        for i in k:
            f.write(i[::-1])
    def fileread(self,path):
        f = open(path,'r')
        print "\n", f.read()
        
if __name__ =="__main__":
    try:
        obj1 = FileOperations()
        samplefile1_path = "C:\Users\Abcd\Desktop\samplefile1.txt"
        samplefile2_path = "C:\Users\Abcd\Desktop\samplefile2.txt"
        
        #reversing lines
        obj1.fileReverseLines(samplefile1_path)
        #printing the file content after reversing
        obj1.fileread(samplefile1_path)
        
        #reversing entire content
        obj1.fileReverseContent(samplefile2_path)
        #printing the file content after reversing
        obj1.fileread(samplefile2_path)
    
    except IOError:
        print "Please check the file path"
    except Exception as e:
        print e
