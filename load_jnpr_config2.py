#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
import time
from time import sleep
import sys

host = '10.13.107.248'
myconf1 = """
         set snmp view APPSI-RO oid 1.3.6.1.4.1.2636.3.39.* exclude
         """
myconf2 = """
         del snmp view APPSI-RO oid 1.3.6.1.4.1.2636.3.39.*
         """

dev = Device(host=host,user='ccl',password='ccl123')
    
        # open a connection with the device and start a NETCONF session
try:
    dev.open()
except Exception as err:
    print "Cannot connect to device:", err

dev.bind( cu=Config )
for i in reversed(range(0, 10)):
    
    print "Locking the configuration"
    try:
        dev.cu.lock()
    except LockError:
        print "Error: Unable to lock configuration"
        dev.close()
        re
    print "Loading configuration changes"
    try:
        dev.cu.load(myconf1, merge=True,format='set')
        print "##voici la configuration qui sera commitee##"
        dev.cu.pdiff()
    except ValueError as err:
        print err.message
    except Exception as err:
        if err.rsp.find('.//ok') is None:
            rpc_msg = err.rsp.findtext('.//error-message')
            print "Unable to load configuration changes: ", rpc_msg
        print "Unlocking the configuration"
        try:
                dev.cu.unlock()
        except UnlockError:
                print "Error: Unable to unlock configuration"
        dev.close()
    print "Committing the configuration"
    try:
        dev.cu.commit()
    except CommitError:
        print "Error: Unable to commit configuration"
        print "Unlocking the configuration"
        try:
            dev.cu.unlock()
        except UnlockError:
            print "Error: Unable to unlock configuration"
        dev.close()



    print "## now wait some time ##"
    for i in reversed(range(1, 60)): #wait one minute
        time.sleep(1 - time.time() % 1) 
        sys.stderr.write('\r%4d' % i)
    print "\n####"
    

    try:
        dev.cu.load(myconf2, merge=True,format='set')
        print "##voici la configuration qui sera commitee##"
        dev.cu.pdiff()
    except ValueError as err:
        print err.message
    except Exception as err:
        if err.rsp.find('.//ok') is None:
            rpc_msg = err.rsp.findtext('.//error-message')
            print "Unable to load configuration changes: ", rpc_msg
        print "Unlocking the configuration"
        try:
                dev.cu.unlock()
        except UnlockError:
                print "Error: Unable to unlock configuration"
        dev.close()
    print "Committing the configuration"
    try:
        dev.cu.commit()
    except CommitError:
        print "Error: Unable to commit configuration"
        print "Unlocking the configuration"
        try:
            dev.cu.unlock()
        except UnlockError:
            print "Error: Unable to unlock configuration"
        dev.close()
    print "Unlocking the configuration"
    try:
         dev.cu.unlock()
    except UnlockError:
         print "Error: Unable to unlock configuration"
dev.close()