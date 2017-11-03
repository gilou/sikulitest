#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
root = 'C:\\Program Files\\Adobe\\'
apps = { "After": r"Adobe After Effects CC 2015\Support Files\AfterFX.exe",
        "Audition": r"Adobe Audition CC 2015\Adobe Audition CC.exe",
        "Bridge": r"Adobe Bridge CC (64 Bit)\Bridge.exe",
        "LightRoom": r"Adobe Lightroom\lightroom.exe",
        "Premiere": r"Adobe Premiere Pro CC 2015\Adobe Premiere Pro.exe",
        "Dreamweaver": r"Adobe Dreamweaver CC 2015\Dreamweaver.exe",
        "Illustrator": r"Adobe Illustrator CC 2015\Support Files\Contents\Windows\Illustrator.exe",
        "Photoshop": r"Adobe Photoshop CC 2015\Photoshop.exe"
        }
def accept():
    wait(30)
    if find("1509638042137.png"):
        click("1509638042137.png")
    else:
        print('En attente du bouton accepter pour 15s...')
        wait("1509618378336.png", 15)
        print('OK, clic accepter')
        click("1509618378336.png")         

notfull = Do.popAsk("Lancement du script pour seulement une appli ?", "Choix appli", 2)

if notfull:
   apps = [ select("Choisissez un soft a lancer dans la liste", options = apps.keys()) ] 

for app, path in sorted(apps.items()):
    setFindFailedResponse(ABORT)
    print('Considering ' + app + '(' + root + path + ')')
    print('killing any licensing utilities stil running (why ?)')
    os.system('taskkill /f /im "adobe_licutil.exe" /t')
    wait(3)
    sapp = App(root + path)
    if not sapp.isRunning(): sapp.open()
    print('app seen as: ' + sapp.getName())
    print('main window as: ' + sapp.getWindow())
    try:
        accept()            
    except FindFailed:
        setFindFailedResponse(SKIP)
        if not sapp.hasWindow():
            delay = 45
        else:
            delay = 2
        print('Echec de la premiere tentative, attente fenetre pendant {delay} secondes'.format(delay=delay))
        if wait("1505729222650.png", delay):
            click("1505729222650.png") 
            print('Attente Eval')
            wait(delay/2)
            wait("1509617897369.png", delay/2)
            click("1509617897369.png")
            print('OK')
        wait(delay)
        
        accept()
    finally:
        wait(3)
        sapp.close()
        wait(3)
