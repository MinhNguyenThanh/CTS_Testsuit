import subprocess
import sys
import os
from os import walk
import xml.etree.ElementTree as ET
import csv
import pygsheets
import pandas as pd


if __name__ == '__main__':
    SPREADSHEET_ID = '1VN8nzFbih88_PpIBE0QM3lK4TCqvWTCCUnBnuCYgnBc'
    gc = pygsheets.authorize()
    # Open spreadsheet and then workseet
    sh = gc.open_by_key(SPREADSHEET_ID)
    wks_list = sh.worksheets()
    test_suite = wks_list[1]
    df = test_suite.get_as_df()
    executed = df['Used?'] == 'y'
    available = df['Executed?'] != 'Done'
    list_module = df[executed & available]
    get_run_modules = list_module['Test cases']
    for tc in get_run_modules:
    	print (tc) 
    # arr = array(get_run_modules[0:2])