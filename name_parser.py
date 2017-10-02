import re

####Is not used for .xls parsing. May be deprecated

def name_parser(regex,Name): #Works with a string or a list. If a string - returns cleaned name or None. If list - returns list of names (without Nones) or just None if no matches are found
	#Function to parse instrumentation names, e.g. PT/PI/PS-3113-(A)
	#The inferred convention for the IB-1 names is:
	#Prefix no longer than two groups of additional letter name plus slash sign e.g. YCV/YIC/
	#Base name - 4 letter name of the instrument. Prefix names are also limited to 4 characters
	#Basic separator - most used are - and space " ", although some more exotic will fit as well, e.g. underscore, slash, EOL. No sperator case is also included
	#Instrumentation number - up to 4 digits
	#Suffix separator - similar to basic separator case except for EOL and space.
	#Suffix - at current state regex is more permitting, assuming that one Instrumentation name per match although capabilities to findall through the raw file are present some excess symbols may be matched accidently
	#Suffix - allowable suffixes include up to 2 letters/digits together or separated with a dash, underscore or slash + up to two groups of /XXX (up to three letters). Alternatively suffix "Alt" is allowed. 
	assert isinstance(Name, str) or isinstance(Name, list), "Should be string or a list: %r" % Name #Check to see if name is a string or a list
	assert type(regex) is re._pattern_type, "regex is wrong type: %r" % regex
	if isinstance(Name, list):
		Matched = []
		for name in Name:
			matched = name_parser(regex,name)
			if matched:
				Matched.append(matched)
		return Matched
	else:
		matched = regex.match(Name)
		if matched:
			return matched.group()
			
	return None




#Testing regex
# Names = ['-1HV1734', 'PI-1710', 'PT/PS/PI-1313', 'JXE\n1226', 'PSV-1725-(1)', 'PSV-B',  'PSV-1-2', 'PSE_1 12', 'TE-4 O', 'TCV-4_H', 'ZSH/ZSHI-138-G', 'HV-666-Alt', 'MV-999-B6-3', 'YCV/YIC/YY-1458-EF', 'TT-2442-X2', 'YI-1446-CD/YLH/YLL', 'JXE-1337-A/X']
# name_regex = re.compile(r"(?:[A-Z]{1,3}/){0,2}[A-Z]{1,4}[- /_\n]?\d{1,4}(?:[-_/]?(?:\(\w\)|\w(?:[-_/]?\w)?\b|Alt\b)(?:/[A-Z]{1,3}){0,2})?")
# List_parsed = name_parser(name_regex,Names)
# for name in Names:
# 	print(name_parser(name_regex, name))
# print(List_parsed)



