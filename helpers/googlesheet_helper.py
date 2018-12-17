import subprocess
import sys
import os
from os import walk
import xml.etree.ElementTree as ET
import csv
import pygsheets
import pandas as pd


# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1VN8nzFbih88_PpIBE0QM3lK4TCqvWTCCUnBnuCYgnBc'
SAMPLE_RANGE_NAME = 'Summary!A2:G'

def read_google_sheet():
    '''
    This method use to get all available modules from googlesheet using pandas framework
    '''
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
    return get_run_modules[0:235] #Number of modules

def update_google_sheet(result_values):
    '''
    This method use to get result from test_result.xml to update google sheet report
    '''
    SPREADSHEET_ID = '1VN8nzFbih88_PpIBE0QM3lK4TCqvWTCCUnBnuCYgnBc'
    gc = pygsheets.authorize()
    # Open spreadsheet and then workseet
    sh = gc.open_by_key(SPREADSHEET_ID)
    wks_list = sh.worksheets()
    module_ws = wks_list[2] # Modules tab
    module_ws.append_table(values=result_values, start="A1", end=None, dimension='ROWS', overwrite=False)

