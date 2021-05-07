# Rick Wallert, Mark Holloway, Vaughn Woerpel
# filter_packets
# Specs: Filter node packets based off of the type

# num - the number of node being analyzed
def filter(num):
	# Create the file names for reading and writing
	file="Node" + str(num) + ".txt"
	writefile="Node" + str(num) + "_filtered.txt"

	# Call the readfile method to filter the input
	readfile(file, writefile)

	# Return the name of the filtered file
	return writefile

def readfile(filename, writefile):
	# Open the proper file
	f = open(filename)

	# Open the writing file
	fw = open(writefile, 'w')

	# Read in the first line
	line = f.readline()

	# Loop over every line in the file
	while line:
		# Check if it's an ICMP message
		if("ICMP" in line):
			fw.write(line)
		
		# Read in the next line
		line = f.readline()

	# Close the files since we're done with all that
	f.close()
	fw.close()