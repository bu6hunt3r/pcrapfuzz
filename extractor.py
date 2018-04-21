import scapy.all as scapy
import random
import time

"""
Should contain method able to return mutable packets
"""
class Reader():
    def __init__(self, path, layer, factor):
        self.original_packet_list=[]
        self.mutable_packet_list=[]
        self.server_list=[]
        self.client_list=[]
        self.layer=layer
        self._pcap_path=path
        self.factor=factor
        assert isinstance(self.factor,float), "factor is not float instance"
        random.seed(time.time())
    
    def read_in(self):
        packets=scapy.rdpcap(self._pcap_path)
        return packets

    def get_cparts(self):
        for pkt in self.read_in():
            self.client_list.append(pkt['IP'].sprintf("%IP.src%"))
            self.server_list.append(pkt['IP'].sprintf("%IP.dst%"))
        
        return (set(self.client_list),set(self.server_list))

    def extract_mutable_packets(self):
        """
        Retiurns tuple including (idx, packet) containing mutable packets
        """
        pkts=scapy.rdpcap(self._pcap_path)
        for pkt in pkts:
            if pkt.haslayer(self.layer) and (random.random() < self.factor / 100):
                self.mutable_packet_list.append(pkt[self.layer])
        
        return self.mutable_packet_list