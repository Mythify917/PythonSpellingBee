from openpyxl import Workbook
import requests

workbook = Workbook()
sheet = workbook.active

spellingbeefile = open('spellingbeewords.txt').read().split()

sheet['A1'] = "----Words----"
sheet['B1'] = "----Defs----"
count = 2
for word in spellingbeefile:
    data = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}').json()
    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
    except:
        definition = "None"
    sheet[f'A{count}'] = word
    sheet[f'B{count}'] = definition
    count += 1

workbook.save(filename="spellingbee_excel.xlsx")