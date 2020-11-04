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
                    exit()
                try:
                    return colHeaders,rows
                except UnboundLocalError:
                    print("CSVReader.py has returned empty values")
                    return 0,0
    except FileNotFoundError:
           print("File does not exists")
           exit()

def returnLocation(colHeaders,rows,rowNum,colNum):
    try:
        colNumberForNegativeValue = len(colHeaders)+(colNum-1)
        rowNumberForNegativeValue = len(rows)+rowNum
        if rowNum==1 or rowNum == -(len(rows)+1):
            if colNum<0:
                return colHeaders[colNumberForNegativeValue],rowNum,colNumberForNegativeValue
            else:
                return colHeaders[colNum-1]
        else:
            if rowNum <0 and colNum >0:
                values =rows[rowNumberForNegativeValue]
                return values[colNum-1],rowNumberForNegativeValue+2,colNum
            elif colNum <0  and rowNum>0:
                values =rows[rowNum-2]
                return values[colNumberForNegativeValue],rowNum,colNumberForNegativeValue+1
            elif rowNum <0 and colNum <0:
                values =rows[rowNumberForNegativeValue]
                return values[colNumberForNegativeValue],rowNumberForNegativeValue+2,colNumberForNegativeValue+1
            else:
                values =rows[rowNum-2]
                return values[colNum-1]
    except IndexError:
        print("Value does not exists may be file is empty in CSV Reader.py")
        exit()
