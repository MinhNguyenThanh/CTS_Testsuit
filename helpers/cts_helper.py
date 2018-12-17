import subprocess
import sys
import os
from os import walk
import xml.etree.ElementTree as ET
import csv
import pygsheets
import commandline_helper as cmd 

CTS_DIR= '/home/ubuntu/Documents/android-cts'
def run_cts_module(name):
    '''
     run command : run cts -m <module-name>
     run command : run -s <watch_seriral>cts -mimport os
<module-name>
    '''
    os.chdir( '/home/ubuntu/Documents/android-cts' )
    cmd.peform_commandline(["./tools/cts-tradefed", "run","cts","-m",name],True) 

def parse_test_result():
    results = []
    reportFile = open('/home/ubuntu/Documents/workspace/qa-wearos/reports/CTS_Report_Summary.csv', 'w')
    # create the csv writer object
    csvwriter = csv.writer(reportFile)
    report_head = []

    # REPORT HEADER
    #| Module |Passed | Failed | Total| Tests |Done |Result Path|Build Model|Build Version SDK|Build FingerPrint|Build Type|

    report_head.append('Module')
    report_head.append('RunTime')
    report_head.append('Passed')
    report_head.append('Failed')
    report_head.append('Total Tests')
    report_head.append('Done')
    report_head.append('Result Path')
    report_head.append('Build Id')
    report_head.append('Build Model')
    report_head.append('Build Version SDK')
    report_head.append('Build FingerPrint')
    report_head.append('Build Type')

    csvwriter.writerow(report_head)
    
    for (dirpath, dirnames, filenames) in walk("/home/ubuntu/Documents/android-cts/results/"):  
        for file in filenames :
            if(file == "test_result.xml"):
                    result_path = dirpath +"/"+ file
                    root = ET.parse(dirpath +"/"+ file).getroot()
                    module = root.find('Module')

                    module_result = []

                 
                    try:
                        if "name" in module.attrib:
                            module_name = module.get('name')
                            runtime = module.get('runtime')
                            number_test_pass = module.get("pass")
                            number_test_fail = root.find("Summary").get('failed')
                            total_test = int(number_test_pass) + int(number_test_fail)
                            done = module.get("done")
                            module_result.append(module_name)
                            module_result.append(runtime)
                            module_result.append(number_test_pass)
                            module_result.append(number_test_fail)
                            module_result.append(total_test)
                            module_result.append(done)
                            module_result.append(result_path)

                        build = root.find('Build')
                        module_result.append(build.get('build_id'))
                        module_result.append(build.get('build_model'))
                        module_result.append(build.get('build_version_sdk'))
                        module_result.append(build.get('build_fingerprint'))
                        module_result.append(build.get('build_type'))
                        results.append(module_result)
                        csvwriter.writerow(module_result)                       
                    except:
                        print("err")

    reportFile.close()
    return results


'''
This method use to parse build info within test-result.xml filr
return : buid id, build type, build model, build fiongerprint, ....
'''
def get_build_info():
    '''
    This method will be generate the build info at the General_Report sheet
    '''
    result_values = []
    for (dirpath, dirnames, filenames) in walk("/home/ubuntu/Documents/android-cts/results/"):  
        for file in filenames :
            if(file == "test_result.xml"):
                    result_path = dirpath +"/"+ file
                    print(result_path)
                    root = ET.parse(dirpath +"/"+ file).getroot()
                    build = root.find('Build')

                    build_info = []
                    build_info.append(build.get('build_id'))
                    build_info.append(build.get('build_model'))
                    build_info.append(build.get('build_version_sdk'))
                    build_info.append(build.get('build_fingerprint'))
                    build_info.append(build.get('build_type'))
                    print(build_info)

def backup_results(command = ["mv", "--","/home/ubuntu/Documents/android-cts/results/*" ,"/home/ubuntu/Documents/android-cts/bak"]):
    cmd.peform_commandline(command)