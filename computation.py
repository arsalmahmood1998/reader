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
    try:
        index = colHeaders.index(colTitle)
    except ValueError:
        print("Given file does not contains this value in for sum")
    sum=0
    try:
        for rows in data:
            sum = sum +int(rows[index])
    except ValueError:
        print("Cannot Convert string to integer for sum")
    return sum

def avg(colHeaders,data,colTitle):
    try:
        sumResult = sum(colHeaders,data,colTitle)
        return (sumResult / len(data))
    except ZeroDivisionError:
        print("Cannot Divide by zero for average")

def minVal(colHeaders,data,colTitle):
    try:
        index = colHeaders.index(colTitle)
    except ValueError:
        print("Given file does not contains this value for min value")
        return 0
    minVal = 99999999999999
    try:
        for rows in data:
            intVal = int (rows[index])
            if  minVal > intVal:
                minVal=intVal
    except ValueError:
        print("Cannot Convert string to integer for min value")
    return minVal

def maxVal(colHeaders,data,colTitle):
    try:
        index = colHeaders.index(colTitle)
    except ValueError:
        print("Given fille does not contains this file for max value")
        return 0
    maxVal = -99999999999999
    try:
        for rows in data:
            intVal = int (rows[index])
            if  maxVal < intVal:
                maxVal=intVal
    except ValueError:
        print("Cannot Convert string to integer for max value")
    return maxVal
