import PySimpleGUI as sg
import json, requests

BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution?"

API_KEY = "bf20a52d2f9f1b788eb971ed9fa18d30"



#All the stuff inside your window

weatherLayout = [ [sg.Text("What City would you like to know the weather?")],
                  [sg.InputText()],
                  [sg.Text("What Country")],
                  [sg.InputText()],
                  [sg.Button("OK"), sg.Button("Cancle")]]


# Creeate the window
window = sg.Window("Weather", weatherLayout)

#Event Loop to process 'events'  and get the 'values' of the inputs
while True:
    event, values = window.read()
   
# if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'OK':
        break

CITY = values[0]
COUNTRY = values[1]   
   
window.close()


URL = BASE_URL +"q=" + CITY +"," + COUNTRY + "&appid=" + API_KEY + "&units=imperial"
response = requests.get(URL)
print(response)

if response.status_code == 200:
    data = response.json()
    print(data)
     
    # geting main data blocks
    main = data['main']
    coord = data['coord']
    temperature = main['temp']
    humidity = main['humidity']
    pressure = main['pressure']
    report = data['weather']
    feels = main['feels_like']
    min = main["temp_min"]
    max = main["temp_max"]
    visibility = data['visibility']
    wind = data["wind"]
    clouds = data["clouds"]
    dt = data['dt']
    sys = data['sys']
    timezone = data['timezone']

   
# Info pop up
infoPopUp = [ [sg.Text("Weather info for " + CITY +", " + COUNTRY)],
                  [sg.Text("Temperature " + str(temperature))],
                  [sg.Text(f"Feels Like: {feels}")],
                  [sg.Text(f"Humidity: {humidity}")],
                  [sg.Text(f"min: {min}")],
                  [sg.Text(f"max: {max}")],
                  [sg.Button("OK"), sg.Button("Cancle")]]


# Creeate the window
window = sg.Window("Weather", infoPopUp)

#Event Loop to process 'events'  and get the 'values' of the inputs
while True:
    event, values = window.read()
   
# if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'OK':
        break

    CITY = values[0]
    COUNTRY = values[1]   
   
window.close()