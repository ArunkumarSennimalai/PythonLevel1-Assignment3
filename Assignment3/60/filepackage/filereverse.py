def fileReverseLines(path):
        f = open(path,'r+')
        k = reversed(f.readlines())
        f.seek(0,0)
        for i in k:
            f.write(i)
def fileReverseContent(path):
        f = open(path,'r+')
        k = reversed(f.readlines())
        f.seek(0,0)
        for i in k:
            f.write(i[::-1])
