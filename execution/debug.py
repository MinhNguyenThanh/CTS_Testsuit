import subprocess
import sys
import os
from os import walk
import xml.etree.ElementTree as ET
import csv
import pygsheets

# If modifying these scopes, delete the file token.json.
#SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1VN8nzFbih88_PpIBE0QM3lK4TCqvWTCCUnBnuCYgnBc'
SAMPLE_RANGE_NAME = 'Summary!A2:G'
CTS_DIR= '/home/ubuntu/Documents/android-cts'

def main():
	result_values = ["1","b","c","x","y","z"]
	print("hello")
	update_google_sheet(result_values)
	print("goobye")





def update_google_sheet(result_values):
    '''
    This method use to get result from test_result.xml to update google sheet report
    '''
    SPREADSHEET_ID = '1VN8nzFbih88_PpIBE0QM3lK4TCqvWTCCUnBnuCYgnBc'
    gc = pygsheets.authorize()
    print("flag")
    # Open spreadsheet and then workseet
    sh = gc.open_by_key(SPREADSHEET_ID)
    wks_list = sh.worksheets()
    module_ws = wks_list[2]# Modules tab
    print(len(wks_list))
    module_ws.append_table(values=result_values, start="A1",end=None, dimension='ROWS', overwrite=True)
        

if __name__ == '__main__':
    main() 