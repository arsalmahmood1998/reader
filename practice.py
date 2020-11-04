def openFile(fileName):
    try:
        with open(fileName) as file:
                listOflines=list(file)
                line=listOflines[0]
                try:
                    colHeaders = line.split(",")
                except ValueError:
                    print("Split function is empty in CSV Reader.py line 8")
                rawRows = listOflines[1:]
                rows=[]
                try:
                    for line in rawRows:
                        row=line.split(",")
                        rows.append(row)
                except ValueError:
                    print("Split function is empty in CSV Reader.py line 14")
                try:
                    return colHeaders,rows
                except UnboundLocalError:
                    print("CSVReader.py has returned empty values")
                    return 0,0
    except FileNotFoundError:
           print("File does not exists")
           exit()

def returnLocation(colHeaders,rows,rowNum,colNum):
    colNumberForNegativeValue = len(colHeaders)+(colNum-1)
    rowNumberForNegativeValue = len(rows)+rowNum
    if rowNum==1 or rowNum == -6:
        if colNum<0:
            return colHeaders[colNumberForNegativeValue],rowNum,colNumberForNegativeValue
        else:
            return colHeaders[colNum-1]
    else:
        if rowNum <0 and colNum >0:
            values =rows[rowNumberForNegativeValue]
            return values[colNum-1],rowNumberForNegativeValue+1,colNum
        elif colNum <0  and rowNum>0:
            values =rows[rowNum-2]
            return values[colNumberForNegativeValue],rowNum,colNumberForNegativeValue+1
        elif rowNum <0 and colNum <0:
            values =rows[rowNumberForNegativeValue]
            return values[colNumberForNegativeValue],rowNumberForNegativeValue+1,colNumberForNegativeValue+1
        else:
            values =rows[rowNum-2]
            return values[colNum-1]

colHeaders,rows = openFile("data2.csv")
print(returnLocation(colHeaders,rows,-6,2))
print(returnLocation(colHeaders,rows,-5,-2))
print(returnLocation(colHeaders,rows,2,-1))
print(returnLocation(colHeaders,rows,3,-3))
print(returnLocation(colHeaders,rows,1,3))
print(returnLocation(colHeaders,rows,0,0))


# id,name,quantity,price,
# 1,phone,23,456,
# 2,drive,12,321,
# 3,mobo,2,567,56,
# 4,casing,29,6,
# 5,psu,9,5675,

# id,name,price,code,
# 1,phone,233,23
# 2,drive,123,45
# 3,mobo,21,34
# 4,casing,299,1
# 5,psu,9,44,0
