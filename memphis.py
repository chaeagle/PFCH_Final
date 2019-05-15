### code written by Charlotte Eagle and reusable under MIT license ###

import csv
import json

wells = {

}

#opens CSV to parse, data taking from ashtracker part of the Environmental Integrity Project
with open ("memphis.csv", "r") as data: 
 	reader = csv.reader(data) 	
 	next(reader, None)

#defines the data
 	for row in reader:
 		facility = row [2]
 		well_name = row[6]
 		well_latitude = row[8]
 		well_longitude = row[9]
 		contaminant = row[11]
 		concentration = row[14]
 		limit = row[16].lower()
 		detection = row[13].lower()
 		collection_date = row[10]

 		well_id = str(facility + well_name)

#establishes dictionary structure for JSON
 		if well_id not in wells:
 			wells[well_id] = {
 				"2010" : [],
 				"2011" : [],
 				"2012" : [],
 				"2013" : [],
 				"2014" : [],
 				"2015" : [],
 				"2016" : [],
 				"2017" : [],
 				"latitude" : well_latitude,
 				"longitude": well_longitude,
 			}

 		year = collection_date[0:4]
 		#print(year)

#find coordinates for each well for overall mapping excel for tableau 
 		# print(well_name, well_latitude, well_longitude)

#this "if" statement defines which wells are contaminated
 		if limit == "true" and detection =="false":
 		 	wells[well_id][year].append({ "contaminant" : contaminant, "concentration" : concentration})
 		else:
 			pass

#print(wells)

with open ("memphis.json", "w") as write_file:
	json.dump(wells, write_file, indent = 2)
	print ("the Memphis JSON is Ready")