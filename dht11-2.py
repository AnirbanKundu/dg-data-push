T RUN FROM TERMINAL USING sudo
 
import subprocess
import re
import sys
import time
 
while(True):
 
# read the sensor for Temperature on Pin 4
output = subprocess.check_output(["./Adafruit_DHT", "11", "4"]);
print output
matches = re.search(“Temp =\s+([0-9.]+)”, output)
if (not matches):
time.sleep(3)
continue
temp = float(matches.group(1))
ftemp= temp* 9.0 / 5.0 + 32.0
 
# Read the sensor for Humidity on Pin 4
matches = re.search(“Hum =\s+([0-9.]+)”, output)
if (not matches):
time.sleep(3)
continue
humidity = float(matches.group(1))
 
#printout the information
print “Temperature: %.1f C” % temp
print “Temperature: %.1f F” % ftemp
print “Humidity: %.1f %%” % humidity

