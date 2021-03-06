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

maxdelay=60
 
def accept():
    if find("1509638042137.png"):
        click("1509638042137.png")
    else:
        print('En attente du bouton accepter pour 40s...')
        if wait("1509618378336.png", 40):
            click("1509618378336.png")

def waitfor_licutil(delay=maxdelay, app=None):
    state = getFindFailedResponse()
    setFindFailedResponse(ABORT)
    found = False
    for tentative in range(delay):
        try:
            find("1509720601306.png")
            found = True
            break
        except FindFailed:
            if app and sapp.hasWindow():
                break
        wait(1)
    setFindFailedResponse(state)
    return found
    
notfull = Do.popAsk("Lancement du script pour seulement une appli ?", "Choix appli (3 secondes)", 3)

if notfull:
    app = select("Choisissez un soft a lancer dans la liste", options = apps.keys())
    apps = dict(app=apps[app])

for app, path in sorted(apps.items()):
    setFindFailedResponse(ABORT)
    print('Considering ' + app + '(' + root + path + ')')
    sapp = App(root + path)
    os.system("taskkill /f /t /im adobe_lic*")
    if not sapp.isRunning(): sapp.open()
    print('app seen as: {} main window as: {} PID is {}'.format(
                                                sapp.getName(),
                                                sapp.getWindow(),
                                                sapp.getPID()
                                            )
    )
    print('Waiting for {} to spawn a window'.format(sapp.getName()))

    waitfor_licutil(maxdelay, sapp)
    try:        
        accept()
               
    except FindFailed:
        setFindFailedResponse(SKIP)
        delay = 10
        print('Echec de la premiere tentative, attente fenetre pendant {delay} secondes'.format(delay=delay))
        if wait("1505729222650.png", delay):
            click("1505729222650.png") 
            print('Attente Eval')
            wait("1509617897369.png", delay)
            click("1509617897369.png")
            print('OK')
        print('et on attend...')
        if not waitfor_licutil(maxdelay, sapp):
            break
        accept()
    finally:
        print('waiting for soft to give sign of life')
        for tentative in range(maxdelay):
            wait(1)            
            if sapp.hasWindow():
                wait(3)
                break
        sapp.close()
