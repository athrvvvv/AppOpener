__version__ = "1.5"
from . import check, update_list, commands
import os, json, re, inspect

# Checking if required files exists or not
check.check_reference()
check.check_json()
check.app_names()

# Get the path of working directory
main_path = os.path.join((check.get_path()), "Data")

# COLORSHEET FOR TERMINAL WARNINGS !
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Initializing
os.system("")

# For making list
def mklist(name=None, specific=None, path=None):
    if path == None:
        caller_frame = inspect.stack()[1]
        filename = caller_frame.filename
        dir_path = os.path.dirname(filename)
        path = dir_path
    if name == None:
        name = "app_data.json"
        json_file = True
    if name.endswith(".txt"):
        name = name
        json_file = False
    dictionary ={}
    with open((os.path.join(path,name)),"w") as outfile:
        json.dump(dictionary,outfile,indent = 4)
    if specific == None:
        with open((os.path.join(main_path,"data.json")),"r") as data_f:
            data = json.load(data_f)
        with open((os.path.join(path,name)),"a+") as f:
            g = open((os.path.join(path,name)),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    if specific == ("name"):
        with open((os.path.join(main_path,"data.json")),"r") as data_f:
            data = json.load(data_f)
            data_keys = list(data.keys())
            if json_file == True:
                d = {k:None for k in data_keys}
                with open((os.path.join(path,name)),"a+") as f:
                    g = open((os.path.join(path,name)),"r+")
                    g.truncate(0)
                    json.dump(d,f,indent=4)
            elif json_file ==False:
                with open((os.path.join(path,name)),"a+") as f:
                    g = open((os.path.join(path,name)),"r+")
                    g.truncate(0)
                    for i in data_keys:
                        f.write(i+"\n")
    if specific == ("id"):
        with open((os.path.join(main_path,"data.json")),"r") as data_f:
            data = json.load(data_f)
            data_values = list(data.values())
            if json_file == True:
                d = {k:None for k in data_values}
                with open((os.path.join(path,name)),"a+") as f:
                    g = open((os.path.join(path,name)),"r+")
                    g.truncate(0)
                    json.dump(d,f,indent=4)
            elif json_file == False:
                with open((os.path.join(path,name)),"a+") as f:
                    g = open((os.path.join(path,name)),"r+")
                    g.truncate(0)
                    for i in data_values:
                        f.write(i+"\n")

# Run application (Regex implemented)
def run(self):
    inp = (self).lower()
    val=(re.compile(r'[^a-zA-Z-^0-9?,>&]').sub(" ",inp)).strip()
    if val == (""):
        pass
    elif val == ("cls"):
        os.system("cls")
    elif val == ("version"):
        print("AppOpener version "+__version__)
    elif inp == ("?"):
        invsys = '"'
        os.system(f"explorer {invsys}https://appopener.readthedocs.io/en/latest/{invsys}")
    elif val == ("help"):
        print()
        commands.commands()
        print()
    elif val == ("ls"):
        update_list.list_apps()
    elif val == ("rename -m"):
        os.startfile(os.path.join(main_path,"app_names.json"))
        print("RELOAD PROGRAM TO APPEND CHANGES")
    elif val == ("update"):
        update_list.update()
    elif " > " in val:
        update_list.do_changes_cli(val)
        update_list.check_new_name()
        update_list.pre_change()
        update_list.modify()
    elif val == ("default"):
        update_list.default()
        update_list.check_new_name()
        update_list.pre_change()
        update_list.modify()
    elif val == "mklist":
        mklist()
    elif "find " in val:
        print()
        val2 = val.replace("find ","")
        if "," in val2:
            splited = val2.split(",")
            for i in splited:
                j = i.strip()
                if j != "":
                    update_list.find_apps(j)
        else:
            update_list.find_apps(val2)
        print()
    elif val == "log -c" or val == "log":
        print()
        val2 = val.replace("log -","")
        update_list.change_log(val)
        print()
    else:
        if "," in val:
            splited = val.split(",")
            for i in splited:
                j = i.strip()
                if j != "":
                    update_list.open_things(j)
        else:
            update_list.open_things(val)

# Close any application by just its name :)
def close(self):
    inp = (self).lower()
    val=(re.compile(r'[^a-zA-Z-^0-9?,>&+.]').sub(" ",inp)).strip()
    if "," in val:
        splited = val.split(",")
        for i in splited:
            j = i.strip()
            if j != "":
                update_list.close_things(j)
    else:
        update_list.close_things(val)

# Give dictionary of appnames (Uppercase or lowercase)
def give_appnames(upper=False):
    file = open((os.path.join(main_path,"data.json")),"r")
    data = json.load(file)
    keys = data.keys()
    if upper == True:
        dict = {}
        for k in keys:
            change = {k.upper() : None}
            dict.update(change)
        keys_upper = dict.keys()
        return keys_upper
    if upper == False:
        return keys
