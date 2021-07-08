import xlsxwriter
import random

#creates the file and adds a new sheet within the designated excel file
outWorkbook = xlsxwriter.Workbook("3stockdata.xlsx")
outSheet = outWorkbook.add_worksheet()

weights=[]
weights2 = []

for i in range(100):
    value = random.random()
    value2 = 1 - value
    weights.append(value)
    weights2.append(value2)

for i in range(len(weights)):
    outSheet.write(i+18, 9, weights[i])
for i in range(len(weights2)):
    outSheet.write(i+18, 10, weights2[i])

outWorkbook.close()

print("done")

               

    
    



