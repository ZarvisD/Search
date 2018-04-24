import os
import re
filename="filename.dmp"
read_data=2**24
offset=0
chunk_start=0
searchtext=b"text or hex to search"
search_length=len(searchtext)
overlap_length = search_length - 1 
he=searchtext.encode('hex')
with open(filename, 'rb') as f:
	while True:
		data= f.read(read_data)
		if not data:
			break
		while True:
			offset=data.find(searchtext,offset)
			# print chunk_start
			# print offset
			if offset < 0:
				break
			s=f.tell()
			# print "Found at",hex(chunk_start+offset)
			f.seek(chunk_start+offset+10)
			datas=f.read(15)
			print "[+] Password Extracted"
			print "[+] "+ datas
			offset+=search_length
			f.seek(s)

		chunk_start += len(data)  #this is done to set the calculate the address of new find str by previous_read_data+offset
		data=data[read_data:]     #Discarding all the old data
		offset=0				  #Setting offset to 0.So, as to search in chunk from beginning
