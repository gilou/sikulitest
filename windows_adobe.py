root = 'C:\\Program Files\\Adobe\\'
apps = { "After": r"Adobe After Effects CC 2015\Support Files\AfterFX.exe",
        "Audition": r"Adobe Audition CC 2015\Adobe Audition CC.exe", 
        "Bridge": r"Adobe Bridge CC (64 Bit)\Bridge.exe"
        }
for app, path in apps.items():
        print('Considering ' + app + '(' + root + path + ')')
        sapp = App(root + path)
        sapp.open()
        wait(2)
        wait("1505729222650.png")
        click("1505729222650.png")
        wait(2)
