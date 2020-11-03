def selectOperation(colHeaders,data,colTitle,operation):
    if operation == "add":
        result = sum(colHeaders,data,colTitle)
        return result
    elif operation == "average":
        result = avg(colHeaders,data,colTitle)
        return result
    elif operation == "Min":
        result = minVal(colHeaders,data,colTitle)
        return result
    elif operation == "Max":
        result = maxVal(colHeaders,data,colTitle)
        return result

def sum(colHeaders,data,colTitle):
    index = colHeaders.index(colTitle)
    sum=0
    try:
        for rows in data:
            sum = sum +int(rows[index])
    except ValueError:
        print("Cannot Convert string to integer")
    return sum

def avg(colHeaders,data,colTitle):
    sumResult = sum(colHeaders,data,colTitle)
    return (sumResult / len(data))

def minVal(colHeaders,data,colTitle):
    index = colHeaders.index(colTitle)
    minVal = 99999999999999
    try:
        for rows in data:
            intVal = int (rows[index])
            if  minVal > intVal:
                minVal=intVal
    except ValueError:
        print("Cannot Convert string to integer")
    return minVal

def maxVal(colHeaders,data,colTitle):
    index = colHeaders.index(colTitle)
    maxVal = -99999999999999
    try:
        for rows in data:
            intVal = int (rows[index])
            if  maxVal < intVal:
                maxVal=intVal
    except ValueError:
        print("Cannot Convert string to integer")
    return maxVal
