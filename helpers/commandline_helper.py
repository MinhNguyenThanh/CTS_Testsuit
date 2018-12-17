import subprocess
import sys
import os
from os import walk
import xml.etree.ElementTree as ET
import csv
import pygsheets

def peform_commandline(args_arr,show_log=False):
    
    if(show_log):
        p = subprocess.Popen(args_arr, stdout=subprocess.PIPE)
        while True:
            line = p.stdout.readline()
            if not line:
                break
            print(line.strip()) 
            sys.stdout.flush()    
    else:
        args_string = ' '.join(args_arr)
        subprocess.call(args_string, stdout=subprocess.PIPE, shell = True)