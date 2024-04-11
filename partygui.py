#!/usr/bin/env python3 ./partygui.py

import PySimpleGUI as sg
import time
import os

platform = ""
website = ""
creator = ""

sg.theme("LightBlue2")

layout = [[sg.Text("What Platform?"), sg.Radio("Coomer", "coom_or_kemono", key="-COOMER-"), sg.Radio("Kemono", "coom_or_kemono", key="-KEMONO-")],
          [sg.Text("(Only If Coomer) What Platform?"), sg.Radio("Onlyfans", "of_or_fa", key="-ONLYFANS-"), sg.Radio("Fansly", "of_or_fa", key="-FANSLY-")],
          [sg.Text("What Is The Username/id?"), sg.Input(key="-USERNAME-", do_not_clear=True, size=(25, 1))],
          [sg.Submit("Start Download"), sg.Cancel()]
]

window = sg.Window('Party GUI', layout)


event, values = window.read()

window.close()

creator = values['-USERNAME-']

if values['-COOMER-']:
    platform = "coomer"
else:
    platform = "kemono"

if values['-ONLYFANS-']:
    website = "onlyfans"
else:
    website = "fansly"

if platform == "kemono":
    os.system("party kemono patreon " + (creator))
else:
    os.system("party coomer %s %s" % (website, creator))

