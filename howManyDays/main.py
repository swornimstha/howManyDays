from datetime import datetime
import sys

currentTime = datetime.now()
inputDate = sys.argv
process = datetime.strptime(inputDate[1], '%Y-%m-%d')

temp = currentTime - process
print("It has been " + str(temp.days) + " days since " + inputDate[1]+".")

