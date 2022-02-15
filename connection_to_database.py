from openpyxl import load_workbook


bd = load_workbook('database.xlsx')
for sheet in bd:
    print(sheet.title)
stickers_page = bd['Stickers']
print(stickers_page['A1'].value)