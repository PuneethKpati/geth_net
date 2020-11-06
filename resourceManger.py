import psutil
import openpyxl
import datetime
import time 

class ResourceManager:
	
	def data_logging(pid):
		currTime = datetime.datetime.now().strftime("%d%m%Y - %H:%M:%S")

		processP = psutil.Process(pid)

		memusage = processP.memory_percent()

		cpuTotal = processP.cpu_percent(interval=2)
		cpuUsage = processP.cpu_percent(interval=2) / psutil.cpu_count()


		resultsXL = openpyxl.load_workbook("./results.xlsx")
		sheet = resultsXL.active 

		sheet.cell(column = 1, row=sheet.max_row +1, value=currTime)
		sheet.cell(column = 2, row=sheet.max_row +1, value=pid)
		sheet.cell(column = 3, row=sheet.max_row +1, value=memusage)
		sheet.cell(column = 4, row=sheet.max_row +1, value=cpuTotal)
		sheet.cell(column = 5, row=sheet.max_row +1, value=cpuUsage)

		print('Entered data: ', currTime, pid, memusage, cpuTotal, cpuUsage)

	def monitor():
		pid = int(input('Process to be monitored: '))

		while True:
			ResourceManager.data_logging(pid)
			time.sleep(5)



