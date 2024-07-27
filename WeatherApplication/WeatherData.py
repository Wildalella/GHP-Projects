import json, requests
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

ZIP = "30040"
CITY = "Statesboro"
STATE = "GA"
COUNTRY = "US"
API_KEY = "bf20a52d2f9f1b788eb971ed9fa18d30"

URL = BASE_URL +"q=" + CITY +"," + COUNTRY + "&appid=" + API_KEY + "&units=imperial"
response = requests.get(URL)
print(response)

if response.status_code == 200:
    data = response.json()
    print(data)
     
    # geting main data blocks
    main = data['main']
    temperature = main['temp']
    humidity = main['humidity']
    pressure = main['pressure']


    print("Weather info for " + CITY +", " + COUNTRY)
    print("Temperature " + str(temperature))
    print(f"Humidity: {humidity}" )
    print(f"Pressure: {pressure}" )
   

 #Challange
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
  

    
    print(f"Feels Like: {feels}" )
    print(f"min: {min}")
    print(f"max: {max}")
    print(f"visibility: {visibility}")
    print(f"wind speed: {wind['speed']}")
    print(f"wind degree: {wind['deg']}")
    print(f"clouds: {clouds['all']}")
    print(f"timezone: {timezone}")
    print(f"sunrise: {sys['sunrise']}")
    print(f"sunset: {sys['sunset']}")
    print(f"dt: {dt}")

   


    
   



















