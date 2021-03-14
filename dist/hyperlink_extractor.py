import openpyxl

wb = openpyxl.load_workbook('feb check.xlsx')
ws = wb.get_sheet_by_name('Sheet1')
i=2
while i<73:
	print(ws.cell(row=i, column=3).hyperlink.target)
	i+=1
