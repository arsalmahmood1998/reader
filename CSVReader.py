def openFile(fileName):
    with open(fileName) as file:
        listOflines=list(file)
        line=listOflines[0]
        colHeaders = line.split(",")
        rawRows = listOflines[1:]
        rows=[]
        for line in rawRows:
            row=line.split(",")
            rows.append(row)
    return colHeaders,rows
