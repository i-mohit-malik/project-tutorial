import os
import datetime

for dirpath, dirnames, filenames in os.walk('C:\\Omniverse\\Mohit\\project-tutorial\\os_module'):
    print(f'\n\nDirectory Path: {dirpath}')
    print('Files:')
    for filename in filenames:  
            print(f'\t{filename}')

mod_time_basic = os.stat('C:\\Omniverse\\Mohit\\project-tutorial\\os_module\\basics.py').st_mtime
print(f'Modification time for basics.py: {datetime.datetime.fromtimestamp(mod_time_basic)}')

# or 

mod_time_about = os.path.getmtime('C:\\Omniverse\\Mohit\\project-tutorial\\os_module\\about.txt')
print(f'Modification time for about.txt: {datetime.datetime.fromtimestamp(mod_time_about)}\n\n')