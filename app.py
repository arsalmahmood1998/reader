try:
    import CSVReader
    import computation
except ModuleNotFoundError:
    print("Cannot import file")

try:
    colHeaders,rows = CSVReader.openFile("data.csv")
    print(CSVReader.returnLocation(colHeaders,rows,-7,2))
    print(CSVReader.returnLocation(colHeaders,rows,-5,-2))
    print(CSVReader.returnLocation(colHeaders,rows,2,-1))
    print(CSVReader.returnLocation(colHeaders,rows,-3,-3))
    print(CSVReader.returnLocation(colHeaders,rows,1,3))
    print(computation.selectOperation(colHeaders,rows,"price","add"))
    print(computation.selectOperation(colHeaders,rows,"price","average"))
    print(computation.selectOperation(colHeaders,rows,"id","Min"))
    print(computation.selectOperation(colHeaders,rows,"price","Max"))
except AttributeError:
     print("Function does not exists")
except NameError:
    print("Given  column does not exists")
