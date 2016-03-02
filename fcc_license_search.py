#!/usr/bin/env python
import argparse
import urllib
import json
import sys

def main():
    args = makeargs()
    fcc_data = query_fcc_by_name(args.lname, args.fname)
    if match_found(args,fcc_data):
        display_results(args,fcc_data)

def query_fcc_by_name(last_name, first_name):
    try:
        data = urllib.urlopen('http://data.fcc.gov/api/license-view/basicSearch/getLicenses?searchValue='+str(last_name)+'%2C+'+str(first_name)+'&format=json').read()
        info = json.loads(data)
        return info
    except Exception as e:
        print_error(e)

def match_found(args,info):
    try:
        if "Errors" in info:
            print info['Errors']['Err'][0]['msg']
            return False
        else:
            return True
    except Exception as e:
        print_error(e)

def display_results(args,info):
    ## takes a dict
    try:
        print "=============== LICENSES ================="
        print "All licenses found for: "+str(args.fname)+' '+str(args.lname)
        for i in info['Licenses']['License']:
            print "Type:", i['serviceDesc']
            print "\tCallsign: ",i['callsign']
            print "\tStatus:",i['statusDesc']
    except Exception as e:
        print_error(e)

def makeargs():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--fname', type=str, help='description help here')
        parser.add_argument('-l', '--lname', type=str, help='description help here')
        args = parser.parse_args()
        return args
    except Exception as e:
        print_error(e)

def print_error(e):
    ## takes an exception as a string
    print "\n--------------------------------------------------------------------------------"
    print "                               There was an error"
    print "--------------------------------------------------------------------------------"
    print str(e)
    print "--------------------------------------------------------------------------------\n"

if __name__ == "__main__":
    main()
