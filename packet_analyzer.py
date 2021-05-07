from filter_packets import filter
from packet_parser import parse
from compute_metrics import compute
from Packet import Packet

import csv

# List of numbers from 1 to 4 to loop over
#loops = list(range(1,5))
loops = [1,2,3,4]

# Resultants list
results = []

for num in loops:
    # Get filtered file from the filter method
    filtered_file = filter(num)

    # List of Packet objects that were parsed
    parsed_packets = []
    parsed_packets = parse(filtered_file, num)

    # Computing with the parsed_packets
    results.append(compute(parsed_packets,num))

print(results)
# Display all results in a csv file based off of saved expected output formatting
with open('output.csv', 'w', newline='') as file:
    # Create a csv file writer using the csv import
    writer = csv.writer(file)
    
    # Loop over every item in the results list (each item being a differing node) using the loops variable from earlier
    for num in loops:
        # Write the node name
        writer.writerow(["Node " + str(num)])

        # Empty line
        writer.writerow([])

        # First four metrics
        writer.writerow(["Echo Requests Sent","Echo Requests Received","Echo Replies Sent","Echo Replies Received"])
        writer.writerow([str(results[num-1][0]), str(results[num-1][1]), str(results[num-1][2]), str(results[num-1][3])])

        # Next two metrics
        writer.writerow(["Echo Request Bytes Sent (bytes)","Echo Request Data Sent (bytes)"])
        writer.writerow([str(results[num-1][4]), str(results[num-1][5])])

        # Next two metrics
        writer.writerow(["Echo Request Bytes Received (bytes)","Echo Request Data Received (bytes)"])
        writer.writerow([str(results[num-1][6]), str(results[num-1][7])])

        # Empty line
        writer.writerow([])

        # Average RTT
        writer.writerow(["Average RTT (milliseconds)", str(results[num-1][8])])

        # Throughput
        writer.writerow(["Echo Request Throughput (kB/sec)", str(results[num-1][9])])

        # Goodput
        writer.writerow(["Echo Request Goodput (kB/sec)", str(results[num-1][10])])

        # Reply delay
        writer.writerow(["Average Reply Delay (microseconds)", str(results[num-1][11])])

        # Hop count
        writer.writerow(["Average Echo Request Hop Count", str(results[num-1][12])])

        # Add an extra empty line if it's not the last input
        if num != 4:
            writer.writerow([])