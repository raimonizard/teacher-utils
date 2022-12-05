import os
import glob
import re

directory = input("Write directory name: ")
if(os.path.exists(directory) & os.path.isdir(directory)):
    print("Directory exists")
    os.chdir(directory)
    choice = input("Would you like to modify moodle exported tasks files e.g. '*_237770_assignsubmission_file_' ? [y/n]: ")

    if choice == 'y':
        res = [file for file in os.listdir(directory) if re.search(r'(?<!\d)_\d{6}_assignsubmission_file_', file)]
        for file in res:
            if(file):
                print(file)
                pattern = f'(?<!\d)_\d{6}_assignsubmission_file_'
                rename = ''
                renamedFile = file.replace(re.findall(r"(?<!\d)_\d{6}_assignsubmission_file_", file)[0],"")
                os.rename(file,renamedFile)
                
        res = [file for file in os.listdir(directory) if re.search(r'(?<!\d)_\d{4}_assignsubmission_file_', file)]
        for file in res:
            if(file):
                print(file)
                pattern = f'(?<!\d)_\d{4}_assignsubmission_file_'
                rename = ''
                renamedFile = file.replace(re.findall(r"(?<!\d)_\d{4}_assignsubmission_file_", file)[0],"")
                os.rename(file,renamedFile)

        res = [file for file in os.listdir(directory) if re.search(r'(?<!\d)_\d{5}_assignsubmission_file_', file)]
        for file in res:
            if(file):
                print(file)
                pattern = f'(?<!\d)_\d{5}_assignsubmission_file_'
                rename = ''
                renamedFile = file.replace(re.findall(r"(?<!\d)_\d{5}_assignsubmission_file_", file)[0],"")
                os.rename(file,renamedFile)

        res = [file for file in os.listdir(directory) if re.search(r'(?<!\d)_\d{6}_assignsubmission_onlinetext_', file)]
        for file in res:
            if(file):
                print(file)
                pattern = f'(?<!\d)_\d{6}_assignsubmission_onlinetext_'
                rename = ''
                renamedFile = file.replace(re.findall(r"(?<!\d)_\d{6}_assignsubmission_onlinetext_", file)[0],"_comentari")
                os.rename(file,renamedFile)
    else:
        pattern = input("Write your search string pattern: ")
        rename = input("Write your rename string: ")
        for file in glob.glob("*" + pattern + "*"):
            if(file):
                print(file)
                renamedFile = file.replace(pattern, rename)
                os.rename(file,renamedFile)
else:
    print("Directory doesn't exist")