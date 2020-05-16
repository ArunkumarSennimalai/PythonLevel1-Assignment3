from filepackage import *

if __name__ =="__main__":
    try:
        samplefile1_path = "C:\Users\Abcd\Desktop\samplefile1.txt"
        samplefile2_path = "C:\Users\Abcd\Desktop\samplefile2.txt"
        
        #reversing lines
        fileReverseLines(samplefile1_path)
        #printing the file content after reversing
        fileread(samplefile1_path)
        
        #reversing entire content
        fileReverseContent(samplefile2_path)
        #printing the file content after reversing
        fileread(samplefile2_path)


        #write 
        quotes = "aaaaa\nbbbbb\nccccc\nddddd\neeeee"
        filewrite(samplefile1_path,quotes,"w")

        #append
        additionalquotes = "\nffffff\ngggggg\nhhhhhh\niiiiii"
        filewrite(samplefile1_path,additionalquotes,"a")
        
        fileread(samplefile1_path)
    
    except IOError:
        print "Please check the file path"
    except Exception as e:
        print e
