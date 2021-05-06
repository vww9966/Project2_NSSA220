from filter_packets import filter
from packet_parser import parse
from compute_metrics import compute
from Packet import Packet

# List of numbers from 1 to 4 to loop over
#loops = list(range(1,5))
loops = [1,2,3,4]

# Resultants list
results = []

for num in loops:
    print('loop ' + str(num))
    
    # Get filtered file from the filter method
    filtered_file = filter(num)

    # List of Packet objects that were parsed
    parsed_packets = []
    parsed_packets = parse(filtered_file, num)

    # Computing with the parsed_packets
    results.append(compute(parsed_packets,num))

print(results)
# Display all results in a csv file based off of saved expected output formatting