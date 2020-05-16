def fileread(path):
        f = open(path,'r')
        print f.read()
        f.close()
def filewrite(path,content,AppendOrWrite='w'):
        f = open(path,AppendOrWrite)
        f.write(content)
        f.close()
