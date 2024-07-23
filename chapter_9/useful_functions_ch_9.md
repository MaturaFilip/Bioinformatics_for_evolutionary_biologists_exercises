# Useful functions for chapter 9: Files, programs, and user input in book Python for Biologists.

os module (Operating system)
shutil module (SHell UTILities)

### rename file / rename and move / rename folder
- os.rename('old.txt', 'new.txt')

### make dir
- os.mkdir('path')
- os.mkdirs('path/next/deeper/more_deeper')

### copy file or folder
- shutil.copy('old.txt', 'copy.txt')
- shutil.copytree('old_folder', 'copy_folder') -> folder copy

### file or folder exists?
if os.path.exists('path.txt'):
	print('exist')

### deleting files and folder
os.remove('file.txt') # single file
os.rmdir('empty_folder')
shutil.rmtree('full_folder')

### listing folder contents 
for file_name in os.listdir('.'): # listdir gives me list of content
	print('name:' + file_name)

### running external programs
The functions for running external program reside in the **subprocess** module

import subprocess
subprocess.call('/bin/date')

-> supply command-line options
subprocess.call('/bin/date +%B', shell=True)

### Saving program output
current_month = subprocess.check_output('/bin/date +%B', shell=True)


### Command line arguments
sys module
print(sys.argv) # special list ['program.py', 'one', 'two']

