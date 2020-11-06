from fileStorage import FileStorage

fileStorage = FileStorage()
while True:
	print('')
	fileName = input("Retrieving File's Name: ")
	try:
		info = fileStorage.retrieve_from_name(fileName)
		print('\n'+ info)
	except:
		print('\nNot a Valid File!')
	