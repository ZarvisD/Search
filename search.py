import os
import re
filename=""
read_data=2**24     #Amount of data to be read in each loop
searchtext="text_to_search" 
he=searchtext.encode('hex')   #Converting data to hex
with open(filename, 'rb') as f:
	while True:
		data= f.read(read_data)
		if not data:
			break
		elif searchtext in data:
			print "Found"
		else:
			continue
