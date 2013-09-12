# This is where chapter 14 exercises go.
import urllib



zip_entry = raw_input("Please enter your zipcode:\n")

zip_open = urllib.urlopen("http://uszip.com/zip/" + zip_entry)
for line in zip_open:
	pop = "Total population"
	tname = zip_entry +  "is the zip code for"
	if pop in line:
		print line
	elif tname in line:
		print line	
	
