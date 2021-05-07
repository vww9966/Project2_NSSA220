# Rick Wallert, Mark Holloway, Vaughn Woerpel
# packet_parser
# Specs: Parse packet information based off of the filtered packet information

from Packet import Packet

# filtered_file - the name of the filtered packet file
# num - the number of the node
def parse(filtered_file, num) :
	# Create a list of parsed packets to return
	parsed_packets = []


	# Start reading from the file
	f = open(filtered_file)
	line = f.readline()

	# Loop over every line
	while line:
		# Split the line data over whitespace
		line_data = line.split()

		# Create a new list of proper formatting
		data_formatted = []

		# Check to make sure the packet isn't unreachable (length of 10)
		if len(line_data) != 10:
			for i in range(1,6):
				data_formatted.append(line_data[i])

			# Add the type, seq, and ttl
			temp_type = line_data[8]
			temp_seq = line_data[10]
			temp_ttl = line_data[11]

			# Cut out the ttl to just the number
			temp_ttl = temp_ttl[4:]

			# Cut out unnecessary info from the seq
			end=temp_seq.index('/')
			temp_seq = temp_seq[4:end]

			# Add this info to the formatted data
			data_formatted.append(temp_type)
			data_formatted.append(temp_seq)
			data_formatted.append(temp_ttl)

			# Add that it's not unreachable
			data_formatted.append(False)

			# Remove the ICMP item in data_formatted
			data_formatted.remove("ICMP")

			# Create a temp Packet object and add it to the parsed_packets list
			temp_packet_object = Packet(data_formatted[0], data_formatted[1], data_formatted[2], data_formatted[4], data_formatted[3], data_formatted[5], data_formatted[6], data_formatted[7])
			parsed_packets.append(temp_packet_object)

		# Read in the next line
		line = f.readline()

	# return the parsed_packets
	return parsed_packets