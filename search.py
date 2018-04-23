import os
import re
filename="filename.dmp"
read_data=2**24
searchtext="bd:mongo:"
he=searchtext.encode('hex')
with open(filename, 'rb') as f:
	while True:
		data= f.read(read_data)
		if not data:
			break
		elif searchtext in data:
			print "Found"
			try:
				offset=hex(data.index(searchtext))
				print offset
			except ValueError:
				print 'Not Found'						
		else:
			continue
