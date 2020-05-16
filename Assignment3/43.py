def search(studentnamelist,name):
    for index in range(len(studentnamelist)):
        if studentnamelist[index] == name:
            return index
    return -1

def printFoundIndex(index):
    if index == -1:
        print "Element not found"
    else:
        print "Element found at index", index


if __name__ == "__main__":
    try:
        studentnamelist = ['Abinesh','Aravindhan','Karthikeyan','ClintonAntony','Jofus','Balaji',"Narayanan",'Bhuvanesh','Kannan','Logesh','Deepan']    
        name = input("Enter the name to be searched: ")
        index = search(studentnamelist,name)
        printFoundIndex(index)
    except Exception as e:
        print e
