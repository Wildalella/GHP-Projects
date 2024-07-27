import PySimpleGUI as sg
import json, requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "bf20a52d2f9f1b788eb971ed9fa18d30"

#All the stuff inside your window
layout = [ [sg.Text("What's your name?")],
           [sg.InputText()],
           [sg.Button("OK"), sg.Button("Cancle")]]

weatherLayout = [ [sg.Text("What City would you like to know the weahter?")],
                  [sg.InputText()],
                  [sg.Button("OK"), sg.Button("Cancle")]]


# Creeate the window
window = sg.Window("Hello Example", layout)

#Event Loop to process 'events'  and get the 'values' of the inputs
while True:
    event, values = window.read()

# if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print('Hello', values [0], '!')

window.close()
