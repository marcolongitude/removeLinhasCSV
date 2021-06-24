import pandas as pd

path = '/home/marco/Documentos/errors.csv'

dataFile = pd.read_csv('/home/marco/Documentos/errors.csv', encoding='utf-8', delimiter=',')

stringPositionOne = dataFile['erro'].str.split(r'\\n').str[0]
stringPositionTwo = dataFile['erro'].str.split(r'\\n').str[1]

dataSpreadsheet = stringPositionOne + ' -> ' + stringPositionTwo

dataSpreadsheetUniq = dataSpreadsheet.drop_duplicates()

dataSpreadsheetUniq.to_csv('errorsLinesUniq.csv', encoding='utf-8', index=False)

print(dataSpreadsheetUniq)
