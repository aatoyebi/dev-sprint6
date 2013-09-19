# This is where chapter 14 exercises go.
import urllib

zip_entry = raw_input("Please enter your zipcode:\n")

zip_open = urllib.urlopen("http://uszip.com/zip/" + zip_entry)
for line in zip_open:
	if "Population" in line:
		print line
	if "Longitude" in line:
		print line	
	if "Latitude" in line:
		print line

zip_open.close()		
	
