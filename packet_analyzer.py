from filter_packets import filter
from packet_parser import *
from compute_metrics import *
from Packet import Packet

# List of numbers from 1 to 4 to loop over
loops = list(range(1,5))

# Resultants list
results = []

for num in loops:
    print('loop ' + str(num))
    
    # Get filtered file from the filter method
    filtered_file = filter(num)

    # List of Packet objects that were parsed
    parsed_packets = []
    parsed_packets = parse(filtered_file)

    # Computing with the parsed_packets
    results.append(compute(parsed_packets))

test = Packet("0.00", "192.168.1.1", "192.168.2.1", "reply", "72", "14", "240")

print(test.source)