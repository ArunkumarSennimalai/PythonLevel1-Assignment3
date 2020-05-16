class FileOperations:
    def fileread(self,path,name):
        f = open(path,'r')
        counter=0
        while True:
            content = f.readline()
            if not content:
                break
            counter += content.count("Treasure")            
        print name , "has" ,counter,"times the word Treasure"
        f.close()

    def checkFiles(self,files_path,files_name):
        for filepath,filename in zip(files_path,files_name):
            self.fileread(filepath,filename)

if __name__ =="__main__":
    try:
        obj1 = FileOperations()
        
        files_path = ["C:\Users\Abcd\Desktop\samplefile.txt","C:\Users\Abcd\Desktop\GK\Wipro\Assignment3\samplefile1.txt","C:\Users\Abcd\Desktop\GK\Wipro\Assignment3\samplefile2.txt","C:\Users\Abcd\Desktop\GK\Wipro\Assignment3\samplefile3.txt"]
        files_name = ["SampleFile1","SampleFile2","SampleFile3","SampleFile4"]
        obj1.checkFiles(files_path,files_name)
        
    except IOError:
        print "Please check the file path"
    except Exception as e:
        print e
