from __future__ import print_function
import os
import time
from myInputs import _Getch
import sqlite3
from sets import Set
def openDatabase(database):
	myHistory = sqlite3.connect(database)
	cursor = myHistory.execute("SELECT url from urls;")
	return cursor
def extracturl(raw_url):
	url = ''
	for i in raw_url:
		if i == '/':
			break
		else:
			url += i
	if url[:4] == 'www.':
		return url
	else:
		return 'www.' + url

def saveIntoFile(filename,cursor):
	updatedFile = open(filename,'w')
	urls = {}
	sexWords = []
	for i in cursor:
		flag = False
		for sexWord in sexWords:
			if sexWord in i[0]:
				flag = True
		if flag:
			continue
		if(i[0][:5] == 'https'):
			if extracturl(i[0][8:40]) not in urls.keys():
				# updatedFile.write(extracturl(i[8:40]) + '\n')
				urls[extracturl(i[0][8:40])] = 1
			else:
				urls[extracturl(i[0][8:40])] += 1
			continue
		if(i[0][:4] == 'http'):
			if extracturl(i[0][7:40]) not in urls:
				# updatedFile.write(extracturl(i[7:40])+'\n')
				urls[extracturl(i[0][7:40])] = 1
			else:
				urls[extracturl(i[0][7:40])] += 1
	sortedList = sorted(urls,key=urls.__getitem__, reverse = True)
	for key in sortedList:
		updatedFile.write(key)
		for i in range(80 - len(key)):
			if i >= (40-len(key)) and i<(70-len(key)):
				updatedFile.write('-')
			elif i == (70-len(key)):
				updatedFile.write('>')
			else:
				updatedFile.write(' ')
		updatedFile.write(str(urls[key]) + '\n')
	updatedFile.close()

os.system('clear')
print ("Enter location of database of your browser history")
database = 'History'
print ("Filename where you want to save your history")
filename = 'updatedFile'
print ("\n\nProcessing....\n\n")
cursor = openDatabase(database)
saveIntoFile(filename,cursor)
print ("\n\nProcess completed")
print ("\n\nHistory saved successfully:)\n\n")