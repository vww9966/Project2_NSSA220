# Rick Wallert, Mark Holloway, Vaughn Woerpel
# compute_metrics
# Specs: Compute packet information based off of the parsed info

from Packet import Packet

# --- Results key ---
#	Num. requests sent
#	Num. request received
#	Num. replies sent
#	Num. replies received
#	Total frame echo bytes sent
#	Total frame echo bytes received
#	Total echo data bytes sent
#	Total echo data bytes received
#	Average ping round trip time
#	Echo request throughput kB/s
#	Echo request goodput
#	Average reply delay
#	Average num. of hops per echo request


# parsed_packets - a list of all the parsed packets to be computed
def compute(parsed_packets) :
	print('called compute function in compute_metrics.py')

	
	# List of results to be returned
	results = [0,0,0,0,0,0,0,0,0,0,0,0,0]


	for packet in parsed_packets:
		if 'reply' in packet.packet_type:
			results[0]+=1
	
	# return the results
	return results



