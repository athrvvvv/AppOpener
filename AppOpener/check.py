import os, json, re, sys, subprocess
from . import update_list

# check what os the library is running on
def check_os():
    os_name = os.name
    if os_name != "nt":
        raise Exception("AppOpener only works on Windows.")
        exit()

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
            is_digit = key[:1].isdigit()
            if is_digit == False:
                val=(re.compile(r'[^a-z-&]')).sub(" ",key)
                final_app_name = re.sub(' +', ' ', val).strip()
                modified_data[final_app_name] = value
            if is_digit == True:
                val=(re.compile(r'[^a-z-&^0-9]')).sub(" ",key)
                final_app_name = re.sub(' +', ' ', val).strip()
                modified_data[final_app_name] = value
        with open((os.path.join(main_path,"data.json")),"w") as f:
            json.dump(modified_data, f, indent=4)

def create_file(print_text=True):
    if check_data == False:
        os.mkdir(main_path)
        subprocess.call("attrib +h "+main_path, shell=True)
    if print_text:
        print("LOADING APPS... (JUST ONCE)")
    cmd = 'powershell -ExecutionPolicy Bypass "Get-StartApps|convertto-json"'
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8', shell=True)
        # Exception if the result is Empty
        # if not result.stdout:
        #     raise Exception("No output returned by the command")
        apps = json.loads(result.stdout)
    except:
        from . import old_style
        return
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
