

import os, glob
import re, vie_parser
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
instr_name_re = re.compile(config ['DEFAULT'] ['InstrNameRegex']) 
#path = os.path.join(os.getcwd(), 'Files to parse') #path to folder with TD-style VIE .xlsx sheets

#ToD0 - add glob to walk through files; determine how to parse standard files (or just bruteforce through everything that might look like tag number)











# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of 2.1.07 VIE list Mycom.xlsx')
path = os.path.join(os.getcwd(), 'Files to parse\\Copy of 3.1.02 VIE FMEA list for Outdoor Purifiers.xlsx') 
# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of Splice test VIE list.xls') 
# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of p1323v0_vmtfV&I.xls')
# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of p1309v0_Stand3V&IList-LHC.xls') #FCV500A-3  
# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of p2617v1_VTS-2 VIE List TID-N-633.xlsx')
# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of 10.  TID-N-358 - VIE List for Midway Kinney Pump Skid.xlsx') 
# path = os.path.join(os.getcwd(), 'Files to parse\\Copy of 11.  TID-N-359 - VIE List for Midway Kinney Pump System.xlsx') #two names

# for name in vie_parser(instr_name_re, path):
# 	print (str(name) + '\n')

for name in vie_parser.flatten(vie_parser.parse(instr_name_re, path)):
	print (name)
# f = open ('Prefixes.txt', 'w+') #to save new instrumentation names




#Files = glob.glob("./Files to parse/*.xlsx") + glob.glob("./Files to parse/*.xls")
# for file in Files: