from openpyxl import Workbook
import requests

workbook = Workbook()
sheet = workbook.active

spellingbeefile = open('spellingbeewords.txt').read().split()

sheet['A1'] = "----Words----"
sheet['B1'] = "----Definitions----"
sheet['C1'] = "----Part Of Speech----"
count = 2
for word in spellingbeefile:
    data = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}').json()
    if data['title'] == "No definitions found.":
        definition = "None"
    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
    except IndexError:
        definition = "No definition found."

    try:
        part_of_speech = data[0]['meanings'][0]['partOfSpeech']
    except IndexError:
        part_of_speech = "No part of speech found."

    sheet[f'A{count}'] = word
    sheet[f'B{count}'] = definition
    sheet[f'C{count}'] = part_of_speech
    count += 1

workbook.save(filename="spellingbee_excel.xlsx")