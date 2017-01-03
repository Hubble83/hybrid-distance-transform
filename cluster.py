#!/usr/bin/python
import os, sys, subprocess
from datetime import datetime

def createInputImg (dim):
	print "\nGenerating", dim+"*"+dim, "input image"
	filename = "inpbm/" + dim + ".pbm"
	file = open(filename, 'w')
	n = int(dim)
	m = int(dim)
	file.write("P1\n")
	file.write(dim + " " + dim + "\n")
	quarter = n/4
	quarter2 = m/4
	for i in range(0, n):
		for j in range(0, m):
			if(j>=quarter2 and j<(m-quarter2) and i>=quarter and i<(n-quarter)):
				if(j==m-1):
					file.write("0\n")
				else:
					file.write("0 ")
			else:
				if(j==m-1):
					file.write("1\n")
				else:
					file.write("1 ")
	file.close()


images = ["16384"]#["512","1024","2048","4096","8192","16384"]
processes = ["2"]#["1","2","4","8","16","32","64"]#,"40","64","80"]
comunications = {"alltoall_one":"0"}#{"alltoall":"0","alltoall_swaps":"1","scatter":"2","alltoall_many":"3"}
nreps = 1
mode = "2"
measures=["INIT","READ","P1","COMUNICATE","P2","WRITE"]

resFolder = "results/"
inFolder = "inpbm/"
outFolder = "outpgm/"


d=datetime.now()
tables = resFolder + str(d.hour)+"-"+str(d.minute)+"-"+str(d.second) + ".csv" 

if not os.path.exists(resFolder):
	os.makedirs(resFolder)
if not os.path.exists(inFolder):
	os.makedirs(inFolder)
if not os.path.exists(outFolder):
	os.makedirs(outFolder)
for img in images:
	if not os.path.exists(img):
		createInputImg(img)

sys.exit(0)

f = open(tables,"w") 

total = len(comunications)*len(images)*len(processes)*nreps
count = 1

os.system( "make delete && make" )
	
if os.path.exists("executable"):

	for com, num in comunications.items():
		print "com:",com,
		f.write("\n\nTable:,"+com+"\n,")
		for proc in processes:
			f.write(proc)
			for ms in measures:
				f.write(",")
		f.write("\n")
		for proc in processes:
			for ms in measures:
				f.write(","+ms)

		for img in images:
			print "img:",img
			f.write("\n"+img)

			for proc in processes:
				print "proc",proc
				times=[ [] for ms in measures]

				for rep in range(nreps):
					print count, "of", total
					count+=1

					if len(sys.argv) > 1 and sys.argv[1]=="fast":
						cOutput = "none"
						cInput = "none"
					else:
						cOutput = outFolder+"com-"+com+"_dim-"+img+"_proc-"+proc+"_rep-"+str(rep)+".pgm"
						cInput = inFolder+img+".pbm"
					
					execution = subprocess.Popen( 
						#mpirun -np 18 --mca btl sm,self,tcp,openib 
						["mpirun", "-q", "-np", proc, "--map-by","core","--mca", "btl", "sm,self,tcp,openib", "executable",
							"-m", mode,
							"-i", cInput, 
							"-o", cOutput,
							"-c", num
						],
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE
					) 
					execution.wait()
					t = execution.stdout.read().decode("ascii").strip()
					curr = t.split(" ")
					for i in range ( len(measures) ):
						times[i].append(curr[i])
					os.system(" rm -rf outpgm/* ")
				for t in times:
					t.sort()
					f.write( ","+str(t[nreps/2]) )
f.close()