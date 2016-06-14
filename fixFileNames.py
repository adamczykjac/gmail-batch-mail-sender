#!/usr/bin/env python

#Skrypt dla Marcina

# from os import listdir
from subprocess import call
from os import listdir, rename
from os.path import isfile, join
import re

pathToVariablePdfsFolder = './var-pdfs'

# Get all the variable PDF names to generate
varPdfs = [f for f in listdir(pathToVariablePdfsFolder) if isfile(join(pathToVariablePdfsFolder, f))]
for v in varPdfs:
	number = int(re.search('(?<=\.)(.*?)(?=\.)', v).group(0))
	if number < 100 and number >= 10:
		filNumber = '0' + str(number)
		newName = 'c.' + filNumber + '.pdf'
		rename(pathToVariablePdfsFolder + '/' + v, pathToVariablePdfsFolder + '/' + newName)
	elif number < 10:
		filNumber = '00' + str(number)
		newName = 'c.' + filNumber + '.pdf'
		rename(pathToVariablePdfsFolder + '/' + v, pathToVariablePdfsFolder + '/' + newName)
print 'Done.'