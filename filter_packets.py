# Rick Wallert, Mark Holloway, Vaughn Woerpel
# filter_packets
# Specs: Filter node packets based off of the type

# num - the number of node being analyzed
def filter(num):
	print('called filter function in filter_packets.py')

	# Create the file names for reading and writing
	file="Node" + str(num) + ".txt"
	writefile="Node" + str(num) + "_filtered.txt"

	# Call the readfile method to filter the input
	readfile(file, writefile)

	# Return the name of the filtered file
	return writefile

def readfile(filename, writefile):
	f = open(filename)
	fw = open(writefile, 'a')
	line = f.readline()
	while line:
		line = f.readline()
		if("ICMP" in line):
			fw.write(line)
	
	f.close()
	fw.close()