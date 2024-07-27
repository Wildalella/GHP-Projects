import json, requests
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


API_KEY = "bf20a52d2f9f1b788eb971ed9fa18d30"

cityOne = input("First city you want to compare")
cityTwo = input("Second city you want to compare")

countryOne = input("First country you want to compare")
countryTwo = input("Second country you want to compare")




#countryOne = input("What country")

URL1 = BASE_URL +"q=" + cityOne +"," + countryOne + "&appid=" + API_KEY + "&units=imperial"
URL2 = BASE_URL +"q=" + cityTwo +"," + countryTwo + "&appid=" + API_KEY + "&units=imperial"

responseOne = requests.get(URL1)
responseTwo = requests.get(URL2)

#Response One
if responseOne.status_code == 200:
    data = responseOne.json()
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
    
  


    print("Weather info for " + cityOne +", " + countryOne)
    print(f"longitude: {coord['lon']}" )
    print(f"lattiude: {coord['lat']}" )

    
   # print(f"description:" + str(report['description']) )
   # print(f"Icon: {report['icon']}" )
    
    
    print("Temperature " + str(temperature))
    print(f"Feels Like: {feels}" )
    print(f"Temperature Min: {min}")
    print(f"Temperature Max: {max}")
    print(f"Pressure: {pressure}" )
    print(f"Humidity: {humidity}" )
    

    print(f"visibility: {visibility}")
    print(f"wind speed: {wind['speed']}")
    print(f"wind degree: {wind['deg']}")

    print(f"clouds: {clouds['all']}")

    print(f"dt: {dt}")
    print(f"type: {sys['type']}")
    print(f"sunrise: {sys['id']}")
    print(f"sunrise: {sys['sunrise']}")
    print(f"sunset: {sys['sunset']}")

    print(f"timezone: {timezone}")
   

    


 # Response Two
if responseTwo.status_code == 200:
    data = responseTwo.json()
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
    

    print("Weather info for " + cityTwo +", " + countryTwo)
    print(f"longitude: {coord['lon']}" )
    print(f"lattiude: {coord['lat']}" )

   # print(f"description: {report['description']}" )
   # print(f"Icon: {report['icon']}" )
    
    
    print("Temperature " + str(temperature))
    print(f"Feels Like: {feels}" )
    print(f"Temperature Min: {min}")
    print(f"Temperature Max: {max}")
    print(f"Pressure: {pressure}" )
    print(f"Humidity: {humidity}" )
    

    print(f"visibility: {visibility}")
    print(f"wind speed: {wind['speed']}")
    print(f"wind degree: {wind['deg']}")

    print(f"clouds: {clouds['all']}")

    print(f"dt: {dt}")
    print(f"type: {sys['type']}")
    print(f"sunrise: {sys['id']}")
    print(f"sunrise: {sys['sunrise']}")
    print(f"sunset: {sys['sunset']}")

    print(f"timezone: {timezone}")
   
    
    
   










