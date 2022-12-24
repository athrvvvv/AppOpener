__version__ = "1.5"
from . import check, update_list, commands
import os, json, re, inspect

# Checking if required files exists or not
check.check_reference()
check.check_json()
check.app_names()

# Get the path of working directory
main_path = os.path.join((check.get_path()), "Data")

# For making list
def mklist(name=None, path=None, output=True):
    if path == None:
        caller_frame = inspect.stack()[1]
        filename = caller_frame.filename
        dir_path = os.path.dirname(filename)
        path = dir_path
    if name == None:
        name = "app_data.json"
    if name.endswith(".txt"):
        name = name
    dictionary ={}
    with open((os.path.join(path,name)),"w") as outfile:
        json.dump(dictionary,outfile,indent = 4)
    with open((os.path.join(main_path,"data.json")),"r") as data_f:
        data = json.load(data_f)
    with open((os.path.join(path,name)),"a+") as f:
        g = open((os.path.join(path,name)),"r+")
        g.truncate(0)
        json.dump(data,f,indent=4)
    if output:
        print("Successfully saved "+name)

# Run application (Regex implemented)
def run(self, output=True):
    if not output:
        output = False
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
        update_list.update(output=output)
    elif " > " in val:
        update_list.do_changes_cli(val)
        update_list.check_new_name()
        update_list.pre_change()
        update_list.modify()
    elif val == ("default"):
        update_list.default(output=output)
        update_list.check_new_name()
        update_list.pre_change()
        update_list.modify()
    elif val == "mklist":
        mklist(output=output)
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
                    update_list.open_things(j, output=output)
        else:
            update_list.open_things(val, output=output)

# Close any application by just its name :)
def close(self, output=True):
    if not output:
        output = False
    inp = (self).lower()
    val=(re.compile(r'[^a-zA-Z-^0-9?,>&+.]').sub(" ",inp)).strip()
    if "," in val:
        splited = val.split(",")
        for i in splited:
            j = i.strip()
            if j != "":
                update_list.close_things(j, output=output)
    else:
        update_list.close_things(val, output=output)

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
