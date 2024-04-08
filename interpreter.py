import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	datas=data.split(";")
	for n in datas:
		srun(n)
	
def sline(argvs):
	f1= open (argvs,"r+")
	for n in f1:
		if n!="":
			if n!="\n":
				scommand(n)
				
	f1.close()
	
print("\x1bc\x1b[44;37m")	
if sys.argv[1]!="":
	sline(sys.argv[1])
