class VersionError(Exception):
	pass

class AlreadyImportedError(VersionError):
	pass

def select(versions, optionsRequired=False):
	pass

def ensureMinimal(minVersion, optionsRequired=False):
	pass

def checkInstalled(versions, optionsRequired=False):
	return True

def getInstalled():
	return "wxPython"

