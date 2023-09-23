import urllib.request

#define a website
url_nyc = "https://w1.weather.gov/xml/current_obs/display.php?stid=KJRB"
url_chi = "https://w1.weather.gov/xml/current_obs/display.php?stid=KORD"
url_la = "https://w1.weather.gov/xml/current_obs/display.php?stid=KCQT"
url_hou = "https://w1.weather.gov/xml/current_obs/display.php?stid=KIAH"


print("Your Weather Report")
print()
print("Current observation are available for:")
print("- Chicago")
print("- New York City")
print("- Los Angeles")
print("- Houston")
print()

#add weather report to dictionary
weather_dict = {}
invalid = True
while invalid == True:
    city = input("Enter the city you would like a weather report for: ")
    if city == "New York City":
        print('Accessing weather data...')
        invalid = False
        nyc_response = urllib.request.urlopen(url_nyc)
        nyc_data = nyc_response.read().decode('utf-8')
        linesplit = nyc_data.split('\n')
        rawweather = linesplit[30]
        weather = rawweather[10:(len(rawweather)-10)]
        weather_dict['nyc_weather'] = weather
        cutlist = ["location","temp_f", "relative_humidity", "wind_string", "observation_time"]
        for item in cutlist:
            ilist = nyc_data.split(item)
            rawitem = ilist[1]
            data = rawitem[1:(len(rawitem)-2)]
            weather_dict['nyc_'+item] = data
        print()
        print('The current weather has been accessed for New York City')
        
        
    elif city == "Chicago":
        print('Accessing weather data...')
        invalid = False
        chi_response = urllib.request.urlopen(url_chi)
        chi_data = chi_response.read().decode('utf-8')
        linesplit = chi_data.split('\n')
        rawweather = linesplit[30]
        weather = rawweather[10:(len(rawweather)-10)]
        weather_dict['chi_weather'] = weather
        cutlist = ["location","temp_f", "relative_humidity", "wind_string", "observation_time"]
        for item in cutlist:
            ilist = chi_data.split(item)
            rawitem = ilist[1]
            data = rawitem[1:(len(rawitem)-2)]
            weather_dict['chi_'+item] = data
        print()
        print('The current weather has been accessed for Chicago')
        

    elif city == "Los Angeles":
        print('Accessing weather data...')
        invalid = False
        la_response = urllib.request.urlopen(url_la)
        la_data = la_response.read().decode('utf-8')
        linesplit = la_data.split('\n')
        rawweather = linesplit[30]
        weather = rawweather[10:(len(rawweather)-10)]
        weather_dict['la_weather'] = weather
        cutlist = ["location","temp_f", "relative_humidity", "wind_string", "observation_time"]
        for item in cutlist:
            ilist = la_data.split(item)
            rawitem = ilist[1]
            data = rawitem[1:(len(rawitem)-2)]
            weather_dict['la_'+item] = data
        print()
        print('The current weather has been accessed for Los Angeles')
    

    elif city == "Houston":
        print('Accessing weather data...')
        invalid = False
        hou_response = urllib.request.urlopen(url_hou)
        hou_data = hou_response.read().decode('utf-8')
        linesplit = hou_data.split('\n')
        rawweather = linesplit[30]
        weather = rawweather[10:(len(rawweather)-10)]
        weather_dict['hou_weather'] = weather
        cutlist = ["location","temp_f", "relative_humidity", "wind_string", "observation_time"]
        for item in cutlist:
            ilist = hou_data.split(item)
            rawitem = ilist[1]
            data = rawitem[1:(len(rawitem)-2)]
            weather_dict['hou_'+item] = data
        print()
        print('The current weather has been accessed for Houston')

        
    else:
        print("No data available. Please try another city")
        print()
        invalid = True

#select & output weather
print()
print('Information available:','\n','- location','\n','- weather','\n','- temperature','\n','- humidity','\n','- wind','\n','- observation')
if city == 'Houston':
    pre = 'hou_'
elif city == 'Chicago':
    pre = 'chi_'
elif city == 'Los Angeles':
    pre = 'la_'
elif city == 'New York City':
    pre = 'nyc_'
keepgoing = True
while keepgoing == True:
    info = input('What weather information would you like? Or, to end, enter "done". ')
    if info == 'location':
        print('The location of the weather report is',weather_dict[pre+'location'])
        print()
    elif info == 'weather':
        print('The weather in', city,'is',weather_dict[pre+'weather'])
        print()
    elif info == 'temperature':
        print('The temperature in',city,'is',weather_dict[pre+'temp_f'],'degrees F')
        print()
    elif info == 'humidity':
        print('The humidity in',city,'is',weather_dict[pre+'relative_humidity']+'%')
        print()
    elif info == 'wind':
        print('The wind in', city, 'is',weather_dict[pre+'wind_string'])
        print()
    elif info == 'observation':
        print('The observation time is',weather_dict[pre+'observation_time'])
        print()
    elif info == 'done':
        print()
        keepgoing = False
    else:
        print('Information unavailable. Please try again')
        print()
        
export = input('Would you like to export the full weather report? (yes/no) ')
if export == 'yes':
    fileobj = open("weatherreport.txt", 'w')
    header = 'Weather for ' + city
    fileobj.write(header)
    fileobj.write('\n')
    fileobj.write('\n')
    fileobj.write('Location: ')
    fileobj.write(weather_dict[pre+'location'])
    fileobj.write('\n')
    fileobj.write('Weather: ')
    fileobj.write(weather_dict[pre+'weather'])
    fileobj.write('\n')
    fileobj.write('Observation: ')
    fileobj.write(weather_dict[pre+'observation_time'])
    fileobj.write('\n')
    fileobj.write('Temperature: ')
    fileobj.write(weather_dict[pre+'temp_f'])
    fileobj.write(' degrees F')
    fileobj.write('\n')
    fileobj.write('Wind: ')
    fileobj.write(weather_dict[pre+'wind_string'])
    fileobj.write('\n')
    fileobj.write('Humidity: ')
    fileobj.write(weather_dict[pre+'relative_humidity'])
    fileobj.write('%')
    fileobj.close()
    

