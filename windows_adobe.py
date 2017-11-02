root = 'C:\\Program Files\\Adobe\\'
apps = { #"After": r"Adobe After Effects CC 2015\Support Files\AfterFX.exe",
        "Audition": r"Adobe Audition CC 2015\Adobe Audition CC.exe"
        #, "Bridge": r"Adobe Bridge CC (64 Bit)\Bridge.exe"
        }
setFindFailedResponse(SKIP)
for app, path in apps.items():
        print('Considering ' + app + '(' + root + path + ')')
        sapp = App(root + path)
        sapp.open()
        try:
            wait("1505729222650.png", 35)
            click("1505729222650.png") 
            wait("1509617897369.png", 5)
            click("1509617897369.png")
            wait("1509618378336.png", 35)
            click("1509618378336.png")
            wait(2)
        except FindFailed:
            print('Failed')
            wait(2)
