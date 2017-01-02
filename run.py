#!/usr/bin/env python3
import os, subprocess

def htmlStart (f):
	f.write("<!DOCTYPE html>")
	f.write("<html><head><style>")
	f.write("</style></head><body>")

def htmlEnd (f):
	f.write("</body>")
	f.write("</html>")

def htmlTitle (f, title):
	f.write("<h2>"+title+"</h2>")

def htmlText (f, text):
	f.write("<p>"+text+"</p>")

def htmlImgSmall (f, img):
	f.write("<img src={0} height='150' width='150' >".format(img))

def htmlImgBig (f, img):
	f.write("<img src={0} height='278' width='370' >".format(img))


cluster = open("results/clusterResults.txt","r")

filename = "html/results.html"
os.makedirs(os.path.dirname(filename), exist_ok=True)
os.makedirs(os.path.dirname("txt/"), exist_ok=True)
f = open(filename,"w")


d = {1:"Euclidian", 2:"Manhattan", 3:"Chessboard"}

htmlStart( f )

counter=0
lines = cluster.readlines()
tests = []
for i in range ( len( lines ) ):

	dim = 0
	img = ""
	mode = 0

	benchmarks = eval(lines[i])
	for key, value in benchmarks.items():
		if key=="dim" : dim = value
		elif key=="img" : img = value
		elif key=="mode" : mode = value
		elif key not in tests : tests.append( key )

	if i%3 == 0 :
		htmlTitle ( f, "Benchmark with a {0}*{0} image".format( str(dim) ) )
		f.write("<br/>{0}, {1}, {2}:<br/><br/>".format(d[1],d[2],d[3]))

	os.system( "convert results/{0}.pgm html/{0}.svg".format(img[:-4]) )
	htmlImgSmall(f, img[:-4]+".svg")
	if i%3 == 2:
		f.write("<br/>")
		htmlText(f, "Performance measures:")

	for t in tests:
		tmp = open("txt/{0}.txt".format(str(counter)), "w")
		
		for key in sorted( list( benchmarks[t].keys() ) ):
			tmp.write( str(key) + "\t"+ benchmarks[t][key] + "\n" )

		tmp.close()

		if i%3 == 2:
			proc = subprocess.Popen(['gnuplot','-p'], 
			                        shell=True,
			                        stdin=subprocess.PIPE,
			                        stdout=subprocess.PIPE,
			                        stderr=subprocess.PIPE
			                        )
			proc.stdin.write( bytes( "set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 pi -1 ps 1.5\n", "ascii" ) )
			proc.stdin.write( bytes( "set style line 2 lc rgb '#ff4c00' lt 1 lw 2 pt 7 pi -1 ps 1.5\n", "ascii" ) )
			proc.stdin.write( bytes( "set style line 3 lc rgb '#ffc000' lt 1 lw 2 pt 7 pi -1 ps 1.5\n", "ascii" ) )
			proc.stdin.write( bytes( "set autoscale\n", "ascii" ) )
			proc.stdin.write( bytes( "set title 'Benchmark'\n", "ascii" ) )
			proc.stdin.write( bytes( "set xlabel '# of threads'\n", "ascii" ) )
			proc.stdin.write( bytes( "set ylabel '{0}'\n".format(t), "ascii" ) )
			proc.stdin.write( bytes( "set term svg\n", "ascii" ) )
			proc.stdin.write( bytes( "set output 'html/{0}.svg'\n".format( str(counter)), "ascii" ) )
			proc.stdin.write( bytes("plot 'txt/{0}.txt' using 1:2:xtic(1):ytic(2) title 'Euclidean' ls 1 with lp, 'txt/{1}.txt' using 1:2:xtic(1):ytic(2) title 'Manhattan' ls 2 with lp, 'txt/{2}.txt' using 1:2:xtic(1):ytic(2) title 'Chessboard' ls 3 with lp\n".format(counter-(2*len(tests)),counter-(len (tests)),counter), "ascii" ) )
			proc.stdin.write( bytes( "quit\n", "ascii" ) )

			htmlImgBig(f, str(counter)+".svg")
		counter +=1
	if i%3 == 2:
		f.write("<br/><br/>")