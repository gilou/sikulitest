root = 'C:\\Program Files\\Adobe\\'
apps = { "After": r"Adobe After Effects CC 2015\Support Files\AfterFX.exe",
        "Audition": r"Adobe Audition CC 2015\Adobe Audition CC.exe", 
        "Bridge": r"Adobe Bridge CC (64 Bit)\Bridge.exe"
        }
for app, path in apps.items():
        print(app + " - " + root + path)

npp = App(r'C:\Program Files\Notepad++\notepad++.exe')
npp.open()
wait(2)
print(npp)
wait("1505728633956.png")
click("1505728633956.png")
wait("1505728661330.png")
click("1505728661330.png")
npp.focus()
type(10*'Hello NPP ')

wait(3)
npp.close()