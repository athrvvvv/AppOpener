import os, json, re, sys
from . import check
# Get path of working directory
def get_path():
    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
        return main_path
    elif __file__:
        main_path = os.path.dirname(__file__)
        return main_path

main_path = os.path.join(get_path(),"Data")

# RENAMING PETNAME IN APP_NAMES FILE
def do_changes(app,petname):
    with open((os.path.join(main_path,"app_names.json")),"r") as file:
        data = json.load(file)
        data.pop(app)
        change = {app:petname.lower()}
        data.update(change)
    with open((os.path.join(main_path,"app_names.json")),"w") as file1:
        json.dump(data,file1,indent=4)

# CHANGE PRE / SEC NAME IN DATA FILE
def pre_change():
    file = open((os.path.join(main_path,"app_names_temp.json")),"r")
    data_file_read = open((os.path.join(main_path,"data.json")),"r")
    data_read = json.load(data_file_read)
    data_file = json.load(file)
    keys_file = list(data_file.keys())
    values_file = list(data_file.values())
    for app2 in keys_file:
        if data_file[app2] != "":
            position = keys_file.index(app2)
            app=values_file[position]
            #print('"'+app2+'"','"'+app+'"')
            try:
                data_read[app] = data_read.pop(app2)
            except:
                pass
            #del data_r[app2]
    with open((os.path.join(main_path,"data.json")),"a+") as f:
        g = open((os.path.join(main_path,"data.json")),"r+")
        g.truncate(0)
        json.dump(data_read,f,indent=4)

# CHANGES IN MAIN DATA FILE (PETNAME)
def change_in_data(app,petname):
    with open((os.path.join(main_path,"data.json")),"r") as file:
        data = json.load(file)
    try:
        data[petname] = data.pop(app)
    except: pass
    with open((os.path.join(main_path,"data.json")),"w") as file1:
        json.dump(data,file1,indent=4)

# REVIEW CHANGES IN APP_NAMES FILE
def modify():
    with open((os.path.join(main_path,"app_names.json")),"r") as file:
        data = json.load(file)
        keys = list(data.keys())
        values = list(data.values())
        for petname in values:
            if petname != "":
                position = values.index(petname)
                app = keys[position]
                #print(app,petname)
                change_in_data(app,petname)

# CHANGE ALL PETNAMES TO DEFAULT APP NAMES
def default(output=True):
    if output:
        print("RESTORING DEFAULT APP NAMES")
    file1 = open((os.path.join(main_path,"app_names.json")),"r")
    data1 = json.load(file1)
    keys = list(data1.keys())
    values = list(data1.values())
    file2 = open((os.path.join(main_path,"app_names.json")),"r")
    data2 = json.load(file2)
    for petname in values:
        if petname != "":
            position = values.index(petname)
            app=keys[position]
            #print(app+" "+petname)
            change = {app:app}
            data2.update(change)
    file3 = open((os.path.join(main_path,"app_names.json")),"w")
    json.dump(data2,file3,indent=4)
    if output:
        print("DONE.")

# EXECUTE CHANGES IN DATA FILE
def check_new_name():
    file = open((os.path.join(main_path,"app_names.json")),"r")
    app_temp = open((os.path.join(main_path,"app_names_temp.json")),"r")
    data_temp = json.load(app_temp)
    data = json.load(file)
    keys = list(data.keys())
    values = list(data.values())
    for app2 in values:
        if app2 != "":
            position = values.index(app2)
            app = keys[position]
            change = {app2:app}
            data_temp.update(change)
    with open((os.path.join(main_path,"app_names_temp.json")),"a+") as f:
        g = open((os.path.join(main_path,"app_names_temp.json")),"r+")
        g.truncate(0)
        json.dump(data_temp,f,indent=4)

# DEPENDENCY OF (3)
def edit_things_cli(count,current_name,petname):
    with open((os.path.join(main_path,"app_names.json")),"r") as app_file:
        data = json.load(app_file)
    for app_name in data:
        if current_name == app_name:
            change = {current_name:petname}
            data.update(change)
            with open((os.path.join(main_path,"app_names.json")),"a+") as f:
                g = open((os.path.join(main_path,"app_names.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
                if count == None:
                    count = 1
                print(str(count)+". "+current_name.upper()+" IS NOW "+petname.upper())

# SORT MULTIPLE CHANGES OF APPS VIA CLI - 3
def do_changes_cli(self):
    if "," in self:
        count = 0
        splited=self.split(",")
        for i in splited:
            j = i.strip()
            if j != "":
                count += 1
                split2 = j.split(">")
                current_name = (split2[0]).strip()
                petname = (split2[1]).strip()
                edit_things_cli(count,current_name,petname)
    else:
        splited = self.split(">")
        # print(splited)
        current_name = (splited[0]).strip()
        petname = (splited[1]).strip()
        edit_things_cli(1,current_name,petname)

# FETCH ALL NEW APPS
def update(output=True):
    if output:
        print("FETCHING ALL NEW APPS (if any)")
    check.create_file()
    if output:
        print("UPDATING THE LIST, THIS MAY TAKE TIME...")
    check.setup_files()
    if output:
        print("WRITING APP NAMES")
    with open((os.path.join(main_path,"app_names.json")),"r") as old_AF:
        old = json.load(old_AF)
    with open((os.path.join(main_path,"app_names_temp.json")),"w+") as temp_af:
        json.dump(old,temp_af,indent=4)
    dictionary ={}
    json_object = json.dumps(dictionary, indent = 4)
    with open((os.path.join(main_path,"app_names.json")),"w") as outfile:
        outfile.write(json_object)
    with open((os.path.join(main_path,"data.json")),"r") as app_file:
        data1 = json.load(app_file)
    with open((os.path.join(main_path, "app_names.json")),"r") as file:
        data = json.load(file)
    for app_name in data1:
        change = {app_name:""}
        data.update(change)
        with open((os.path.join(main_path,"app_names.json")),"a+") as f:
            g = open((os.path.join(main_path,"app_names.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    with open((os.path.join(main_path,"app_names_temp.json")),"r") as file:
        data = json.load(file)
        values = list(data.values())
        keys = list(data.keys())
    for petname in values:
        if petname != "":
            position = values.index(petname)
            app_old=keys[position]
            # print(str(app_old)+" changed to "+str(petname))
            do_changes(app_old,petname)
    check_new_name()
    if output:
        print("LIST UPDATED.")

# SETUP FILES - 1
def check_app_names():
    print()
    print("PREPARING FOR INPUTS (JUST ONCE)")
    empty_dictionary ={}
    with open((os.path.join(main_path,"app_names.json")),"w") as outfile:
        json.dump(empty_dictionary, outfile)
    with open((os.path.join(main_path,"data.json")),"r") as app_file:
        data = json.load(app_file)
        keys = data.keys()
        dictionary = {}
    for app_name in keys:
        change = {app_name:""}
        dictionary.update(change)
        with open((os.path.join(main_path,"app_names.json")),"a+") as f:
            g = open((os.path.join(main_path,"app_names.json")),"r+")
            g.truncate(0)
            json.dump(dictionary,f,indent=4)
    with open((os.path.join(main_path,"app_names_temp.json")),"w") as outfile:
        json.dump(empty_dictionary, outfile)
