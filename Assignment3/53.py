def fileFunctions(samplefile1_path):
            f = open(samplefile1_path, "r+")    
            print "Name of the file: ", f.name  #name     
            f.flush() #flush
            fid = f.fileno() #fileno
            print "File Descriptor: ", fid
            ret = f.isatty() #isatty
            print "Return value : ", ret
            f.seek(0,0) #seek
            line = f.read(10)  #read
            print "Read Line: %s" % (line)
            line = f.readline() #readline
            print "Read Line: %s" % (line)
            content = f.readlines(5) #readlines
            print "Read Lines: %s" % (content)
            pos = f.tell() #tell
            print "Current Position: %d" % (pos)
            f.truncate() #truncate
            line = f.readline()
            print "Read Line after truncate: %s" % (line)
            f.seek(0, 2)
            line = f.write("Hello") #write
            f.seek(0, 3)
            line = f.writelines("Welcome to python programming") #writelines
            f.seek(0,0)
            for index in range(3):
               line = f.next()   #next
               print "Line No %d - %s" % (index, line)
            f.close()
if __name__ =="__main__":
    try:
        samplefile1_path = "C:\Users\Abcd\Desktop\samplefile.txt"
        fileFunctions(samplefile1_path)
    except IOError as e:
        print e
    except Exception as e:
        print e
