import csv
import os


def createFile(fileName):
        with open(fileName,"w",newline="") as f:
            mywriter = csv.writer(f)
            mywriter.writerow(["Task", "Status"])  # Header
            f.close()



def getAllRows(fileName):
    currdat =[]
    with open (fileName,"r") as f:
        reader  = csv.DictReader(f)
        for row in reader:
            currdat.append(row)
        f.close()
    return currdat
        
def writecsv(fileName,datatowrite):
    currdat = getAllRows(fileName)
    noduplicate = [item for item in datatowrite if item not in currdat]
    with open(fileName,'a+') as f:
        mywrite = csv.DictWriter(f,fieldnames=["Task", "Status"])
        mywrite.writerows(noduplicate)
        f.close()

def findtheIndex(fileName,findData):
    currdat = getAllRows(fileName)
    with open(fileName,"r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            currdat.append(row)
        f.close()     
    index = -1
    searchkey = "Task"
    searchValue = findData[searchkey]
    print(searchValue)
    for i, items in enumerate(currdat):
        print(items)
        if searchkey in items and items[searchkey] == searchValue:
            index = i
            break
    return index

def updatetheTask(fileName,newdata):
    currdat = getAllRows(fileName)
    indextochange = findtheIndex(fileName,newdata)
    valuetochange= newdata["Status"]
    print(valuetochange)
    print(indextochange)
    if indextochange != -1 :
        currdat[indextochange]["Status"] = valuetochange
        createFile(fileName)
        writecsv(fileName,currdat)
    else:
         print(f"{fileName} does not has {newdata}")       

def addnewTask(filename,newtas):
    currdat = getAllRows(fileName)
    currdat.append(newtas)
    writecsv(fileName,currdat)

fileName = "sampl1.csv"
createFile(fileName)
datatow = [{"Task":"learn python","Status":"pending"},{"Task":"Selenium","Status":"complete"},{"Task":"selenium with python","Status":"pending"}]
writecsv(fileName,datatow)   
updatetheTask(fileName,{"Task":"Selenium","Status":"New"})
addnewTask(fileName,{"Task":"Selenium1","Status":"New"})
            