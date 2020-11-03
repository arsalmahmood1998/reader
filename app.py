import CSVReader
import computation

colHeaders,rows = CSVReader.openFile("data.csv")

print(computation.selectOperation(colHeaders,rows,"id","add"))

print(computation.selectOperation(colHeaders,rows,"id","average"))

print(computation.selectOperation(colHeaders,rows,"name","Min"))

colHeaders,rows = CSVReader.openFile("data2.csv")

print(computation.selectOperation(colHeaders,rows,"price","add"))

print(computation.selectOperation(colHeaders,rows,"price","average"))
