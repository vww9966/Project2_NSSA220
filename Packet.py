# Rick Wallert, Mark Holloway, Vaughn Woerpel
# Packet
# Specs: Packet dataclass for simple storage of individual packet information

from dataclasses import dataclass

@dataclass
class Packet(object):
    # Class for individual packet information

    # Cast the type of all the information just to make sure no strange casting happens while working
    time : str
    source : str
    dest : str
    packet_type : str
    packet_length : str
    seq : str
    ttl : str


    def __init__(self, time, source, dest, packet_type, packet_length, seq, ttl):
        self.time = time
        self.source = source
        self.dest = dest
        self.packet_type = packet_type
        self.packet_length = packet_length
        self.seq = seq
        self.ttl = ttl
