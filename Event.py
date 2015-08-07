import pprint

class Event(object):
	"""docstring for Event"""

	def __init__(self):
		self.umasks = []
		self.registro = {}

	def setName(self, name):
		self.name = name

	def setPMU(self, PMUName):
		self.PMU = PMUName

	def setIDX(self, id):
		self.IDX = id

	def setDesc(self, desc):
		self.description = desc

	def setCode(self, code):
		self.code = code

	def addUmask(self, umask):
		self.umasks.append(umask)

	def hasUmasks(self):
		return len(self.umasks)>0

	def addRegistro(self, reg, description):
		if reg not in self.registro:
			self.registro[reg] = description
		else:
			self.registro[reg] = self.registro[reg] + "; " + description

	def addAttribute(self, line):
		key = line.split(":")[0].strip()
		if "IDX" in key:
			self.setIDX(line.split(":")[1].strip())
		if "PMU" in key:
			self.setPMU(line.split(":")[1].strip())
		if "Name" in key:
			self.setName(line.split(":")[1].strip())
		if "Desc" in key:
			self.setDesc(line.split(":")[1].strip())
		if "Code" in key:
			self.setCode(line.split(":")[1].strip())
		if "Umask" in key:
			self.addUmask(line.replace("\n",""))

	def toJSON(self):
		ret = "{"
		ret += "'IDX' : '" + self.IDX + "', \n"
		ret += "'PMU name' : '" + self.PMU + "', \n"
		ret += "'Name' : '" + self.name + "', \n"
		ret += "'Description' : '" + self.description + "', \n"
		ret += "'Codes' : " + str(pprint.pformat(self.registro, width=1)) + " \n"
		ret += "}"
		return ret

	def __str__(self):
		ret = ""
		ret += "Name:\t" + self.name+"\n"
		ret += "PMU:\t" + self.PMU+"\n"
		ret += "IDX:\t" + self.IDX+"\n"
		ret += "Desc:\t" + self.description+"\n"
		ret += "Code:\t" + self.code+"\n"
		ret += "Umasks:\t" + str(self.umasks)+"\n"
		ret += "Registro:\t" + str(self.registro)
		return ret