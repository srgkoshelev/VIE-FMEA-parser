import xlrd
import os

def split_names (List,Separators): #One time function: Splits combinations like PT/PI to ["PT", "PI"] given the separator
	assert isinstance(List,list), "List should be a list"
	assert isinstance(Separators,list) or (isinstance(Separators,str) and len(Separators) == 1), "Separators should be a list or single character separator"
	Separator = Separators[0]
	temp = []
	result = []
	for item in List:
		if Separator in item:
			temp.append(item.split(Separator))
		else:
			result.append(item)
	for item in temp:
		result = result + item
	if len(Separators) == 1: #Separator must be 1 symbol, e.g. '/', '\n'
		return result
	else: 
		return split_names(result, Separators[1:])


#path = os.path.abspath(os.dirname)
path = os.path.join(os.getcwd(), 'Files to parse') #The file is not there anyway. I got the prefixes previously, now they are ready to use
print (path)



book = xlrd.open_workbook(path+"\Additional files\FMEA_&_VIE_spreadsheet.xlsx")
sh = book.sheet_by_index(0)
table = []
for col_num in range (sh.ncols):
	buf = []
	for row_num in range (sh.nrows):
		if sh.cell_type(row_num,col_num) == 0: #empty string check
			buf.append("")
		elif sh.cell_type(row_num,col_num) == 1: #text string
			buf.append(sh.cell_value(row_num,col_num))
		elif sh.cell_type(row_num,col_num) == 2: #number
			buf.append('{:.0g}'.format(sh.cell_value(row_num,col_num)))
	table.append(buf)

names = table[0]
names = list(set(split_names(names,['/', '\n'])))
names.sort()
names = [x for x in names if x != '???' and len(x) < 8]
print(names)



# #Saving list of used prefixes
# f = open ('Prefixes.txt', 'w+')
# f.write(",".join(names)+'\n')
# f.close

