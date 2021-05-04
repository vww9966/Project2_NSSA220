# Rick Wallert, Mark Holloway, Vaughn Woerpel
# filter_packets
# Specs: Filter node packets based off of the type

file="Node1.txt"
writefile="Node1_ICMP.txt"
def filter():
	print('called filter function in filter_packets.py')
	readfile(file)

def readfile(filename):
	f = open(filename)
	fw = open(writefile, 'a')
	line = f.readline()
	while line:
		line = f.readline()
		if("ICMP" in line):
			fw.write(line)
	
	f.close()
	fw.close()

filter()