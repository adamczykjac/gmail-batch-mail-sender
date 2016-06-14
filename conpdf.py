#!/usr/bin/env python

#Skrypt dla Marcina

# from os import listdir
from subprocess import call
from os import listdir, mkdir
from os.path import isfile, join
import re

pathToVariablePdfsFolder = './var-pdfs'
pathToStaticPdfsFolder = './static-pdfs'
pathToResultFolder = './out/'
pdfFilenameToGenerate = 'MAdamczyk-Internship documents.pdf'
pdfTkOutputArgs = []

# Delete possibly existing files in ./out folder
call(['rm', '-rf', 'out/*'])

# Get all the static PDF names to generate
staticPdfs = [f for f in listdir(pathToStaticPdfsFolder) if isfile(join(pathToStaticPdfsFolder, f))]
print 'Static Pdfs to merge: \n'
for s in staticPdfs:
	pdfTkOutputArgs.append(pathToStaticPdfsFolder + '/' + s)
	print s
print '\n'

# Get all the variable PDF names to generate
varPdfs = [f for f in listdir(pathToVariablePdfsFolder) if isfile(join(pathToVariablePdfsFolder, f))]
for v in varPdfs:
	number = re.search('(?<=\.)(.*?)(?=\.)', v).group(0)
	path = pathToResultFolder + number
	mkdir( path, 0755 );
	pdfTkArgs = [pathToStaticPdfsFolder + '/' + 'logo.pdf'] + \
				[pathToVariablePdfsFolder + '/' + v] + \
				[pathToStaticPdfsFolder + '/' + 'resume.pdf'] + \
				[pathToStaticPdfsFolder + '/' + 'worksamples.pdf'] + \
				['cat'] + \
				['output', path + \
				'/' + \
				pdfFilenameToGenerate]
	# Create array with arguments for pdftk
	print 'Calling Pdftk with the following arguments: '
	print pdfTkArgs
	call(['pdftk'] + pdfTkArgs)

print 'Done.'
