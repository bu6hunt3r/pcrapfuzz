#!/usr/bin/env python
#-*- coding: utf-8 -*-

from subprocess import PIPE, Popen

def mutate(payload):
    radamsa_bin="/usr/bin/radamsa"
    radamsa=[radamsa_bin,'-n','1','-']
    r=Popen(radamsa,stdout=PIPE, stdin=PIPE)
    result=r.communicate(payload)[0]
    return result