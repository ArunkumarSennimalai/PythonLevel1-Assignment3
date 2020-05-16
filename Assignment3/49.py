class FileOperations:
    def fileread(self,path):
        f = open(path,'r')
        print f.read()
        f.close()

    def filewrite(self,path,content,AppendOrWrite='w'):
        f = open(path,AppendOrWrite)
        f.write(content)
        f.close()

if __name__ =="__main__":
    try:
        samplefile1_path = "C:\Users\priya\Desktop\samplefile.txt"
        obj1 = FileOperations()
        
        obj1.fileread(samplefile1_path)
        
        quotes = "aaaaa\nbbbbb\nccccc\nddddd\neeeee"
        obj1.filewrite(samplefile1_path,quotes,"w")
        
        additionalquotes = "\nffffff\ngggggg\nhhhhhh\niiiiii"
        obj1.filewrite(samplefile1_path,additionalquotes,"a")
        
        obj1.fileread(samplefile1_path)
    except IOError:
        print "Please check the file path"
    except Exception as e:
        print e
