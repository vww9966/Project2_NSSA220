from filter_packets import *
from packet_parser import *
from compute_metrics import *
from Packet import Packet

filter()
parse()
compute()

test = Packet("0.00", "192.168.1.1", "192.168.2.1", "reply", "72", "14", "240")

print(test.source)