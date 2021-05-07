# Rick Wallert, Mark Holloway, Vaughn Woerpel
# compute_metrics
# Specs: Compute packet information based off of the parsed info

from Packet import Packet

# --- Results key ---
# 0  Num. requests sent
# 1  Num. request received
# 2  Num. replies sent
# 3  Num. replies received
# 4  Total frame echo bytes sent
# 5  Total frame echo bytes received
# 6  Total echo data bytes sent
# 7  Total echo data bytes received
# 8  Average ping round trip time
# 9  Echo request throughput kB/s
# 10 Echo request goodput
# 11 Average reply delay
# 12 Average num. of hops per echo request

# Store all of the possible node ip's
nodeip=["192.168.100.1","192.168.100.2","192.168.200.1","192.168.200.2"]

# parsed_packets - a list of all the parsed packets to be computed
# node - the current node number (1,2,3, or 4)
def compute(parsed_packets,node) :
	# List of results to be returned
	results = [0,0,0,0,0,0,0,0,0,0,0,0,0]

	# Helper variables for calculations
	rttsum=0
	replydelay=0
	rtttotal=0
	replydelaytotal=0
	hopcountsum=0
	totalpackets=0
	previous_packet=None

	# Loop through every parsed packet object
	for packet in parsed_packets:
		# Calculate Requests sent/received
		if 'request' in packet.packet_type:
			if nodeip[node-1]==packet.source:
				results[0]+=1
			else:
				results[1]+=1
		if 'reply' in packet.packet_type:
			if nodeip[node-1]==packet.source:
				results[2]+=1
			else:
				results[3]+=1
		
		# Calculate Frame and payload bytes
		if nodeip[node-1]==packet.source:
			# Frame
			results[4]+=int(packet.packet_length)
			# Payload
			results[6]+=(int(packet.packet_length)-20)
		else:
			# Frame
			results[5]+=int(packet.packet_length)
			# Payload
			results[7]+=(int(packet.packet_length)-20)

		# Calculate Ping RTT + Ping reply delay
		if previous_packet is not None and packet.seq in previous_packet.seq:
			if packet.source==nodeip[node-1]:
				rttsum+=(float(packet.time)-float(previous_packet.time))
				rtttotal+=1
			else:
				replydelay+=(float(packet.time)-float(previous_packet.time))
				replydelaytotal+=1

		# Calculate Average hops count
		if packet.ttl != '128':
			hopcountsum+=3
		else:
			hopcountsum+=1
		totalpackets+=1

		previous_packet=packet

	# Calculate Average RTT
	results[8]=(rttsum/rtttotal)*1000
	
	# Calculate Echo request throughput
	results[9]=float((results[4]/1000)/rttsum)

	# Calculate Echo request goodput
	results[10]=float((results[6]/1000)/rttsum)	

	# Calculate Reply delay
	results[11]=(replydelay/replydelaytotal)*1000000

	# Calculate Average number of hops per echo request
	results[12]=float(hopcountsum/totalpackets)

	# return this list of results
	return results