from AppOpener import open, close

def main():
    print()
    print("1. Open <any_name> TO OPEN APPLICATIONS")
    print("2. Close <any_name> TO CLOSE APPLICATIONS")
    print()
    open("help")
    print("TRY 'OPEN <any_key>'")
    while True:
        inp = input("ENTER APPLICATION TO OPEN / CLOSE: ").lower()
        if "close " in inp:
            app_name = inp.replace("close ","").strip()
            close(app_name, close_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
        if "open " in inp:
            app_name = inp.replace("open ","")
            open(app_name, open_closest=True) # App will be open be it matches little bit too

if __name__ == '__main__':
    main()
