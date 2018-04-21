#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import binascii
from extractor import Reader
from mutator import Mutator

FUZZ_FACTOR=50.0

PCAP_LOCATION='./test.pcap'
radamsa_bin="/usr/bin/radamsa"

clients_list=[]
servers_list=[]
pkts_list=[]

VERBOSE=False

def main():
    global VERBOSE
    parser=argparse.ArgumentParser(description="Simple PCAP fuzzer based on radamsa mutation engine")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-D",required=True, action="store", dest="dest", help="Destionation host to fuzz application on")
    requiredNamed.add_argument("-P",required=True, action="store", dest="port", help="Destionation port to fuzz application on")
    requiredNamed.add_argument("-S",required=True, action="store", dest="source", help="Sorce host to fuzz messages from")
    requiredNamed.add_argument("-f",required=True, action="store", dest="file", help="Input pcap file")
    requiredNamed.add_argument("-z",required=True, action="store", dest="fuzz", help="fuzz factor between 0 and 100")
    requiredNamed.add_argument("-l",required=True, action="store", dest="layer", help="packet layer to fuzz")
    parser.add_argument("-v","--verbose", dest="verbose", action="store_true", help="verbose output")
    opts=parser.parse_args()

    if opts.dest:
        DEST=opts.dest

    if opts.source:
        SOURCE=opts.source

    if opts.port:
        PORT=opts.port

    if opts.file:
        FILE=opts.file

    if opts.fuzz:
        FUZZ=float(opts.fuzz)

    if opts.layer:
        LAYER=opts.layer
        assert isinstance(LAYER,str), "layer must be specified as layer in scapy's syntax"
        
    if opts.verbose:
        VERBOSE=opts.verbose

    reader=Reader(FILE, LAYER, FUZZ)

    # Cients and Servers are lists
    clients, servers = reader.get_cparts()
    
    if VERBOSE:
        for idx, elem in enumerate(clients):
            print "Client %s - %s" % (idx, elem) 

        for idx, elem in enumerate(servers):
            print "Server %s - %s" % (idx, elem) 

    # Grab mutable packets out of pcap with specified layer
    mutable_packets=reader.extract_mutable_packets()

    m=Mutator(DEST,PORT,LAYER)



    if VERBOSE: print u"\033[1;32m\u2714 Found %s mutable packets (factor %s)\033[0m" % (len(mutable_packets),FUZZ)
    
    if VERBOSE:
        for idx, p in enumerate(mutable_packets):
            print "%s -> %s" % (idx, type(p))
            print "%s -> %s" % (idx, binascii.hexlify(p.load))
            print "MUT: %s -> %s" % (idx, binascii.hexlify(m.prepare_payload(p.load)))

    for idx, p in enumerate(mutable_packets):
        print "%s" % (p.load)

if __name__ == '__main__':
    main()