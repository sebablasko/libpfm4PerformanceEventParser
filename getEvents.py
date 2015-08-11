import sys
import json

def morphEventCode(code):
	return "r"+code[2:]

if(len(sys.argv)<2):
	print "Error. Uso: ./getEvents.py archivoAProcesar"
	exit()

archivo = sys.argv[1]

with open(archivo) as data_file:
	events = json.load(data_file)

allEvents = []

for event in events:
	for code in event["Codes"]:
		if code not in allEvents:
			allEvents.append(code)

for val in allEvents:
	print morphEventCode(val)+",",
