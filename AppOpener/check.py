import os, json, re, sys
from subprocess import getoutput
from . import update_list

# Get path of working directory
def get_path():
    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
        return main_path
    elif __file__:
        main_path = os.path.dirname(__file__)
        return main_path

main_path = os.path.join(get_path(), "Data")

# Status of existance of required files
check_data = os.path.isdir(main_path)
check_json_list = os.path.exists(os.path.join(main_path,"data.json"))
check_app_names = os.path.exists(os.path.join(main_path,"app_names.json"))

# Convert text file to json format file
def setup_files():
    with open((os.path.join(main_path,"data.json")),"r") as data_file:
        data_duplicate = json.load(data_file)
        modified_data = {}
        for key, value in data_duplicate.items():
            is_digit = key.isdigit()
            if not is_digit:
                val=(re.compile(r'[^a-z-&]')).sub(" ",key)
                final_app_name = re.sub(' +', ' ', val).strip()
                modified_data[final_app_name] = value
            if is_digit:
                val=(re.compile(r'[^a-z-&^0-9]')).sub(" ",key)
                final_app_name = re.sub(' +', ' ', val).strip()
                modified_data[final_app_name] = value
        with open((os.path.join(main_path,"data.json")),"w") as f:
            json.dump(modified_data, f, indent=4)

def create_file():
    if not check_data:
        os.mkdir(main_path)
        os.system(("attrib +h "+main_path))
    cmd = 'powershell -ExecutionPolicy Bypass "Get-StartApps|convertto-json"'
    apps=json.loads(getoutput(cmd))
    names = {}
    for each in apps:
        names.update({each['Name'].lower():each['AppID']})
    with open((os.path.join(main_path,"data.json")),"w") as outfile:
        json.dump(names,outfile,indent = 4)
    setup_files()

def check_json():
    if check_json_list == (False):
        create_file()

# Make seperate file for appnames (to perform various features)
def app_names():
    if check_app_names == (False):
        update_list.check_app_names()
    update_list.check_new_name()
    update_list.pre_change()
    update_list.modify()
