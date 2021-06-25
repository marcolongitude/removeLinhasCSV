import pandas as pd

# path = '/home/marco/Documentos/errors.csv'

path = input('Digite o caminho do arquivo csv: ')
colName = input('Digite a coluna que será gravada: ')

dataFile = pd.read_csv('/home/marco/Documentos/errors.csv', encoding='utf-8', delimiter=',')

stringPositionOne = dataFile[colName].str.split(r'\\n').str[0]
stringPositionTwo = dataFile[colName].str.split(r'\\n').str[1]

dataSpreadsheet = stringPositionOne + ' -> ' + stringPositionTwo

dataSpreadsheetUniq = dataSpreadsheet.drop_duplicates()

dataSpreadsheetUniq.to_csv('errorsLinesUniq.csv', encoding='utf-8', index=False)

print(dataSpreadsheetUniq)
