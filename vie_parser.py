###Python module for parsing .XLS/.XLSX files
###


import xlrd
import re

 
def instr_name_parser(regex,Name): 
#Parses a name against regex describing instrumentation name
#Takes regex (predetermined, probably won't change), Instrumentation name (single, with no excess information or symbols)
#Returns tuple of tuples
	assert isinstance(Name, str), "Name is not a string: %r" % Name #Check to see if name is a string or a list
	assert type(regex) is re._pattern_type, "regex is wrong type: %r" % regex
	matched = regex.match(Name)
	if matched:
		if len(matched.group("prefix")) > 0:
			prefix = tuple(filter(None, re.split('\W', str(matched.group("prefix")))))
		else:
			prefix = None
		if matched.group("suffix"):
			suffix = tuple(filter(None, re.split('\W', str(matched.group("suffix")))))
		else:
			suffix = None
		basename = matched.group("basename")
		number = matched.group("number")
		return (prefix, basename, number, suffix)
	return None



def parse(regex, Path_to_file):
	#Returns a list of tuples, containing parsed instrumentation names
	book = xlrd.open_workbook(Path_to_file)
	filename_re = re.compile(r'[/\\]([^/\\]*)[.]xlsx?$')
	print("Analyzing data from VIE list \"{}\"...\n".format(filename_re.search(Path_to_file).group(1)))
	Parsed_names = []
	for sheet in book.sheets():
		for col_num in range(sheet.ncols):
			Parsed_names_temp = [instr_name_parser(regex, str(x)) for x in sheet.col_values(col_num) if instr_name_parser(regex, str(x))]
			if len(Parsed_names_temp) > len(Parsed_names):
				Parsed_names = Parsed_names_temp
				if __name__ == '__main__':
					for cell in sheet.col_values(col_num): #for debug purposes only. when finished uncomment the if statement below
						print (str(cell)+'   ->   '+str(instr_name_parser(regex, str(cell))))
	return Parsed_names


def flatten(Parsed_names):
	assert type(Parsed_names) == list
	assert type (Parsed_names[0]) == tuple
	Flat_prefix_names = []
	for name in Parsed_names:
		if name[0]:
			for prefix in name[0]:
				flat_name = prefix+'-'+name[2]
				if name[3]:
					Flat_prefix_names.append(flat_name+'-'+'-'.join(name[3]))
		if name[3]:
			Flat_prefix_names.append(name[1]+'-'+name[2]+'-'+'-'.join(name[3]))
		else:
			Flat_prefix_names.append(name[1]+'-'+name[2])

	return Flat_prefix_names



def main ():
	print('Testing regex')
	Names_y = ['PI-1710', 'PT/PS/PI-1313', 'JXE\n1226', 'PSV-1725-(1)', 'PSV-1-2', 'PSE_1 12', 'TE-4 O', 'TCV-4_H', 'ZSH/ZSHI-138-G', 'HV-666-Alt', 'MV-999-B6-3', 'YCV/YIC/YY-1458-EF', 'TT-2442-X2', 'YI-1446-CD/YLH/YLL', 'JXE-1337-A/X', 'TE-TLA3A', 'FCV500A-3']
	Names_n = ['-1HV1734', 'PSV-B']

	import configparser
	config = configparser.ConfigParser()
	config.read('config.ini')
	instr_name_re = re.compile(config ['DEFAULT'] ['InstrNameRegex']) 

	# for name in Names_y:
	# 	print(name + '   ->   ' + str(instr_name_parser(instr_name_re, name)))
	# 	print ('\n')
	# for name in Names_n:
	# 	print(name + '   ->   ' + str(instr_name_parser(instr_name_re, name)))

	import os
	path = os.path.join(os.getcwd(), 'Files to parse\\Copy of p1309v0_Stand3V&IList-LHC.xls') #FCV500A-3  
	# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of 2.1.07 VIE list Mycom.xlsx')
	Parsed_list = parse(instr_name_re, path)
	print('\n'*3)
	print (flatten(Parsed_list))


if __name__ == "__main__":
	main()