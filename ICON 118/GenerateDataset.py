import openpyxl
import random
import pandas as pd

def almenoUnoZero(val1=-1, val2=-1, val3=-1, val4=-1, val5=-1, val6=-1):
    trovato = False

    if(val1 == 0 or val2== 0 or val3 == 0 or val4 == 0 or val5 == 0 or val6 == 0):
        trovato = True

    return trovato

def fillDataset(path):
    xfile = openpyxl.load_workbook(path)
    sheet = xfile['Sheet1']

    patologia = 'A'
    cosciente = 'B'
    lesioni = 'C'
    respiro = 'D'
    dolToracico = 'E'
    emorragia = 'F'
    ustione = 'G'
    codice = 'H'


    countWhite = 0
    row = 2

    while(countWhite < 10):
        cell = patologia+str(row)
        sheet[cell] = countWhite

        cell = cosciente+str(row)
        sheet[cell] = 0

        cell = lesioni+str(row)
        sheet[cell] = 0

        cell = respiro+str(row)
        sheet[cell] = 0

        cell = dolToracico+str(row)
        sheet[cell] = 0

        cell = emorragia+str(row)
        sheet[cell] = 0

        cell = ustione+str(row)
        sheet[cell] = 0

        cell = codice+str(row)
        sheet[cell] = 0

        row = row + 1
        countWhite = countWhite + 1

    countGreen = 0
    while(countGreen < 114):
        les = random.randint(0, 1)
        doltor = random.randint(0, 1)
        emorr = random.randint(0, 1)
        ust = random.randint(0, 1)

        if(not(les == 1 and doltor == 1 and emorr == 1 and ust == 1)
        and not(les == 0 and doltor == 1 and emorr == 1 and ust == 1)
        and not(les == 1 and doltor == 0 and emorr == 1 and ust == 1)
        and not(les == 1 and doltor == 1 and emorr == 0 and ust == 1)
        and not(les == 1 and doltor == 1 and emorr == 1 and ust == 0)):
            cell = patologia+str(row)
            sheet[cell] = random.randint(0, 9)

            cell = cosciente+str(row)
            sheet[cell] = 0

            cell = lesioni+str(row)
            sheet[cell] = les

            cell = respiro+str(row)
            sheet[cell] = 0

            cell = dolToracico+str(row)
            sheet[cell] = doltor

            cell = emorragia+str(row)
            sheet[cell] = emorr

            cell = ustione+str(row)
            sheet[cell] = ust

            cell = codice+str(row)
            sheet[cell] = 1

            countGreen += 1
            row += 1

    countYellow = 0
    while(countYellow < 430):
        les = random.randint(0, 2)
        resp = random.randint(0, 1)
        doltor = random.randint(0, 1)
        emorr = random.randint(0, 1)
        ust = random.randint(0, 2)

        if(not(les == 0 and resp == 0 and doltor == 0 and emorr == 0 and ust == 0)
        and not(les == 0 and resp == 0 and doltor == 0 and emorr == 0 and ust == 1)
        and not(les == 0 and resp == 0 and doltor == 0 and emorr == 1 and ust == 0)
        and not(les == 0 and resp == 0 and doltor == 1 and emorr == 0 and ust == 0)
        and not(les == 0 and resp == 1 and doltor == 0 and emorr == 0 and ust == 0)
        and not(les == 1 and resp == 0 and doltor == 0 and emorr == 0 and ust == 0)
        and not(les == 0 and resp == 0 and doltor == 0 and emorr == 1 and ust == 1)
        and not(les == 0 and resp == 0 and doltor == 1 and emorr == 0 and ust == 1)
        and not(les == 0 and resp == 1 and doltor == 0 and emorr == 0 and ust == 1)
        and not(les == 1 and resp == 0 and doltor == 0 and emorr == 0 and ust == 1)
        and not(les == 0 and resp == 0 and doltor == 1 and emorr == 1 and ust == 0)
        and not(les == 0 and resp == 1 and doltor == 0 and emorr == 1 and ust == 0)
        and not(les == 1 and resp == 0 and doltor == 0 and emorr == 1 and ust == 0)
        and not(les == 0 and resp == 1 and doltor == 1 and emorr == 0 and ust == 0)
        and not(les == 1 and resp == 0 and doltor == 1 and emorr == 0 and ust == 0)
        and not(les == 1 and resp == 1 and doltor == 0 and emorr == 0 and ust == 0)):
            cell = patologia+str(row)
            sheet[cell] = random.randint(0, 9)

            cell = cosciente+str(row)
            sheet[cell] = 0

            cell = lesioni+str(row)
            sheet[cell] = les

            cell = respiro+str(row)
            sheet[cell] = 0

            cell = dolToracico+str(row)
            sheet[cell] = doltor

            cell = emorragia+str(row)
            sheet[cell] = emorr

            cell = ustione+str(row)
            sheet[cell] = ust

            cell = codice+str(row)
            sheet[cell] = 2

            countYellow += 1
            row += 1

    countRed = 0
    while(countRed < 2200):
        cos = random.randint(0, 1)
        les = random.randint(0, 3)
        resp = random.randint(0, 2)
        doltor = random.randint(0, 1)
        emorr = random.randint(0, 1)
        ust = random.randint(0, 2)

        if(not(les == 0 and resp == 0 and doltor == 0 and emorr == 0 and ust == 0)
        and not(les == 0 and resp == 0 and doltor == 0 and emorr == 0 and ust == 1)
        and not(les == 0 and resp == 0 and doltor == 0 and emorr == 1 and ust == 0)
        and not(les == 0 and resp == 0 and doltor == 1 and emorr == 0 and ust == 0)
        and not(les == 0 and resp == 1 and doltor == 0 and emorr == 0 and ust == 0)
        and not(les == 1 and resp == 0 and doltor == 0 and emorr == 0 and ust == 0)
        and not(les == 0 and resp == 0 and doltor == 0 and emorr == 1 and ust == 1)
        and not(les == 0 and resp == 0 and doltor == 1 and emorr == 0 and ust == 1)
        and not(les == 0 and resp == 1 and doltor == 0 and emorr == 0 and ust == 1)
        and not(les == 1 and resp == 0 and doltor == 0 and emorr == 0 and ust == 1)
        and not(les == 0 and resp == 0 and doltor == 1 and emorr == 1 and ust == 0)
        and not(les == 0 and resp == 1 and doltor == 0 and emorr == 1 and ust == 0)
        and not(les == 1 and resp == 0 and doltor == 0 and emorr == 1 and ust == 0)
        and not(les == 0 and resp == 1 and doltor == 1 and emorr == 0 and ust == 0)
        and not(les == 1 and resp == 0 and doltor == 1 and emorr == 0 and ust == 0)
        and not(les == 1 and resp == 1 and doltor == 0 and emorr == 0 and ust == 0)
        and not((les>=1 and les <= 2) and almenoUnoZero(resp,doltor,emorr,ust) == True)
        and not((ust>=1 and ust <= 2) and almenoUnoZero(resp,doltor,emorr,les) == True)
        and not(resp == 2 and almenoUnoZero(ust,doltor,emorr,les) == True)):
            cell = patologia + str(row)
            sheet[cell] = random.randint(0, 9)

            cell = cosciente + str(row)
            sheet[cell] = 0

            cell = lesioni + str(row)
            sheet[cell] = les

            cell = respiro + str(row)
            sheet[cell] = 0

            cell = dolToracico + str(row)
            sheet[cell] = doltor

            cell = emorragia + str(row)
            sheet[cell] = emorr

            cell = ustione + str(row)
            sheet[cell] = ust

            cell = codice + str(row)
            sheet[cell] = 3

            countRed += 1
            row += 1

    xfile.save(path)
def xlsxTocsv(xlsxFilePath, csvFilePath):
    read_file = pd.read_excel(xlsxFilePath)
    read_file.to_csv(csvFilePath, index=None, header=True)

#fillDataset('C:/Users/39333/PycharmProjects/ICON vero/resources/datasetICON.xlsx')
#xlsxTocsv('C:/Users/39333/PycharmProjects/ICON vero/resources/datasetICON.xlsx','C:/Users/39333/PycharmProjects/ICON vero/resources/datasetICON.csv')
print('Done!')