import os,json,re

main_path = os.path.dirname(__file__)

def run(self):
    inp = (self).lower()
    val=(re.compile(r'[^a-zA-Z-^0-9 ]').sub(" ",inp)).strip()
    if val == (""):
        pass
    else:
        with open ((os.path.join(main_path,"apps_list.json")),"r") as f:
            data1 = json.load(f)
            try:
                dir01 = data1[val]
                os.system("explorer shell:appsFolder\\"+dir01)
            except:
                print("NOT FOUND")
                pass