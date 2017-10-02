import configparser
config = configparser.ConfigParser()
Regex_string = r"(?P<prefix>(?:[A-Z]{1,3}/){0,3})(?P<basename>[A-Z]{1,4})[- /_\n]?(?P<number>\d{1,4})([-_/(]?(?P<suffix>\w{1,3}([/-]\w{1,3}){0,3}))?\b" #If updated .md needs to be updated as well
config['DEFAULT'] = {'InstrNameRegex':Regex_string}

with open ('config.ini', 'w') as configfile:
	config.write(configfile)
	print ('Config file has been created successfully')


# #Testing how recording works
# config.read('config.ini')
# if config ['DEFAULT'] ['InstrNameRegex'] != Regex_string:
# 	print (config ['DEFAULT'] ['InstrNameRegex'])
# 	print (Regex_string)
# else:
# 	print ("Regex string match!")




