import os, json, re, win32gui, win32con, sys
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
check_reference_file = os.path.exists(os.path.join(main_path,"reference.txt"))
check_json_list = os.path.exists(os.path.join(main_path,"data.json"))
check_app_names = os.path.exists(os.path.join(main_path,"app_names.json"))

# Maximize window
def maximize():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# Convert text file to json format file
def convert_txt_json():
    dictionary ={}
    with open((os.path.join(main_path,"data.json")),"w") as outfile:
        json.dump(dictionary,outfile,indent = 4)
    file1 = open(os.path.join(main_path,'reference.txt'),'r')
    Lines = file1.readlines()
    for line in Lines:
        line1= line.strip()
        index = line1.find('  ')
        # HERE line1[:index] is the APP-NAME
        # HERE line1[index:] is the APP-ID.
        app_name = line1[:index]
        app_id = (line1[index:]).strip()
        is_digit = app_name[:1].isdigit()
        with open ((os.path.join(main_path,"data.json")),"r") as f:
                data = json.load(f)
        if is_digit == (False):
            val=(re.compile(r'[^a-z-&]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open((os.path.join(main_path,"data.json")),"a+") as f:
                g = open((os.path.join(main_path,"data.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
        elif is_digit == (True):
            val=(re.compile(r'[^a-z-&^0-9]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open((os.path.join(main_path,"data.json")),"a+") as f:
                g = open((os.path.join(main_path,"data.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)

# Making temp file for appnames and appids
def check_reference():
    if check_data == (False):
        os.mkdir(main_path)
        os.system(("attrib +h "+main_path))
    if check_reference_file == (False):
        maximize()
        os.system("mode 800")
        print("LOADING APPS... (JUST ONCE)")
        os.system("powershell -command "+'"'+"get-StartApps | Out-File -encoding ASCII -Filepath "+"'"+(os.path.join(main_path,"reference.txt"))+"'"+'"')
        with open((os.path.join(main_path,"reference.txt")),"r") as f, open((os.path.join(main_path,"reference_temp.txt")),"w+") as outfile:
            for i in f.readlines():
                if not i.strip():
                    continue
                if i:
                    outfile.write(i)
        os.system("mode 100") # This used as to get lengthy appids

# Check if json formatted file is made
def check_json():
    if check_json_list == (False):
        print("REARRANGING APPS... (JUST ONCE)")
        convert_txt_json()
        try: os.remove(os.path.join(main_path,"reference_temp.txt"))
        except: pass

# Make seperate file for appnames (to perform various features)
def app_names():
    if check_app_names == (False):
        update_list.check_app_names()
    update_list.check_new_name()
    update_list.pre_change()
    update_list.modify()
