import sys
sys.path.append('/home/ubuntu/Documents/workspace/qa-wearos/helpers')
import commandline_helper as cmd 
import googlesheet_helper as ggs 
import cts_helper as cts 
               
if __name__ == '__main__':
    cts.backup_results()
    available_modules = ggs.read_google_sheet()
    for module in available_modules:
        cts.run_cts_module(module)

    raw_result = cts.parse_test_result()  
    ggs.update_google_sheet(raw_result) 
    