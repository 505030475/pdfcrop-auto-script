import os,time
import glob
print('demon started')
file_list_start = glob.glob('*.pdf')

while 1:
    file_list = glob.glob('*.pdf')
    change_flag = False
    for file in file_list:
        if file not in file_list_start:
            if '-crop' in file:
                continue
            command = 'pdfcrop '+file
            res = os.system(command)
            print('crop pdf file:',file,'\t\tresult:',res)
            change_flag = True
    if change_flag:
        file_list_start = file_list

    time.sleep(4)