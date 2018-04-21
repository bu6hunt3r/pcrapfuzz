import scapy.all as scapy
from socket import AF_INET, SOCK_STREAM
from radamsa import mutate

class Mutator():
    def __init__(self,dest,port,layer):
        self._dst=dest
        self._port=port
        self._layer=layer
    
    def prepare_payload(self, payload):
        _payload=mutate(payload)
        return _payload
    
    def prepare_packet(self, pkt, payload):
        p=pkt[self._layer]
        p.payload=self.prepare_payload(payload)
        return p
    
    def send_packet(self, pkt):
        print type(p)

    

        
