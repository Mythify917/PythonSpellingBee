from openpyxl import Workbook
import requests
import json

workbook = Workbook()
sheet = workbook.active



sheet['A1'] = "----Words----"
sheet['B1'] = "----Definitions----"
sheet['C1'] = "----Part Of Speech----"

with open('count.json', 'r') as f:
    count = json.load(f)

while True:    

    word = input("Enter a word:\n")
    data = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}').json()

    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    part_of_speech = data[0]['meanings'][0]['partOfSpeech']

    sheet[f"A{count}"] = word
    sheet[f"B{count}"] = definition
    sheet[f"C{count}"] = part_of_speech

    workbook.save(filename="any_word.xlsx")
    count += 1

    with open('count.json', 'w') as f:
        json.dump(count, f, indent=4)


    
