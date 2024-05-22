from geopy.geocoders import Nominatim
import haversine as hs
import geocoder
import csv
import pandas

csvFile = pandas.read_csv('C:/Users/Surya Vemuri/Downloads/EVIndia.csv')
cran = csvFile['Range'].tolist()
cname = csvFile['Car'].tolist()
car = input("Enter a car: ")
battery = [30.2, 26, 40.5, 50.3, 39.2, 90, 93.4, 71.7, 80, 71, 79.2, 71]
for i in range(0, 14):
    if car.lower() in cname[i].lower():
        crange = int(cran[i][0:4])
        cbat = battery[i]
        break
while True:
    drive = input("Where are you going to drive today? ")
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(drive)
    print("You'll be going to ", getLoc)
    add = (getLoc.latitude, getLoc.longitude)
    g = geocoder.ip('me')
    dist = (hs.haversine(add, g.latlng))
    power_consumed = 0.1*dist
    powerleft = cbat - power_consumed
    crange1 = powerleft/0.1
    print("Range: ", crange)
    if(crange1<0):
        print("You will not be able to make it to your destination with the amount of charge you have left. Please go to the nearest Charging Station as soon as possible.\n")
    else:
        ch = input("Drive to your destination?(y/n)");
        if(ch.lower() == 'y'):
            crange = crange1
            cbat = powerleft
        else:
            break
    print("Range left: ", crange)
    gh = input("Would you like to continue?(y/n)")
    if gh == 'y':
        continue
    else:
        break
        



