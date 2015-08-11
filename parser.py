import sys
import json
import subprocess
from Event import Event

def getRecord(EventName, umaskMName=None):
	command = libpfm4Path+"./check_events "+EventName
	if(umaskMName!=None):
		command += ":"+umaskMName

	proceso = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	codigo = proceso.stdout.readlines()[-1].split(":")[1].replace("\n","").strip()
	retval = proceso.wait()
	return codigo

		
if(len(sys.argv)<2):
	print "Error. Uso: ./parser.py pathTo<./check_events>Fromlibpfm4"
	exit()


pattern="#-----------------------------"

registro = None
listaEventos = []

libpfm4Path = sys.argv[1]

# 1.- Generar archivo fuente con los eventos disponibles del SO
filename = "allEvents.txt"
archivo = open(filename, 'w')
command = libpfm4Path+"./showevtinfo"
proceso = subprocess.Popen(command, stdout=archivo)
proceso.wait()
archivo.close()

# 2.- Coleccionar todos los registros de Eventos disponibles en el archivo de entrada
archivo = open(filename, 'r')
for line in archivo:
	if pattern in line:
		if registro != None:
			listaEventos.append(registro)
		registro = Event()
	else:
		if registro != None:
			registro.addAttribute(line)
listaEventos.append(registro)
archivo.close()

# 3.- Recuperar todos los codigos de evento disponibles para cada Evento con sus distintos umasks
for evento in listaEventos:
	if evento.hasUmasks():
		for umask in evento.umasks:
			umaskName = umask.split(":")[3].strip().replace("[","").replace("]","")
			evento.addRegistro(getRecord(evento.name, umaskName), umask)
	else:
		evento.addRegistro(getRecord(evento.name), evento.description)


# 4.- Imprimir la lista de eventos en formato JSON
print "["
for reg in listaEventos[:-1]:
	print reg.toJSON(), ","
print listaEventos[-1].toJSON()
print "]"