#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

VERBOSE=True

FUZZ_FACTOR=50.0

PCAP_LOCATION='./test.pcap'
radamsa_bin="/usr/bin/radamsa"

clients_list=[]
servers_list=[]
pkts_list=[]

def main():
    parser=argparse.ArgumentParser(description="Simple PCAP fuzzer based on radamsa mutation engine")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-D",required=True, action="store", dest="host", help="Destionation host to fuzz application on")
    requiredNamed.add_argument("-S",required=True, action="store", dest="source", help="Sorce host to fuzz messages from")
    requiredNamed.add_argument("-f",required=True, action="store", dest="file", help="Input pcap file")
    requiredNamed.add_argument("-z",required=True, action="store", dest="fuzz", help="fuzz factor between 0 and 100")
    opts=parser.parse_args()

    if len(sys.argv) != 8:
        parser.help()
    
    if opts.host:
        HOST=opts.host

    if opts.port
        PORT=opts.port

    if opts.file:
        FILE=opts.file

    if opts.fuzz:
        FUZZ=opts.fuzz

if __name__ == '__main__':
    main()