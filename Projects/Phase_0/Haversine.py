import math
import re

print("When writing coordinates in DMS format, do so with a degree symbol, single quotation, double quotation splitting the Degrees, Minutes, Seconds, and Direction")

# Start User Input Coordinates
start_lat_dms = input("Enter the latitude of your starting point: ")
start_lat_deg, start_lat_min, start_lat_sec, start_lat_dir = re.split('[°\'"]', start_lat_dms)
start_lat = float(start_lat_deg) + float(start_lat_min)/60 + float(start_lat_sec)/3600 * (-1 if start_lat_dir in ["S"] else 1)

start_lon_dms = input("Enter the longitude of your starting point: ")
start_lon_deg, start_lon_min, start_lon_sec, start_lon_dir = re.split('[°\'"]', start_lon_dms)
start_lon = float(start_lon_deg) + float(start_lon_min)/60 + float(start_lon_sec)/3600 * (-1 if start_lon_dir in ["W"] else 1)

# End User Input Coordinates
end_lat_dms = input("Enter the latitude of your ending point: ")
end_lat_deg, end_lat_min, end_lat_sec, end_lat_dir = re.split('[°\'"]', end_lat_dms)
end_lat = float(end_lat_deg) + float(end_lat_min)/60 + float(end_lat_sec)/3600 * (-1 if end_lat_dir in ["S"] else 1)

end_lon_dms = input("Enter the longitude of your ending point: ")
end_lon_deg, end_lon_min, end_lon_sec, end_lon_dir = re.split('[°\'"]', end_lon_dms)
end_lon = float(end_lon_deg) + float(end_lon_min)/60 + float(end_lon_sec)/3600 * (-1 if end_lon_dir in ["W"] else 1)

# Prerequisite Calculations
radius = 6371

start_lat_rad = math.radians(start_lat)
end_lat_rad = math.radians(end_lat)
lat_dif = math.radians(start_lat - end_lat)
lon_dif = math.radians(start_lon - end_lon)

# Using Haversine Formula
a = math.sin(lat_dif/2) * math.sin(lat_dif/2) + math.cos(start_lat_rad) * math.cos(end_lat_rad) * math.sin(lon_dif/2) * math.sin(lon_dif/2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = radius * c

# Final Steps
choice = input("Select the units of distance: \n1. Miles \n2. Kilometers \n")

if choice == "1":
    print("The distance is", round(distance/1.609, 2), "miles")

if choice == "2":
    print("The distance is", round(distance, 2), "kilometers")
