# Rick Wallert, Mark Holloway, Vaughn Woerpel
# packet_parser
# Specs: Parse packet information based off of the filtered packet information

from Packet import Packet

# filtered_file - the name of the filtered packet file
# num - the number of the node
def parse(filtered_file, num) :
	print('called parse function in packet_parser.py')

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

		# if the list length is 10, then it's a destination unreachable
		# otherwise, it's a normal one
		if len(line_data) == 10:
			# Add the already properly formatted data
			for i in range(0,6):
				data_formatted.append(line_data[i])

			# Check if it's a request or a reply based off of the source
			current_node = ""

			# Set the IP based off of the node num (num) variable
			if num == 1:
				current_node = "192.168.100.1"
			elif num == 2:
				current_node = "192.168.100.2"
			elif num == 3:
				current_node = "192.168.200.1"
			else:
				current_node = "192.168.200.2"

			# Check to see if the unreachable ping is a request or reply
			# if the source (data_formatted[2]) does not equal the current_node (Host IP), then it's a reply
			# else, it's a request
			if data_formatted[2] != current_node:
				data_formatted.append("reply")
			else:
				data_formatted.append("request")

			# Add the boolean saying it's unreachable
			data_formatted.append(True)

			temp_packet_object = Packet(data_formatted[1], data_formatted[2], data_formatted[3], data_formatted[-2], data_formatted[-3], 'none', 'none', data_formatted[-1])
			parsed_packets.append(temp_packet_object)

		# Read in the next line
		line = f.readline()

	# outside loop


	# return the parsed_packets
	return parsed_packets