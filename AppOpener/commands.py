def commands():
    data = [['KEY', 'USE'],
            ['(?)','DOCUMENTATION'],
            ['(VERSION)','SEE APPOPENER VERSION'],
            ['(LS)','LIST OF APPLICATIONS'],
            ['(FIND XYZ)', "FIND APPLICATION"],
            ['(UPDATE -M)','UPDATE APPNAMES MANUALLY'],
            ['(UPDATE)','LOAD NEW DATA'],
            ['(OLD > NEW)','UPDATE APP VIA CLI'],
            ['(DEFAULT)','RESTORES DEFAULT APPNAMES'],
            ['(LOG)','SEE CHANGED PETNAME(s)'],
            ['(CLS)','CLEARS SCREEN']
            ]
    dash = '-' * 35
    for i in range(len(data)):
        if i == 0:
            print(dash)
            print('{:<15s}{:^15s}'.format(data[i][0],data[i][1]))
            print(dash)
        else:
            print('{:<15s}{:^12s}'.format(data[i][0],data[i][1]))