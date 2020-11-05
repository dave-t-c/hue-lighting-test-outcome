import subprocess
import time
from phue import Bridge

# Input the correct IP for your bridge. 
# To connect, press the button on the top of the bridge, then run the script within 30 seconds.
bridge = Bridge('Bridge IP')
bridge.connect()

# Get a dictionary of lights, then get the light you want using its name.
lights = bridge.get_light_objects('name')
light = lights['Name of Lamp']
light.on = True

# Change the color to purple while the tests are taking place.
# Set the brightness to 0 to minimize the visible change in color.
# 
light.brightness = 0
light.hue = 50000
light.brightness = 100

# Run the tests, wait for it to finish and get the return code.
# In this example, mvn is used for testing. Please place this python file in the same directory as the pom.xml file.
# You can modify this to be whatever test command you want, as long as the test 
# return code is 0 on sucess or > 0 on failiure, it should still work.
child = subprocess.Popen("mvn clean test", shell=True, stdout=subprocess.PIPE)
child.wait()
rc = child.returncode

if rc > 0:
  # Set light to red, as it is an unexpected return code.
  light.hue = 65000
  print('Tests failed')
else:
  # Set light to green, as tests have passed.
  light.hue = 30000
  print('Tests passed')

# Display the result for 5 seconds, then turn the light off.
time.sleep(5) 
light.on = False
